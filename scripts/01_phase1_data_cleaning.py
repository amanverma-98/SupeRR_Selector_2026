"""
Phase 1: Data Loading, Cleaning & Joining
==========================================
SupeRR Selector Season 2 - Round 1
Loads all CSVs, cleans types, joins tables, filters, and saves a merged dataset.
"""

import pandas as pd
import numpy as np
import os
import re
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = r"D:\movies\6af458274c1e8_data_pack\Data Pack"
OUTPUT_DIR = r"D:\movies\6af458274c1e8_data_pack\output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 70)
print("PHASE 1: DATA LOADING, CLEANING & JOINING")
print("=" * 70)

# ============================================================
# STEP 1: Load all CSVs
# ============================================================
print("\n--- STEP 1: Loading CSVs ---")

bbb = pd.read_csv(os.path.join(DATA_DIR, "ball_by_ball.csv"))
matches = pd.read_csv(os.path.join(DATA_DIR, "matches.csv"))
competitions = pd.read_csv(os.path.join(DATA_DIR, "competitions.csv"))
teams = pd.read_csv(os.path.join(DATA_DIR, "teams.csv"))
playing_xi = pd.read_csv(os.path.join(DATA_DIR, "playing_eleven.csv"))
player_map = pd.read_csv(os.path.join(DATA_DIR, "competition_team_player_mapping.csv"))

print(f"  ball_by_ball:    {bbb.shape[0]:>8,} rows x {bbb.shape[1]} cols")
print(f"  matches:         {matches.shape[0]:>8,} rows x {matches.shape[1]} cols")
print(f"  competitions:    {competitions.shape[0]:>8,} rows x {competitions.shape[1]} cols")
print(f"  teams:           {teams.shape[0]:>8,} rows x {teams.shape[1]} cols")
print(f"  playing_eleven:  {playing_xi.shape[0]:>8,} rows x {playing_xi.shape[1]} cols")
print(f"  player_mapping:  {player_map.shape[0]:>8,} rows x {player_map.shape[1]} cols")

# ============================================================
# STEP 2: Clean & Parse Data Types
# ============================================================
print("\n--- STEP 2: Cleaning & Parsing Data Types ---")

# --- ball_by_ball ---
# Convert boolean strings to actual booleans
for col in ['is_four', 'is_six', 'is_wicket']:
    bbb[col] = bbb[col].astype(str).str.lower().map({'true': True, 'false': False}).fillna(False)

# Numeric columns
bbb['match_id'] = bbb['match_id'].astype(int)
bbb['innings'] = bbb['innings'].astype(int)
bbb['overid'] = bbb['overid'].astype(int)
bbb['over_ball_num'] = bbb['over_ball_num'].astype(int)
bbb['innings_ball_num'] = bbb['innings_ball_num'].astype(int)
bbb['batting_team_id'] = bbb['batting_team_id'].astype(int)
bbb['bowling_team_id'] = bbb['bowling_team_id'].astype(int)
bbb['striker_id'] = bbb['striker_id'].astype(int)
bbb['non_striker_id'] = bbb['non_striker_id'].astype(int)
bbb['bowler_id'] = bbb['bowler_id'].astype(int)
bbb['runs'] = bbb['runs'].astype(int)
bbb['extras1_runs'] = bbb['extras1_runs'].astype(int)
bbb['extras_2_runs'] = bbb['extras_2_runs'].astype(int)
bbb['batting_order'] = pd.to_numeric(bbb['batting_order'], errors='coerce').fillna(0).astype(int)

# Bowl speed: convert to float, treat 0 and -1 as NaN
bbb['bowl_speed'] = pd.to_numeric(bbb['bowl_speed'], errors='coerce')
bbb.loc[bbb['bowl_speed'] <= 0, 'bowl_speed'] = np.nan

# Clean string columns
bbb['extras_type'] = bbb['extras_type'].fillna('None').astype(str)
bbb['dismissal_type'] = bbb['dismissal_type'].fillna('').astype(str)
bbb['dismissed_player_id'] = pd.to_numeric(bbb['dismissed_player_id'], errors='coerce').fillna(0).astype(int)

# Standardize dismissal types
bbb['dismissal_type'] = bbb['dismissal_type'].replace({
    'Obstracting the field': 'Obstructing the field'
})

print(f"  Boolean columns converted: is_four, is_six, is_wicket")
print(f"  Numeric columns parsed: runs, extras, bowl_speed, IDs")
print(f"  Dismissal types standardized")

# --- matches ---
matches['match_id'] = matches['match_id'].astype(int)
matches['comp_id'] = matches['comp_id'].astype(int)
matches['match_date'] = pd.to_datetime(matches['match_date'], errors='coerce')

# Parse revised target and revised overs
matches['revised_target'] = pd.to_numeric(matches['revised_target'], errors='coerce')
matches['first_inn_revised_overs'] = pd.to_numeric(matches['first_inn_revised_overs'], errors='coerce')
matches['second_inn_revised_overs'] = pd.to_numeric(matches['second_inn_revised_overs'], errors='coerce')
matches['knock_out'] = pd.to_numeric(matches['knock_out'], errors='coerce').fillna(0).astype(int)
matches['win_team_id'] = pd.to_numeric(matches['win_team_id'], errors='coerce').fillna(0).astype(int)
matches['toss_win_team_id'] = pd.to_numeric(matches['toss_win_team_id'], errors='coerce').fillna(0).astype(int)
matches['man_of_the_match'] = pd.to_numeric(matches['man_of_the_match'], errors='coerce').fillna(0).astype(int)

# Parse win margin from result string
def parse_win_margin(result):
    """Extract win margin (runs or wickets) from result string."""
    if pd.isna(result) or result == '':
        return np.nan, ''
    result_lower = result.lower()
    # Check for tie/super over/no result
    if 'tie' in result_lower or 'super over' in result_lower:
        return 0, 'tie'
    if 'no result' in result_lower or 'abandon' in result_lower or 'draw' in result_lower:
        return np.nan, 'no_result'
    # Extract margin
    m = re.search(r'by\s+(\d+)\s+(run|wicket|wkt)', result_lower)
    if m:
        margin = int(m.group(1))
        unit = 'runs' if 'run' in m.group(2) else 'wickets'
        return margin, unit
    return np.nan, ''

matches[['win_margin', 'win_margin_type']] = matches['result'].apply(
    lambda x: pd.Series(parse_win_margin(x))
)

print(f"  Matches: dates parsed, DLS fields cleaned, win margins extracted")
print(f"  Win margin extracted for {matches['win_margin'].notna().sum()} / {len(matches)} matches")

# --- competitions ---
competitions['comp_id'] = competitions['comp_id'].astype(int)
print(f"  Competitions: {competitions['match_format'].value_counts().to_dict()}")

# --- player_map: Build player ID -> name lookup ---
# Take the most recent name for each player_id (in case of spelling variations)
player_names = player_map.sort_values('comp_id').drop_duplicates(
    subset='player_id', keep='last'
)[['player_id', 'player_name']].copy()
player_names['player_id'] = player_names['player_id'].astype(int)
print(f"  Unique players in mapping: {len(player_names)}")

# ============================================================
# STEP 3: Filter Super Overs
# ============================================================
print("\n--- STEP 3: Filtering Super Overs ---")

super_over_count = bbb[bbb['innings'].isin([3, 4])].shape[0]
bbb = bbb[bbb['innings'].isin([1, 2])].copy()
print(f"  Removed {super_over_count} super-over deliveries")
print(f"  Remaining deliveries: {len(bbb):,}")

# ============================================================
# STEP 4: Join ball_by_ball with matches
# ============================================================
print("\n--- STEP 4: Joining ball_by_ball with matches ---")

match_cols = [
    'match_id', 'comp_id', 'match_date', 'stage', 'venue_country',
    'home_team_id', 'away_team_id',
    'toss_win_team_id', 'toss_opted',
    'man_of_the_match', 'knock_out',
    'win_team_id', 'result',
    'first_inn_revised_overs', 'second_inn_revised_overs', 'revised_target',
    'win_margin', 'win_margin_type'
]

bbb = bbb.merge(matches[match_cols], on='match_id', how='left')
print(f"  Merged with matches: {len(bbb):,} rows")

# Join competition format & season
bbb = bbb.merge(competitions[['comp_id', 'match_format', 'season']], on='comp_id', how='left')
print(f"  Merged with competitions: {len(bbb):,} rows")

# Verify no rows lost
assert len(bbb) == 200961 or len(bbb) > 200000, f"Unexpected row count: {len(bbb)}"

# ============================================================
# STEP 5: Compute Total Runs Per Delivery
# ============================================================
print("\n--- STEP 5: Computing total runs per delivery ---")

# Total runs = bat runs + all extras
bbb['total_runs'] = bbb['runs'] + bbb['extras1_runs'] + bbb['extras_2_runs']

# Is it a dot ball? (0 runs off bat AND no extras)
bbb['is_dot'] = (bbb['runs'] == 0) & (bbb['extras_type'] == 'None')

# Is it a legal delivery? (not a wide or no-ball)
# Wides and no-balls (Overstep) don't count as legal deliveries
bbb['is_legal'] = ~bbb['extras_type'].isin(['wide', 'Overstep'])

print(f"  Total runs computed")
print(f"  Dot balls: {bbb['is_dot'].sum():,} ({bbb['is_dot'].mean()*100:.1f}%)")
print(f"  Legal deliveries: {bbb['is_legal'].sum():,} ({bbb['is_legal'].mean()*100:.1f}%)")

# ============================================================
# STEP 6: Compute Running Totals per (match, innings)
# ============================================================
print("\n--- STEP 6: Computing running totals ---")

# Sort by match, innings, and ball number
bbb = bbb.sort_values(['match_id', 'innings', 'innings_ball_num']).reset_index(drop=True)

# Group by match + innings
grp = bbb.groupby(['match_id', 'innings'])

# Cumulative runs scored so far (BEFORE this delivery — shift by 1)
bbb['cumulative_runs'] = grp['total_runs'].cumsum()
# cumulative_runs is AFTER this ball; for pre-ball state, shift:
bbb['runs_before_ball'] = bbb['cumulative_runs'] - bbb['total_runs']

# Cumulative wickets fallen (BEFORE this delivery)
bbb['cumulative_wickets_after'] = grp['is_wicket'].cumsum().astype(int)
bbb['wickets_before_ball'] = bbb['cumulative_wickets_after'] - bbb['is_wicket'].astype(int)

# Balls bowled so far (within the group, 1-indexed)
bbb['balls_so_far'] = grp.cumcount() + 1

# Legal balls so far (for computing run rates more accurately)
bbb['legal_balls_so_far'] = grp['is_legal'].cumsum().astype(int)

# Current run rate (using legal balls)
bbb['current_rr'] = np.where(
    bbb['legal_balls_so_far'] > 0,
    bbb['cumulative_runs'] / (bbb['legal_balls_so_far'] / 6),
    0
)

print(f"  Running totals computed: cumulative_runs, wickets, balls, current_rr")

# ============================================================
# STEP 7: Compute 1st Innings Totals & Chase Targets
# ============================================================
print("\n--- STEP 7: Computing chase targets ---")

# First innings total per match
inn1_totals = bbb[bbb['innings'] == 1].groupby('match_id').agg(
    first_inn_total=('total_runs', 'sum'),
    first_inn_balls=('is_legal', 'sum')  # legal deliveries
).reset_index()

bbb = bbb.merge(inn1_totals, on='match_id', how='left')

# Chase target: revised_target if DLS, else first_inn_total + 1
bbb['chase_target'] = np.where(
    bbb['revised_target'].notna() & (bbb['revised_target'] > 0),
    bbb['revised_target'],
    bbb['first_inn_total'] + 1
)

# Second innings chase fields
mask_2nd = bbb['innings'] == 2

bbb.loc[mask_2nd, 'runs_remaining'] = (
    bbb.loc[mask_2nd, 'chase_target'] - bbb.loc[mask_2nd, 'runs_before_ball']
)

# Total legal deliveries available in 2nd innings (usually 120, or revised)
bbb['max_legal_balls_2nd'] = np.where(
    bbb['second_inn_revised_overs'].notna() & (bbb['second_inn_revised_overs'] > 0),
    bbb['second_inn_revised_overs'] * 6,
    120
)

bbb.loc[mask_2nd, 'balls_remaining'] = (
    bbb.loc[mask_2nd, 'max_legal_balls_2nd'] - bbb.loc[mask_2nd, 'legal_balls_so_far'] + 1
)
# Ensure balls_remaining is at least 1 to avoid division by zero
bbb['balls_remaining'] = bbb['balls_remaining'].clip(lower=1)

bbb.loc[mask_2nd, 'required_rr'] = (
    bbb.loc[mask_2nd, 'runs_remaining'] / (bbb.loc[mask_2nd, 'balls_remaining'] / 6)
)

print(f"  1st innings totals computed for {len(inn1_totals)} matches")
print(f"  Chase targets set (DLS-aware)")
print(f"  RRR computed for {mask_2nd.sum():,} 2nd innings deliveries")

# Quick validation
print(f"\n  Validation - 2nd innings RRR stats:")
rrr_stats = bbb.loc[mask_2nd, 'required_rr'].describe()
print(f"    Mean RRR: {rrr_stats['mean']:.1f}")
print(f"    Median RRR: {rrr_stats['50%']:.1f}")
print(f"    Max RRR: {rrr_stats['max']:.1f}")

# ============================================================
# STEP 8: Add Match Phase Column
# ============================================================
print("\n--- STEP 8: Adding match phase ---")

def get_match_phase(overid):
    if overid <= 6:
        return 'Powerplay'
    elif overid <= 15:
        return 'Middle'
    else:
        return 'Death'

bbb['match_phase'] = bbb['overid'].apply(get_match_phase)

phase_dist = bbb['match_phase'].value_counts()
print(f"  Powerplay: {phase_dist.get('Powerplay', 0):,} deliveries")
print(f"  Middle:    {phase_dist.get('Middle', 0):,} deliveries")
print(f"  Death:     {phase_dist.get('Death', 0):,} deliveries")

# ============================================================
# STEP 9: Create Player Name Lookup (using ball_by_ball names + mapping)
# ============================================================
print("\n--- STEP 9: Building player name lookup ---")

# Get names from ball_by_ball (most recent appearance)
striker_names = bbb[['striker_id', 'striker_name']].drop_duplicates(
    subset='striker_id', keep='last'
).rename(columns={'striker_id': 'player_id', 'striker_name': 'player_name'})

bowler_names = bbb[['bowler_id', 'bowler_name']].drop_duplicates(
    subset='bowler_id', keep='last'
).rename(columns={'bowler_id': 'player_id', 'bowler_name': 'player_name'})

# Combine: prefer mapping file names, fall back to ball_by_ball names
all_names = pd.concat([striker_names, bowler_names, player_names], ignore_index=True)
all_names = all_names.drop_duplicates(subset='player_id', keep='last')

print(f"  Total unique players with names: {len(all_names)}")

# ============================================================
# STEP 10: Identify No-Result / Abandoned Matches
# ============================================================
print("\n--- STEP 10: Filtering no-result matches ---")

no_result_matches = matches[matches['win_margin_type'] == 'no_result']['match_id'].tolist()
pre_filter = len(bbb)
bbb = bbb[~bbb['match_id'].isin(no_result_matches)].copy()
post_filter = len(bbb)
print(f"  Removed {pre_filter - post_filter:,} deliveries from {len(no_result_matches)} no-result matches")
print(f"  Remaining deliveries: {post_filter:,}")

# ============================================================
# STEP 11: Validate Data Quality
# ============================================================
print("\n--- STEP 11: Data Quality Validation ---")

# Check for missing critical columns
critical_cols = ['match_id', 'innings', 'overid', 'striker_id', 'bowler_id', 'runs', 'stage']
for col in critical_cols:
    nulls = bbb[col].isna().sum()
    if nulls > 0:
        print(f"  WARNING: {col} has {nulls} null values")
    else:
        print(f"  OK: {col} - no nulls")

# Innings distribution
print(f"\n  Innings distribution:")
print(f"    {bbb['innings'].value_counts().to_dict()}")

# Match format distribution
print(f"\n  Match format distribution:")
print(f"    {bbb['match_format'].value_counts().to_dict()}")

# Season distribution
print(f"\n  Season distribution:")
season_counts = bbb.groupby('season')['match_id'].nunique().to_dict()
print(f"    {season_counts}")

# Stage distribution
print(f"\n  Match stage distribution:")
stage_counts = bbb.groupby('stage')['match_id'].nunique().to_dict()
print(f"    {stage_counts}")

# Unique counts
n_matches = bbb['match_id'].nunique()
n_batters = bbb['striker_id'].nunique()
n_bowlers = bbb['bowler_id'].nunique()
print(f"\n  Unique matches: {n_matches}")
print(f"  Unique batters: {n_batters}")
print(f"  Unique bowlers: {n_bowlers}")

# ============================================================
# STEP 12: Save Cleaned Dataset
# ============================================================
print("\n--- STEP 12: Saving cleaned dataset ---")

# Save main merged dataframe
output_path = os.path.join(OUTPUT_DIR, "bbb_cleaned.parquet")
bbb.to_parquet(output_path, index=False)
print(f"  Saved: {output_path} ({os.path.getsize(output_path) / 1024 / 1024:.1f} MB)")

# Save player names lookup
names_path = os.path.join(OUTPUT_DIR, "player_names.csv")
all_names.to_csv(names_path, index=False)
print(f"  Saved: {names_path}")

# Save matches (cleaned)
matches_path = os.path.join(OUTPUT_DIR, "matches_cleaned.csv")
matches.to_csv(matches_path, index=False)
print(f"  Saved: {matches_path}")

# ============================================================
# STEP 13: Summary Report
# ============================================================
print("\n" + "=" * 70)
print("PHASE 1 COMPLETE - SUMMARY")
print("=" * 70)
print(f"""
  Dataset:
    Total deliveries:        {len(bbb):>10,}
    1st innings deliveries:  {(bbb['innings']==1).sum():>10,}
    2nd innings deliveries:  {(bbb['innings']==2).sum():>10,}
    Matches:                 {n_matches:>10,}
    Unique batters:          {n_batters:>10,}
    Unique bowlers:          {n_bowlers:>10,}

  Computed Features:
    - total_runs (bat + extras per ball)
    - is_dot (dot ball flag)
    - is_legal (legal delivery flag)
    - cumulative_runs (running score)
    - wickets_before_ball (wickets fallen before this delivery)
    - current_rr (current run rate)
    - chase_target (DLS-aware)
    - runs_remaining (2nd innings)
    - balls_remaining (2nd innings)
    - required_rr (2nd innings required run rate)
    - match_phase (Powerplay/Middle/Death)
    - win_margin / win_margin_type (parsed from result)

  Joined Tables:
    - matches (stage, result, DLS, toss, venue)
    - competitions (format, season)

  Outputs:
    - {output_path}
    - {names_path}
    - {matches_path}

  Column count: {len(bbb.columns)}
  Columns: {list(bbb.columns)}
""")
