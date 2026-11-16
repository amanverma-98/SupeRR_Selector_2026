"""
Phase 3: Player Performance Metrics & Ranking
===============================================
SupeRR Selector Season 2 - Round 1
Computes batting/bowling metrics under pressure vs overall,
calculates uplift, applies eligibility + shrinkage, ranks Top 10.
"""

import pandas as pd
import numpy as np
import os
import json
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = r"D:\movies\6af458274c1e8_data_pack\output"

print("=" * 70)
print("PHASE 3: PLAYER PERFORMANCE METRICS & RANKING")
print("=" * 70)

# ============================================================
# STEP 1: Load Phase 2 Output
# ============================================================
print("\n--- STEP 1: Loading pressure-enriched dataset ---")

bbb = pd.read_csv(os.path.join(OUTPUT_DIR, "bbb_with_pressure.csv"))
player_names = pd.read_csv(os.path.join(OUTPUT_DIR, "player_names.csv"))

with open(os.path.join(OUTPUT_DIR, "pressure_config.json"), 'r') as f:
    config = json.load(f)

# Re-parse booleans
for col in ['is_four', 'is_six', 'is_wicket', 'is_dot', 'is_legal']:
    bbb[col] = bbb[col].astype(str).str.strip().str.lower().isin(['true', '1'])

print(f"  Loaded {len(bbb):,} deliveries")
print(f"  High pressure: {(bbb['pressure_category'] == 'High').sum():,}")
print(f"  Player names: {len(player_names)}")

# ============================================================
# STEP 2: Define Metric Computation Functions
# ============================================================
print("\n--- STEP 2: Defining metric functions ---")

def compute_batting_metrics(df):
    """Compute batting metrics from a group of deliveries for a batter."""
    balls = len(df)
    if balls == 0:
        return pd.Series({
            'bat_balls': 0, 'bat_runs': 0, 'bat_sr': np.nan,
            'bat_avg': np.nan, 'bat_boundary_pct': np.nan,
            'bat_dot_pct': np.nan, 'bat_impact': np.nan,
            'bat_fours': 0, 'bat_sixes': 0, 'bat_dismissals': 0,
            'bat_dots': 0
        })

    runs = df['runs'].sum()
    fours = df['is_four'].sum()
    sixes = df['is_six'].sum()
    dismissals = df['is_wicket'].sum()
    dots = ((df['runs'] == 0) & (df['extras_type'] == 'None')).sum()

    sr = (runs / balls * 100) if balls > 0 else 0
    avg = (runs / dismissals) if dismissals > 0 else runs * 1.5  # not-out bonus
    boundary_pct = ((fours + sixes) / balls * 100) if balls > 0 else 0
    dot_pct = (dots / balls * 100) if balls > 0 else 0
    impact = ((runs + 10 * sixes + 5 * fours) / balls) if balls > 0 else 0

    return pd.Series({
        'bat_balls': balls,
        'bat_runs': runs,
        'bat_sr': sr,
        'bat_avg': avg,
        'bat_boundary_pct': boundary_pct,
        'bat_dot_pct': dot_pct,
        'bat_impact': impact,
        'bat_fours': fours,
        'bat_sixes': sixes,
        'bat_dismissals': dismissals,
        'bat_dots': dots
    })


def compute_bowling_metrics(df):
    """Compute bowling metrics from a group of deliveries for a bowler."""
    balls = len(df)
    if balls == 0:
        return pd.Series({
            'bowl_balls': 0, 'bowl_runs_conceded': 0, 'bowl_econ': np.nan,
            'bowl_sr': np.nan, 'bowl_dot_pct': np.nan,
            'bowl_boundary_pct': np.nan, 'bowl_extras_pct': np.nan,
            'bowl_wickets': 0, 'bowl_dots': 0, 'bowl_legal': 0
        })

    runs_conceded = df['total_runs'].sum()
    legal_balls = df['is_legal'].sum()
    overs = legal_balls / 6

    # Wickets: only count bowler-attributable dismissals
    bowler_dismissals = ['Bowled', 'Caught', 'LBW', 'Stump', 'Hit Wicket']
    wickets = df[df['dismissal_type'].isin(bowler_dismissals)]['is_wicket'].sum()
    total_wickets = df['is_wicket'].sum()  # including run outs

    dots = ((df['runs'] == 0) & (df['extras_type'] == 'None')).sum()
    boundaries_conceded = (df['is_four'].sum() + df['is_six'].sum())
    extras = df[df['extras_type'].isin(['wide', 'Overstep'])].shape[0]

    econ = (runs_conceded / overs) if overs > 0 else 0
    bowl_sr = (legal_balls / wickets) if wickets > 0 else legal_balls * 1.5  # no-wicket penalty
    dot_pct = (dots / balls * 100) if balls > 0 else 0
    boundary_pct = (boundaries_conceded / balls * 100) if balls > 0 else 0
    extras_pct = (extras / balls * 100) if balls > 0 else 0

    return pd.Series({
        'bowl_balls': balls,
        'bowl_runs_conceded': runs_conceded,
        'bowl_econ': econ,
        'bowl_sr': bowl_sr,
        'bowl_dot_pct': dot_pct,
        'bowl_boundary_pct': boundary_pct,
        'bowl_extras_pct': extras_pct,
        'bowl_wickets': wickets,
        'bowl_dots': dots,
        'bowl_legal': legal_balls
    })

print("  Batting metrics: SR, Average, Boundary%, Dot%, Impact")
print("  Bowling metrics: Economy, SR, Dot%, Boundary%, Extras%")

# ============================================================
# STEP 3: Compute Batting Metrics — Overall & Under Pressure
# ============================================================
print("\n--- STEP 3: Computing batting metrics ---")

# Overall batting metrics per player
bat_overall = bbb.groupby('striker_id').apply(compute_batting_metrics).reset_index()
bat_overall.columns = ['player_id'] + ['all_' + c for c in bat_overall.columns[1:]]

# High-pressure batting metrics
hp_bat = bbb[bbb['pressure_category'] == 'High']
bat_pressure = hp_bat.groupby('striker_id').apply(compute_batting_metrics).reset_index()
bat_pressure.columns = ['player_id'] + ['hp_' + c for c in bat_pressure.columns[1:]]

# Low-pressure batting metrics (for contrast)
lp_bat = bbb[bbb['pressure_category'] == 'Low']
bat_low = lp_bat.groupby('striker_id').apply(compute_batting_metrics).reset_index()
bat_low.columns = ['player_id'] + ['lp_' + c for c in bat_low.columns[1:]]

# Merge
batters = bat_overall.merge(bat_pressure, on='player_id', how='left')
batters = batters.merge(bat_low, on='player_id', how='left')

# Count matches and seasons
batter_matches = bbb.groupby('striker_id')['match_id'].nunique().reset_index()
batter_matches.columns = ['player_id', 'matches_batted']

batter_seasons = bbb.groupby('striker_id')['season'].nunique().reset_index()
batter_seasons.columns = ['player_id', 'seasons_batted']

# Modal batting order (most common position)
batter_order = bbb.groupby('striker_id')['batting_order'].agg(
    lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 0
).reset_index()
batter_order.columns = ['player_id', 'typical_batting_order']

batters = batters.merge(batter_matches, on='player_id', how='left')
batters = batters.merge(batter_seasons, on='player_id', how='left')
batters = batters.merge(batter_order, on='player_id', how='left')

# Add player names
batters = batters.merge(player_names, on='player_id', how='left')

# Fill missing names from bbb
missing_names = batters[batters['player_name'].isna()]['player_id']
if len(missing_names) > 0:
    name_fill = bbb[bbb['striker_id'].isin(missing_names)][['striker_id', 'striker_name']].drop_duplicates()
    name_fill.columns = ['player_id', 'player_name']
    for _, row in name_fill.iterrows():
        batters.loc[batters['player_id'] == row['player_id'], 'player_name'] = row['player_name']

print(f"  Total batters: {len(batters)}")
print(f"  Batters with pressure data: {batters['hp_bat_balls'].notna().sum()}")

# ============================================================
# STEP 4: Compute Bowling Metrics — Overall & Under Pressure
# ============================================================
print("\n--- STEP 4: Computing bowling metrics ---")

# Overall bowling metrics
bowl_overall = bbb.groupby('bowler_id').apply(compute_bowling_metrics).reset_index()
bowl_overall.columns = ['player_id'] + ['all_' + c for c in bowl_overall.columns[1:]]

# High-pressure bowling metrics
hp_bowl = bbb[bbb['pressure_category'] == 'High']
bowl_pressure = hp_bowl.groupby('bowler_id').apply(compute_bowling_metrics).reset_index()
bowl_pressure.columns = ['player_id'] + ['hp_' + c for c in bowl_pressure.columns[1:]]

# Low-pressure bowling metrics
lp_bowl = bbb[bbb['pressure_category'] == 'Low']
bowl_low = lp_bowl.groupby('bowler_id').apply(compute_bowling_metrics).reset_index()
bowl_low.columns = ['player_id'] + ['lp_' + c for c in bowl_low.columns[1:]]

# Merge
bowlers = bowl_overall.merge(bowl_pressure, on='player_id', how='left')
bowlers = bowlers.merge(bowl_low, on='player_id', how='left')

# Count matches and seasons
bowler_matches = bbb.groupby('bowler_id')['match_id'].nunique().reset_index()
bowler_matches.columns = ['player_id', 'matches_bowled']

bowler_seasons = bbb.groupby('bowler_id')['season'].nunique().reset_index()
bowler_seasons.columns = ['player_id', 'seasons_bowled']

bowlers = bowlers.merge(bowler_matches, on='player_id', how='left')
bowlers = bowlers.merge(bowler_seasons, on='player_id', how='left')

# Add player names
bowlers = bowlers.merge(player_names, on='player_id', how='left')
missing_names_b = bowlers[bowlers['player_name'].isna()]['player_id']
if len(missing_names_b) > 0:
    name_fill_b = bbb[bbb['bowler_id'].isin(missing_names_b)][['bowler_id', 'bowler_name']].drop_duplicates()
    name_fill_b.columns = ['player_id', 'player_name']
    for _, row in name_fill_b.iterrows():
        bowlers.loc[bowlers['player_id'] == row['player_id'], 'player_name'] = row['player_name']

print(f"  Total bowlers: {len(bowlers)}")
print(f"  Bowlers with pressure data: {bowlers['hp_bowl_balls'].notna().sum()}")

# ============================================================
# STEP 5: Apply Eligibility Filters
# ============================================================
print("\n--- STEP 5: Applying eligibility filters ---")

# BATTER eligibility
bat_eligible = batters[
    (batters['all_bat_balls'] >= 200) &         # Minimum balls faced
    (batters['hp_bat_balls'] >= 30) &            # Minimum pressure balls
    (batters['matches_batted'] >= 15) &          # Minimum matches
    (batters['seasons_batted'] >= 2) &           # At least 2 seasons
    (batters['typical_batting_order'] <= 7)       # Not a pure tailender
].copy()

print(f"  Batter eligibility funnel:")
print(f"    Total batters:            {len(batters)}")
print(f"    >= 200 balls faced:       {(batters['all_bat_balls'] >= 200).sum()}")
print(f"    >= 30 pressure balls:     {((batters['all_bat_balls'] >= 200) & (batters['hp_bat_balls'] >= 30)).sum()}")
print(f"    >= 15 matches:            {((batters['all_bat_balls'] >= 200) & (batters['hp_bat_balls'] >= 30) & (batters['matches_batted'] >= 15)).sum()}")
print(f"    >= 2 seasons:             {((batters['all_bat_balls'] >= 200) & (batters['hp_bat_balls'] >= 30) & (batters['matches_batted'] >= 15) & (batters['seasons_batted'] >= 2)).sum()}")
print(f"    Batting order <= 7:       {len(bat_eligible)}")
print(f"  -> ELIGIBLE BATTERS: {len(bat_eligible)}")

# BOWLER eligibility
bowl_eligible = bowlers[
    (bowlers['all_bowl_balls'] >= 240) &         # Minimum balls bowled
    (bowlers['hp_bowl_balls'] >= 36) &            # Minimum pressure balls
    (bowlers['matches_bowled'] >= 15) &           # Minimum matches
    (bowlers['seasons_bowled'] >= 2)              # At least 2 seasons
].copy()

print(f"\n  Bowler eligibility funnel:")
print(f"    Total bowlers:            {len(bowlers)}")
print(f"    >= 240 balls bowled:      {(bowlers['all_bowl_balls'] >= 240).sum()}")
print(f"    >= 36 pressure balls:     {((bowlers['all_bowl_balls'] >= 240) & (bowlers['hp_bowl_balls'] >= 36)).sum()}")
print(f"    >= 15 matches:            {((bowlers['all_bowl_balls'] >= 240) & (bowlers['hp_bowl_balls'] >= 36) & (bowlers['matches_bowled'] >= 15)).sum()}")
print(f"    >= 2 seasons:             {((bowlers['all_bowl_balls'] >= 240) & (bowlers['hp_bowl_balls'] >= 36) & (bowlers['matches_bowled'] >= 15) & (bowlers['seasons_bowled'] >= 2)).sum()}")
print(f"  -> ELIGIBLE BOWLERS: {len(bowl_eligible)}")

# ============================================================
# STEP 6: Compute Uplift Scores
# ============================================================
print("\n--- STEP 6: Computing uplift scores ---")

# BATTING UPLIFTS
# SR uplift: positive = better SR under pressure
bat_eligible['sr_uplift'] = (
    (bat_eligible['hp_bat_sr'] - bat_eligible['all_bat_sr']) / bat_eligible['all_bat_sr']
)

# Average uplift: positive = higher average under pressure
bat_eligible['avg_uplift'] = (
    (bat_eligible['hp_bat_avg'] - bat_eligible['all_bat_avg']) / bat_eligible['all_bat_avg']
)
# Cap avg_uplift at reasonable range to prevent not-out inflation
bat_eligible['avg_uplift'] = bat_eligible['avg_uplift'].clip(-1, 3)

# Boundary% uplift: positive = more boundaries under pressure
bat_eligible['boundary_uplift'] = (
    (bat_eligible['hp_bat_boundary_pct'] - bat_eligible['all_bat_boundary_pct']) /
    bat_eligible['all_bat_boundary_pct'].clip(lower=1)
)

# Dot% uplift: REVERSED — lower dots under pressure is better
bat_eligible['dot_uplift'] = (
    (bat_eligible['all_bat_dot_pct'] - bat_eligible['hp_bat_dot_pct']) /
    bat_eligible['all_bat_dot_pct'].clip(lower=1)
)

# Impact uplift: positive = higher impact under pressure
bat_eligible['impact_uplift'] = (
    (bat_eligible['hp_bat_impact'] - bat_eligible['all_bat_impact']) /
    bat_eligible['all_bat_impact'].clip(lower=0.1)
)

print(f"  Batting uplifts computed for {len(bat_eligible)} players")
print(f"    SR uplift:       mean={bat_eligible['sr_uplift'].mean():.3f}, std={bat_eligible['sr_uplift'].std():.3f}")
print(f"    Avg uplift:      mean={bat_eligible['avg_uplift'].mean():.3f}, std={bat_eligible['avg_uplift'].std():.3f}")
print(f"    Boundary uplift: mean={bat_eligible['boundary_uplift'].mean():.3f}, std={bat_eligible['boundary_uplift'].std():.3f}")
print(f"    Dot uplift:      mean={bat_eligible['dot_uplift'].mean():.3f}, std={bat_eligible['dot_uplift'].std():.3f}")
print(f"    Impact uplift:   mean={bat_eligible['impact_uplift'].mean():.3f}, std={bat_eligible['impact_uplift'].std():.3f}")

# BOWLING UPLIFTS
# Economy uplift: REVERSED — lower economy under pressure is better
bowl_eligible['econ_uplift'] = (
    (bowl_eligible['all_bowl_econ'] - bowl_eligible['hp_bowl_econ']) /
    bowl_eligible['all_bowl_econ'].clip(lower=1)
)

# Bowling SR uplift: REVERSED — lower SR (more wickets) under pressure is better
bowl_eligible['bowl_sr_uplift'] = (
    (bowl_eligible['all_bowl_sr'] - bowl_eligible['hp_bowl_sr']) /
    bowl_eligible['all_bowl_sr'].clip(lower=1)
)
bowl_eligible['bowl_sr_uplift'] = bowl_eligible['bowl_sr_uplift'].clip(-1, 2)

# Dot% uplift: positive = more dots under pressure
bowl_eligible['bowl_dot_uplift'] = (
    (bowl_eligible['hp_bowl_dot_pct'] - bowl_eligible['all_bowl_dot_pct']) /
    bowl_eligible['all_bowl_dot_pct'].clip(lower=1)
)

# Boundary conceded uplift: REVERSED — fewer boundaries under pressure is better
bowl_eligible['bowl_bdry_uplift'] = (
    (bowl_eligible['all_bowl_boundary_pct'] - bowl_eligible['hp_bowl_boundary_pct']) /
    bowl_eligible['all_bowl_boundary_pct'].clip(lower=1)
)

# Extras uplift: REVERSED — fewer extras under pressure is better
bowl_eligible['bowl_extras_uplift'] = (
    (bowl_eligible['all_bowl_extras_pct'] - bowl_eligible['hp_bowl_extras_pct']) /
    bowl_eligible['all_bowl_extras_pct'].clip(lower=0.1)
)
bowl_eligible['bowl_extras_uplift'] = bowl_eligible['bowl_extras_uplift'].clip(-2, 2)

print(f"\n  Bowling uplifts computed for {len(bowl_eligible)} players")
print(f"    Econ uplift:     mean={bowl_eligible['econ_uplift'].mean():.3f}, std={bowl_eligible['econ_uplift'].std():.3f}")
print(f"    Bowl SR uplift:  mean={bowl_eligible['bowl_sr_uplift'].mean():.3f}, std={bowl_eligible['bowl_sr_uplift'].std():.3f}")
print(f"    Dot uplift:      mean={bowl_eligible['bowl_dot_uplift'].mean():.3f}, std={bowl_eligible['bowl_dot_uplift'].std():.3f}")
print(f"    Boundary uplift: mean={bowl_eligible['bowl_bdry_uplift'].mean():.3f}, std={bowl_eligible['bowl_bdry_uplift'].std():.3f}")
print(f"    Extras uplift:   mean={bowl_eligible['bowl_extras_uplift'].mean():.3f}, std={bowl_eligible['bowl_extras_uplift'].std():.3f}")

# ============================================================
# STEP 7: Bayesian Shrinkage
# ============================================================
print("\n--- STEP 7: Applying Bayesian shrinkage ---")

K_BAT = 50   # shrinkage parameter for batters
K_BOWL = 60  # shrinkage parameter for bowlers

def apply_shrinkage(series, pressure_balls, k, pop_mean):
    """Regress extreme uplift values toward population mean based on sample size."""
    shrinkage_factor = pressure_balls / (pressure_balls + k)
    return pop_mean + shrinkage_factor * (series - pop_mean)

# Batting shrinkage
for col in ['sr_uplift', 'avg_uplift', 'boundary_uplift', 'dot_uplift', 'impact_uplift']:
    pop_mean = bat_eligible[col].mean()
    bat_eligible[col + '_raw'] = bat_eligible[col].copy()
    bat_eligible[col] = apply_shrinkage(
        bat_eligible[col], bat_eligible['hp_bat_balls'], K_BAT, pop_mean
    )

# Bowling shrinkage
for col in ['econ_uplift', 'bowl_sr_uplift', 'bowl_dot_uplift', 'bowl_bdry_uplift', 'bowl_extras_uplift']:
    pop_mean = bowl_eligible[col].mean()
    bowl_eligible[col + '_raw'] = bowl_eligible[col].copy()
    bowl_eligible[col] = apply_shrinkage(
        bowl_eligible[col], bowl_eligible['hp_bowl_balls'], K_BOWL, pop_mean
    )

print(f"  Applied shrinkage (K_bat={K_BAT}, K_bowl={K_BOWL})")
print(f"  Batters: small-sample uplifts regressed toward population mean")
print(f"  Bowlers: small-sample uplifts regressed toward population mean")

# ============================================================
# STEP 8: Z-Score Normalization & Composite Scores
# ============================================================
print("\n--- STEP 8: Computing composite scores ---")

def zscore(series):
    """Z-score normalize a series."""
    m = series.mean()
    s = series.std()
    if s == 0 or pd.isna(s):
        return series * 0
    return (series - m) / s

# BATTING: Pressure Batting Score (PBS)
bat_eligible['z_sr']       = zscore(bat_eligible['sr_uplift'])
bat_eligible['z_avg']      = zscore(bat_eligible['avg_uplift'])
bat_eligible['z_boundary'] = zscore(bat_eligible['boundary_uplift'])
bat_eligible['z_dot']      = zscore(bat_eligible['dot_uplift'])
bat_eligible['z_impact']   = zscore(bat_eligible['impact_uplift'])

# Weighted composite
W_BAT = {'sr': 0.30, 'avg': 0.20, 'boundary': 0.20, 'dot': 0.15, 'impact': 0.15}

bat_eligible['PBS'] = (
    W_BAT['sr']       * bat_eligible['z_sr'] +
    W_BAT['avg']      * bat_eligible['z_avg'] +
    W_BAT['boundary'] * bat_eligible['z_boundary'] +
    W_BAT['dot']      * bat_eligible['z_dot'] +
    W_BAT['impact']   * bat_eligible['z_impact']
)

print(f"  PBS weights: SR={W_BAT['sr']}, Avg={W_BAT['avg']}, Boundary={W_BAT['boundary']}, "
      f"Dot={W_BAT['dot']}, Impact={W_BAT['impact']}")
print(f"  PBS stats: mean={bat_eligible['PBS'].mean():.4f}, std={bat_eligible['PBS'].std():.4f}")

# BOWLING: Pressure Bowling Score (PBoS)
bowl_eligible['z_econ']    = zscore(bowl_eligible['econ_uplift'])
bowl_eligible['z_bowl_sr'] = zscore(bowl_eligible['bowl_sr_uplift'])
bowl_eligible['z_bowl_dot']= zscore(bowl_eligible['bowl_dot_uplift'])
bowl_eligible['z_bowl_bdry'] = zscore(bowl_eligible['bowl_bdry_uplift'])
bowl_eligible['z_bowl_ext'] = zscore(bowl_eligible['bowl_extras_uplift'])

W_BOWL = {'econ': 0.30, 'sr': 0.25, 'dot': 0.20, 'bdry': 0.15, 'ext': 0.10}

bowl_eligible['PBoS'] = (
    W_BOWL['econ'] * bowl_eligible['z_econ'] +
    W_BOWL['sr']   * bowl_eligible['z_bowl_sr'] +
    W_BOWL['dot']  * bowl_eligible['z_bowl_dot'] +
    W_BOWL['bdry'] * bowl_eligible['z_bowl_bdry'] +
    W_BOWL['ext']  * bowl_eligible['z_bowl_ext']
)

print(f"  PBoS weights: Econ={W_BOWL['econ']}, SR={W_BOWL['sr']}, Dot={W_BOWL['dot']}, "
      f"Bdry={W_BOWL['bdry']}, Extras={W_BOWL['ext']}")
print(f"  PBoS stats: mean={bowl_eligible['PBoS'].mean():.4f}, std={bowl_eligible['PBoS'].std():.4f}")

# ============================================================
# STEP 9: Consistency Multiplier
# ============================================================
print("\n--- STEP 9: Computing consistency multiplier ---")

# Per-match batting SR under pressure
hp_per_match_bat = bbb[bbb['pressure_category'] == 'High'].groupby(
    ['striker_id', 'match_id']
).apply(lambda df: pd.Series({
    'match_sr': df['runs'].sum() / len(df) * 100 if len(df) > 0 else 0,
    'match_balls': len(df)
})).reset_index()

# Only consider matches with >= 5 pressure balls
hp_per_match_bat = hp_per_match_bat[hp_per_match_bat['match_balls'] >= 5]

# Coefficient of variation of per-match SR (lower = more consistent)
bat_consistency = hp_per_match_bat.groupby('striker_id').agg(
    sr_std=('match_sr', 'std'),
    sr_mean=('match_sr', 'mean'),
    pressure_matches=('match_id', 'nunique')
).reset_index()
bat_consistency.columns = ['player_id', 'bat_sr_std', 'bat_sr_mean', 'bat_pressure_matches']

# CV = std/mean, lower is better; convert to multiplier
bat_consistency['bat_cv'] = bat_consistency['bat_sr_std'] / bat_consistency['bat_sr_mean'].clip(lower=1)
bat_consistency['bat_consistency'] = 1 / (1 + bat_consistency['bat_cv'])
# Scale to 0.7-1.0 range
bat_consistency['bat_multiplier'] = 0.7 + 0.3 * bat_consistency['bat_consistency']

bat_eligible = bat_eligible.merge(
    bat_consistency[['player_id', 'bat_multiplier', 'bat_pressure_matches', 'bat_cv']],
    on='player_id', how='left'
)
bat_eligible['bat_multiplier'] = bat_eligible['bat_multiplier'].fillna(0.7)

# Per-match bowling economy under pressure
hp_per_match_bowl = bbb[bbb['pressure_category'] == 'High'].groupby(
    ['bowler_id', 'match_id']
).apply(lambda df: pd.Series({
    'match_econ': df['total_runs'].sum() / (df['is_legal'].sum() / 6) if df['is_legal'].sum() > 0 else 0,
    'match_balls': len(df)
})).reset_index()

hp_per_match_bowl = hp_per_match_bowl[hp_per_match_bowl['match_balls'] >= 5]

bowl_consistency = hp_per_match_bowl.groupby('bowler_id').agg(
    econ_std=('match_econ', 'std'),
    econ_mean=('match_econ', 'mean'),
    pressure_matches=('match_id', 'nunique')
).reset_index()
bowl_consistency.columns = ['player_id', 'bowl_econ_std', 'bowl_econ_mean', 'bowl_pressure_matches']

bowl_consistency['bowl_cv'] = bowl_consistency['bowl_econ_std'] / bowl_consistency['bowl_econ_mean'].clip(lower=1)
bowl_consistency['bowl_consistency'] = 1 / (1 + bowl_consistency['bowl_cv'])
bowl_consistency['bowl_multiplier'] = 0.7 + 0.3 * bowl_consistency['bowl_consistency']

bowl_eligible = bowl_eligible.merge(
    bowl_consistency[['player_id', 'bowl_multiplier', 'bowl_pressure_matches', 'bowl_cv']],
    on='player_id', how='left'
)
bowl_eligible['bowl_multiplier'] = bowl_eligible['bowl_multiplier'].fillna(0.7)

# Apply consistency multiplier
bat_eligible['PBS_final'] = bat_eligible['PBS'] * bat_eligible['bat_multiplier']
bowl_eligible['PBoS_final'] = bowl_eligible['PBoS'] * bowl_eligible['bowl_multiplier']

print(f"  Batting consistency multiplier: mean={bat_eligible['bat_multiplier'].mean():.3f}")
print(f"  Bowling consistency multiplier: mean={bowl_eligible['bowl_multiplier'].mean():.3f}")

# ============================================================
# STEP 10: Final Rankings
# ============================================================
print("\n--- STEP 10: Final Rankings ---")

# Sort and rank
bat_eligible = bat_eligible.sort_values('PBS_final', ascending=False).reset_index(drop=True)
bat_eligible['rank'] = range(1, len(bat_eligible) + 1)

bowl_eligible = bowl_eligible.sort_values('PBoS_final', ascending=False).reset_index(drop=True)
bowl_eligible['rank'] = range(1, len(bowl_eligible) + 1)

# ============================================================
# Display Top 10 Batters
# ============================================================
print("\n" + "=" * 100)
print("TOP 10 BATTERS UNDER PRESSURE")
print("=" * 100)
print(f"{'Rank':<5} {'Player':<25} {'Overall SR':>10} {'Press SR':>10} {'SR Uplift':>10} "
      f"{'Press Avg':>10} {'Press Balls':>11} {'Matches':>8} {'PBS':>8}")
print("-" * 100)

top10_bat = bat_eligible.head(10)
for _, row in top10_bat.iterrows():
    print(f"{int(row['rank']):<5} {str(row['player_name']):<25} "
          f"{row['all_bat_sr']:>10.1f} {row['hp_bat_sr']:>10.1f} "
          f"{row['sr_uplift']*100:>9.1f}% "
          f"{row['hp_bat_avg']:>10.1f} {int(row['hp_bat_balls']):>11} "
          f"{int(row['matches_batted']):>8} {row['PBS_final']:>8.4f}")

# ============================================================
# Display Top 10 Bowlers
# ============================================================
print("\n" + "=" * 100)
print("TOP 10 BOWLERS UNDER PRESSURE")
print("=" * 100)
print(f"{'Rank':<5} {'Player':<25} {'Overall Econ':>12} {'Press Econ':>11} {'Econ Uplift':>12} "
      f"{'Press Wkts':>10} {'Press Balls':>11} {'Matches':>8} {'PBoS':>8}")
print("-" * 100)

top10_bowl = bowl_eligible.head(10)
for _, row in top10_bowl.iterrows():
    print(f"{int(row['rank']):<5} {str(row['player_name']):<25} "
          f"{row['all_bowl_econ']:>12.2f} {row['hp_bowl_econ']:>11.2f} "
          f"{row['econ_uplift']*100:>11.1f}% "
          f"{int(row['hp_bowl_wickets']):>10} {int(row['hp_bowl_balls']):>11} "
          f"{int(row['matches_bowled']):>8} {row['PBoS_final']:>8.4f}")

# ============================================================
# STEP 11: Extended Top 20 for context
# ============================================================
print("\n\n--- Extended Top 20 Batters ---")
top20_bat = bat_eligible.head(20)
for _, row in top20_bat.iterrows():
    print(f"  {int(row['rank']):>2}. {str(row['player_name']):<25} "
          f"SR: {row['all_bat_sr']:.1f}->{row['hp_bat_sr']:.1f} "
          f"Avg: {row['all_bat_avg']:.1f}->{row['hp_bat_avg']:.1f} "
          f"PBS={row['PBS_final']:.4f} "
          f"(balls={int(row['hp_bat_balls'])}, matches={int(row['matches_batted'])})")

print("\n--- Extended Top 20 Bowlers ---")
top20_bowl = bowl_eligible.head(20)
for _, row in top20_bowl.iterrows():
    print(f"  {int(row['rank']):>2}. {str(row['player_name']):<25} "
          f"Econ: {row['all_bowl_econ']:.2f}->{row['hp_bowl_econ']:.2f} "
          f"Wkts: {int(row['hp_bowl_wickets'])} "
          f"PBoS={row['PBoS_final']:.4f} "
          f"(balls={int(row['hp_bowl_balls'])}, matches={int(row['matches_bowled'])})")

# ============================================================
# STEP 12: Save All Outputs
# ============================================================
print("\n--- STEP 12: Saving outputs ---")

# Full eligible batters
bat_output = os.path.join(OUTPUT_DIR, "batters_ranked.csv")
bat_eligible.to_csv(bat_output, index=False)
print(f"  Saved: {bat_output} ({len(bat_eligible)} players)")

# Full eligible bowlers
bowl_output = os.path.join(OUTPUT_DIR, "bowlers_ranked.csv")
bowl_eligible.to_csv(bowl_output, index=False)
print(f"  Saved: {bowl_output} ({len(bowl_eligible)} players)")

# Top 10 summary
top10_bat_summary = top10_bat[['rank', 'player_name', 'player_id', 
    'all_bat_sr', 'hp_bat_sr', 'sr_uplift',
    'all_bat_avg', 'hp_bat_avg', 'avg_uplift',
    'all_bat_boundary_pct', 'hp_bat_boundary_pct', 'boundary_uplift',
    'all_bat_dot_pct', 'hp_bat_dot_pct', 'dot_uplift',
    'hp_bat_balls', 'matches_batted', 'seasons_batted',
    'bat_multiplier', 'PBS', 'PBS_final',
    'typical_batting_order'
]].copy()
top10_bat_summary.to_csv(os.path.join(OUTPUT_DIR, "top10_batters.csv"), index=False)

top10_bowl_summary = top10_bowl[['rank', 'player_name', 'player_id',
    'all_bowl_econ', 'hp_bowl_econ', 'econ_uplift',
    'all_bowl_sr', 'hp_bowl_sr', 'bowl_sr_uplift',
    'all_bowl_dot_pct', 'hp_bowl_dot_pct', 'bowl_dot_uplift',
    'all_bowl_boundary_pct', 'hp_bowl_boundary_pct', 'bowl_bdry_uplift',
    'hp_bowl_balls', 'hp_bowl_wickets', 'matches_bowled', 'seasons_bowled',
    'bowl_multiplier', 'PBoS', 'PBoS_final'
]].copy()
top10_bowl_summary.to_csv(os.path.join(OUTPUT_DIR, "top10_bowlers.csv"), index=False)

print(f"  Saved: top10_batters.csv")
print(f"  Saved: top10_bowlers.csv")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("PHASE 3 COMPLETE")
print("=" * 70)
print(f"""
  Eligible batters:  {len(bat_eligible)}
  Eligible bowlers:  {len(bowl_eligible)}
  
  Top 10 Batters:  {', '.join(top10_bat['player_name'].tolist())}
  
  Top 10 Bowlers:  {', '.join(top10_bowl['player_name'].tolist())}
  
  Outputs:
    - batters_ranked.csv  (all eligible batters with scores)
    - bowlers_ranked.csv  (all eligible bowlers with scores)
    - top10_batters.csv   (Top 10 summary)
    - top10_bowlers.csv   (Top 10 summary)
""")
