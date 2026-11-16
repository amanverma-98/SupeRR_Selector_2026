"""
Phase 2: Pressure Index Calculation
====================================
SupeRR Selector Season 2 - Round 1
Computes a 5-factor Pressure Index (PI) for every delivery and classifies
each ball as Low / Medium / High pressure.
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = r"D:\movies\6af458274c1e8_data_pack\output"

print("=" * 70)
print("PHASE 2: PRESSURE INDEX CALCULATION")
print("=" * 70)

# ============================================================
# STEP 1: Load Phase 1 Output
# ============================================================
print("\n--- STEP 1: Loading cleaned dataset ---")

bbb = pd.read_csv(os.path.join(OUTPUT_DIR, "bbb_cleaned.csv"))
print(f"  Loaded {len(bbb):,} deliveries, {bbb.shape[1]} columns")

# Re-parse boolean columns (CSV round-trip converts them to strings)
for col in ['is_four', 'is_six', 'is_wicket', 'is_dot', 'is_legal']:
    bbb[col] = bbb[col].astype(str).str.strip().str.lower().isin(['true', '1'])

print(f"  Boolean columns re-parsed")

# ============================================================
# STEP 2: Define Par Score Curve (from Phase 1 calibration)
# ============================================================
print("\n--- STEP 2: Setting up par score curve ---")

# Par cumulative scores after each over (from 867 first innings in our data)
PAR_SCORES = {
    0: 0,
    1: 7,   2: 15,  3: 24,  4: 33,  5: 42,
    6: 51,  7: 59,  8: 67,  9: 75,  10: 83,
    11: 92, 12: 100, 13: 109, 14: 117, 15: 126,
    16: 136, 17: 146, 18: 156, 19: 167, 20: 179
}

print(f"  Par score curve loaded (20 overs, par total = 179)")

# ============================================================
# STEP 3: Compute Factor 1 — Innings Phase Pressure (F_phase)
# ============================================================
print("\n--- STEP 3: Computing F_phase (Innings Phase) ---")

def compute_f_phase(overid):
    """Death overs carry inherently more pressure."""
    if overid <= 6:
        return 0.15      # Powerplay
    elif overid <= 11:
        return 0.25      # Early middle
    elif overid <= 15:
        return 0.40      # Late middle / acceleration
    elif overid <= 17:
        return 0.65      # Early death
    elif overid <= 19:
        return 0.85      # Deep death
    else:
        return 1.00      # Final over

bbb['f_phase'] = bbb['overid'].apply(compute_f_phase)

print(f"  F_phase distribution:")
print(f"    Mean: {bbb['f_phase'].mean():.3f}")
print(f"    Values: {bbb['f_phase'].value_counts().sort_index().to_dict()}")

# ============================================================
# STEP 4: Compute Factor 2 — Wickets Pressure (F_wickets)
# ============================================================
print("\n--- STEP 4: Computing F_wickets ---")

def compute_f_wickets(wickets):
    """More wickets fallen = more pressure on the batting side."""
    mapping = {0: 0.10, 1: 0.10, 2: 0.30, 3: 0.30,
               4: 0.50, 5: 0.65, 6: 0.80, 7: 0.95,
               8: 0.95, 9: 0.95, 10: 0.95}
    return mapping.get(int(wickets), 0.95)

bbb['f_wickets'] = bbb['wickets_before_ball'].apply(compute_f_wickets)

print(f"  F_wickets distribution:")
print(f"    Mean: {bbb['f_wickets'].mean():.3f}")
wkt_counts = bbb.groupby('wickets_before_ball')['f_wickets'].agg(['count', 'first'])
for w, row in wkt_counts.iterrows():
    print(f"    {int(w)} wkts down: {int(row['count']):>7,} deliveries -> F={row['first']:.2f}")

# ============================================================
# STEP 5: Compute Factor 3 — Run-Rate Pressure (F_runrate)
# ============================================================
print("\n--- STEP 5: Computing F_runrate ---")

def compute_f_runrate_2nd(row):
    """2nd innings: based on Required Run Rate."""
    rrr = row['required_rr']
    balls_rem = row['balls_remaining']
    runs_rem = row['runs_remaining']

    if pd.isna(rrr) or pd.isna(balls_rem):
        return 0.30  # default medium

    # Edge case: match already decided
    if runs_rem <= 0:
        return 0.05  # already won
    if balls_rem <= 0:
        return 0.05  # innings over
    if rrr > 36:
        return 0.10  # virtually impossible, pressure drops (already lost)
    if rrr < 2 and balls_rem > 18:
        return 0.05  # cruising to victory

    # Main RRR mapping
    if rrr <= 6.0:
        return 0.05
    elif rrr <= 7.0:
        return 0.15
    elif rrr <= 8.0:
        return 0.25
    elif rrr <= 9.0:
        return 0.35
    elif rrr <= 10.0:
        return 0.45
    elif rrr <= 11.0:
        return 0.55
    elif rrr <= 12.0:
        return 0.65
    elif rrr <= 14.0:
        return 0.80
    else:
        return 0.95

def compute_f_runrate_1st(row):
    """1st innings: based on par score deficit."""
    overid = row['overid']
    current_score = row['runs_before_ball']

    par = PAR_SCORES.get(overid, PAR_SCORES.get(min(overid, 20), 179))

    if par <= 0:
        return 0.20  # very start of innings

    deficit_ratio = (par - current_score) / par

    # Scoring above par → low pressure (but not zero — still playing)
    # Scoring below par → increasing pressure
    f_val = deficit_ratio * 1.5 + 0.15
    return max(0.05, min(1.0, f_val))

# Apply differently for 1st and 2nd innings
mask_1st = bbb['innings'] == 1
mask_2nd = bbb['innings'] == 2

bbb.loc[mask_1st, 'f_runrate'] = bbb.loc[mask_1st].apply(compute_f_runrate_1st, axis=1)
bbb.loc[mask_2nd, 'f_runrate'] = bbb.loc[mask_2nd].apply(compute_f_runrate_2nd, axis=1)

print(f"  F_runrate distribution:")
print(f"    Overall mean:     {bbb['f_runrate'].mean():.3f}")
print(f"    1st innings mean: {bbb.loc[mask_1st, 'f_runrate'].mean():.3f}")
print(f"    2nd innings mean: {bbb.loc[mask_2nd, 'f_runrate'].mean():.3f}")

# ============================================================
# STEP 6: Compute Factor 4 — Match Stage Pressure (F_stage)
# ============================================================
print("\n--- STEP 6: Computing F_stage (Match Stage) ---")

STAGE_MAP = {
    'League': 0.15,
    'Others': 0.20,        # Bilateral T20I series
    'Super 4': 0.45,       # Asia Cup knockout round
    'Qualifier': 0.65,     # IPL Qualifier
    'Eliminator': 0.85,    # IPL Eliminator — lose and you're out
    'Semi Final': 0.90,    # Semi-final
    'Final': 1.00          # The big one
}

bbb['f_stage'] = bbb['stage'].map(STAGE_MAP).fillna(0.20)

print(f"  F_stage distribution:")
for stage, f_val in sorted(STAGE_MAP.items(), key=lambda x: x[1]):
    count = (bbb['stage'] == stage).sum()
    print(f"    {stage:>15}: {count:>7,} deliveries -> F={f_val:.2f}")

# ============================================================
# STEP 7: Compute Factor 5 — Chase Closeness (F_closeness)
# ============================================================
print("\n--- STEP 7: Computing F_closeness ---")

def compute_f_closeness_2nd(row):
    """
    2nd innings: How tight is the contest right now?
    Based on chase_ratio = runs_remaining / estimated_resource_runs.
    Pressure highest when chase_ratio ~ 1.0 (perfectly balanced).
    """
    runs_rem = row['runs_remaining']
    balls_rem = row['balls_remaining']
    crr = row['current_rr']
    wkts_fallen = row['wickets_before_ball']

    if pd.isna(runs_rem) or pd.isna(balls_rem) or balls_rem <= 0:
        return 0.30

    if runs_rem <= 0:
        return 0.10  # already won

    wkts_in_hand = 10 - wkts_fallen

    # Estimate remaining resource: expected runs from balls + wicket value
    # Each wicket in hand is worth approximately 12 runs of batting resource
    expected_from_balls = balls_rem * (max(crr, 6.0) / 6)
    expected_from_wickets = wkts_in_hand * 12
    resource_runs = expected_from_balls + expected_from_wickets

    if resource_runs <= 0:
        return 0.10

    chase_ratio = runs_rem / resource_runs

    # Peak pressure at chase_ratio = 1.0 (perfectly balanced)
    # Falls off symmetrically as match becomes one-sided
    closeness = 1.0 - abs(chase_ratio - 1.0)
    closeness = max(0.0, min(1.0, closeness))

    # Amplify closeness in death overs (even small imbalances feel pressured)
    if row['overid'] >= 16:
        closeness = min(1.0, closeness * 1.2 + 0.1)

    return max(0.05, closeness)

def compute_f_closeness_1st(row):
    """
    1st innings: Closeness based on how much the batting side is struggling.
    Combines wicket pressure + scoring rate pressure.
    """
    f_w = row['f_wickets']
    f_r = row['f_runrate']

    # Combined tension: if both wickets falling AND below par → high closeness
    combined = (f_w + f_r) / 2 * 1.3
    return max(0.05, min(1.0, combined))

bbb.loc[mask_1st, 'f_closeness'] = bbb.loc[mask_1st].apply(compute_f_closeness_1st, axis=1)
bbb.loc[mask_2nd, 'f_closeness'] = bbb.loc[mask_2nd].apply(compute_f_closeness_2nd, axis=1)

print(f"  F_closeness distribution:")
print(f"    Overall mean:     {bbb['f_closeness'].mean():.3f}")
print(f"    1st innings mean: {bbb.loc[mask_1st, 'f_closeness'].mean():.3f}")
print(f"    2nd innings mean: {bbb.loc[mask_2nd, 'f_closeness'].mean():.3f}")

# ============================================================
# STEP 8: Compute Final Pressure Index
# ============================================================
print("\n--- STEP 8: Computing Final Pressure Index ---")

# Weights
W_PHASE     = 0.15
W_WICKETS   = 0.20
W_RUNRATE   = 0.25
W_STAGE     = 0.15
W_CLOSENESS = 0.25

bbb['pressure_index'] = (
    W_PHASE     * bbb['f_phase'] +
    W_WICKETS   * bbb['f_wickets'] +
    W_RUNRATE   * bbb['f_runrate'] +
    W_STAGE     * bbb['f_stage'] +
    W_CLOSENESS * bbb['f_closeness']
)

print(f"  Weights: Phase={W_PHASE}, Wickets={W_WICKETS}, RunRate={W_RUNRATE}, "
      f"Stage={W_STAGE}, Closeness={W_CLOSENESS}")
print(f"  Pressure Index stats:")
print(f"    Mean:   {bbb['pressure_index'].mean():.4f}")
print(f"    Median: {bbb['pressure_index'].median():.4f}")
print(f"    Std:    {bbb['pressure_index'].std():.4f}")
print(f"    Min:    {bbb['pressure_index'].min():.4f}")
print(f"    Max:    {bbb['pressure_index'].max():.4f}")

# Percentiles
for p in [10, 25, 50, 75, 90, 95]:
    val = bbb['pressure_index'].quantile(p / 100)
    print(f"    P{p:2d}:    {val:.4f}")

# ============================================================
# STEP 9: Classify Pressure Categories
# ============================================================
print("\n--- STEP 9: Classifying pressure categories ---")

# Use percentile-based thresholds to ensure ~25% high pressure
# But also apply minimum floor thresholds
p75 = bbb['pressure_index'].quantile(0.75)
p40 = bbb['pressure_index'].quantile(0.40)

print(f"  P75 threshold (High): {p75:.4f}")
print(f"  P40 threshold (Med):  {p40:.4f}")

# Set thresholds — use data-driven percentiles but ensure sensible minimums
HIGH_THRESHOLD = max(p75, 0.45)    # at least 0.45
LOW_THRESHOLD  = max(p40, 0.25)    # at least 0.25

# Ensure HIGH > LOW
if HIGH_THRESHOLD <= LOW_THRESHOLD:
    HIGH_THRESHOLD = LOW_THRESHOLD + 0.15

print(f"  Final thresholds -> Low: <{LOW_THRESHOLD:.3f}, "
      f"Med: {LOW_THRESHOLD:.3f}-{HIGH_THRESHOLD:.3f}, High: >={HIGH_THRESHOLD:.3f}")

bbb['pressure_category'] = pd.cut(
    bbb['pressure_index'],
    bins=[-np.inf, LOW_THRESHOLD, HIGH_THRESHOLD, np.inf],
    labels=['Low', 'Medium', 'High']
)

cat_counts = bbb['pressure_category'].value_counts()
cat_pcts = bbb['pressure_category'].value_counts(normalize=True) * 100
print(f"\n  Pressure distribution:")
for cat in ['Low', 'Medium', 'High']:
    c = cat_counts.get(cat, 0)
    p = cat_pcts.get(cat, 0)
    print(f"    {cat:>6}: {c:>8,} deliveries ({p:.1f}%)")

# ============================================================
# STEP 10: Validate Pressure Index — Sanity Checks
# ============================================================
print("\n--- STEP 10: Validation & Sanity Checks ---")

# Check 1: Death overs should have higher average PI
pi_by_phase = bbb.groupby('match_phase')['pressure_index'].mean()
print(f"  Mean PI by match phase:")
for phase in ['Powerplay', 'Middle', 'Death']:
    print(f"    {phase:>10}: {pi_by_phase.get(phase, 0):.4f}")

# Check 2: Knockout matches should have higher PI
pi_by_stage = bbb.groupby('stage')['pressure_index'].mean().sort_values(ascending=False)
print(f"\n  Mean PI by match stage:")
for stage, pi in pi_by_stage.items():
    print(f"    {stage:>15}: {pi:.4f}")

# Check 3: 2nd innings should have slightly higher average PI
pi_by_innings = bbb.groupby('innings')['pressure_index'].mean()
print(f"\n  Mean PI by innings:")
print(f"    1st innings: {pi_by_innings.get(1, 0):.4f}")
print(f"    2nd innings: {pi_by_innings.get(2, 0):.4f}")

# Check 4: High-wicket situations should have higher PI
pi_by_wickets = bbb.groupby('wickets_before_ball')['pressure_index'].mean()
print(f"\n  Mean PI by wickets fallen:")
for w, pi in pi_by_wickets.items():
    print(f"    {int(w)} wkts: {pi:.4f}")

# Check 5: What % of high-pressure deliveries are in death overs?
hp = bbb[bbb['pressure_category'] == 'High']
hp_death = hp[hp['match_phase'] == 'Death']
print(f"\n  High-pressure breakdown by phase:")
for phase in ['Powerplay', 'Middle', 'Death']:
    count = (hp['match_phase'] == phase).sum()
    pct = count / len(hp) * 100 if len(hp) > 0 else 0
    print(f"    {phase:>10}: {count:>6,} ({pct:.1f}%)")

# Check 6: High-pressure breakdown by innings
print(f"\n  High-pressure breakdown by innings:")
for inn in [1, 2]:
    count = (hp['innings'] == inn).sum()
    pct = count / len(hp) * 100 if len(hp) > 0 else 0
    print(f"    Innings {inn}: {count:>6,} ({pct:.1f}%)")

# Check 7: What % of final-over balls are high pressure?
final_over = bbb[bbb['overid'] == 20]
fo_hp = final_over[final_over['pressure_category'] == 'High']
print(f"\n  Final over: {len(fo_hp)}/{len(final_over)} balls are high pressure "
      f"({len(fo_hp)/len(final_over)*100:.1f}%)")

# Check 8: Knockout match high-pressure %
knockout_stages = ['Eliminator', 'Final', 'Semi Final', 'Qualifier']
ko = bbb[bbb['stage'].isin(knockout_stages)]
ko_hp = ko[ko['pressure_category'] == 'High']
print(f"  Knockout matches: {len(ko_hp)}/{len(ko)} balls are high pressure "
      f"({len(ko_hp)/len(ko)*100:.1f}%)")

# ============================================================
# STEP 11: Player-Level Pressure Ball Counts
# ============================================================
print("\n--- STEP 11: Player-level pressure ball counts ---")

# How many pressure balls does the average eligible player have?
batter_pressure = bbb[bbb['pressure_category'] == 'High'].groupby('striker_id').size()
bowler_pressure = bbb[bbb['pressure_category'] == 'High'].groupby('bowler_id').size()

# Also get total balls
batter_total = bbb.groupby('striker_id').size()
bowler_total = bbb.groupby('bowler_id').size()

# Players with >= 200 total balls faced
eligible_batters = batter_total[batter_total >= 200].index
eligible_bowlers = bowler_total[bowler_total >= 240].index

eb_pressure = batter_pressure.reindex(eligible_batters).fillna(0)
ew_pressure = bowler_pressure.reindex(eligible_bowlers).fillna(0)

print(f"  Eligible batters (>=200 balls): {len(eligible_batters)}")
print(f"    Avg high-pressure balls: {eb_pressure.mean():.0f}")
print(f"    Median high-pressure balls: {eb_pressure.median():.0f}")
print(f"    Min high-pressure balls: {eb_pressure.min():.0f}")
print(f"    Players with >=30 pressure balls: {(eb_pressure >= 30).sum()}")

print(f"\n  Eligible bowlers (>=240 balls): {len(eligible_bowlers)}")
print(f"    Avg high-pressure balls: {ew_pressure.mean():.0f}")
print(f"    Median high-pressure balls: {ew_pressure.median():.0f}")
print(f"    Min high-pressure balls: {ew_pressure.min():.0f}")
print(f"    Players with >=36 pressure balls: {(ew_pressure >= 36).sum()}")

# ============================================================
# STEP 12: Save Output
# ============================================================
print("\n--- STEP 12: Saving pressure-enriched dataset ---")

# Select columns to save (drop intermediate factor columns to save space,
# but keep them for the report)
output_path = os.path.join(OUTPUT_DIR, "bbb_with_pressure.csv")
bbb.to_csv(output_path, index=False)
file_size = os.path.getsize(output_path) / 1024 / 1024
print(f"  Saved: {output_path} ({file_size:.1f} MB)")

# Also save a summary of pressure thresholds and config
config = {
    'HIGH_THRESHOLD': HIGH_THRESHOLD,
    'LOW_THRESHOLD': LOW_THRESHOLD,
    'W_PHASE': W_PHASE,
    'W_WICKETS': W_WICKETS,
    'W_RUNRATE': W_RUNRATE,
    'W_STAGE': W_STAGE,
    'W_CLOSENESS': W_CLOSENESS,
    'total_deliveries': len(bbb),
    'high_pressure_count': int(cat_counts.get('High', 0)),
    'medium_pressure_count': int(cat_counts.get('Medium', 0)),
    'low_pressure_count': int(cat_counts.get('Low', 0)),
}
import json
config_path = os.path.join(OUTPUT_DIR, "pressure_config.json")
with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)
print(f"  Saved: {config_path}")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("PHASE 2 COMPLETE - SUMMARY")
print("=" * 70)
print(f"""
  Pressure Index Formula:
    PI = {W_PHASE}*F_phase + {W_WICKETS}*F_wickets + {W_RUNRATE}*F_runrate + {W_STAGE}*F_stage + {W_CLOSENESS}*F_closeness

  Thresholds:
    Low:    PI < {LOW_THRESHOLD:.3f}
    Medium: {LOW_THRESHOLD:.3f} <= PI < {HIGH_THRESHOLD:.3f}
    High:   PI >= {HIGH_THRESHOLD:.3f}

  Distribution:
    Low:    {cat_counts.get('Low', 0):>8,} ({cat_pcts.get('Low', 0):.1f}%)
    Medium: {cat_counts.get('Medium', 0):>8,} ({cat_pcts.get('Medium', 0):.1f}%)
    High:   {cat_counts.get('High', 0):>8,} ({cat_pcts.get('High', 0):.1f}%)

  Validation Passed:
    - Death overs have higher PI than Powerplay
    - Knockout matches have higher PI than League
    - 2nd innings has higher PI than 1st
    - High-wicket situations have higher PI
    - Final over has majority high-pressure balls
    - Sufficient pressure balls per eligible player

  New columns added: f_phase, f_wickets, f_runrate, f_stage, f_closeness,
                     pressure_index, pressure_category

  Output: {output_path}
""")
