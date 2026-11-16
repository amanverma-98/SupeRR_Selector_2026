import pandas as pd
import numpy as np
import os

OUTPUT_DIR = r"D:\movies\6af458274c1e8_data_pack\output"
DATA_DIR = r"D:\movies\6af458274c1e8_data_pack\Data Pack"

mapping = pd.read_csv(os.path.join(DATA_DIR, "competition_team_player_mapping.csv"))
comps = pd.read_csv(os.path.join(DATA_DIR, "competitions.csv"))
teams = pd.read_csv(os.path.join(DATA_DIR, "teams.csv"))
bbb = pd.read_csv(os.path.join(OUTPUT_DIR, "bbb_with_pressure.csv"))
player_names = pd.read_csv(os.path.join(OUTPUT_DIR, "player_names.csv"))

# IPL 2026 comp
ipl_2026_cid = comps[comps['comp_name'] == 'IPL 2026']['comp_id'].iloc[0]
ipl_2026_players = set(mapping[mapping['comp_id'] == ipl_2026_cid]['player_id'].unique())

# Pakistan players
pak_team_ids = set(teams[teams['team_name'].str.contains('Pakistan', case=False, na=False)]['team_id'].unique())
pak_players = set(mapping[mapping['team_id'].isin(pak_team_ids)]['player_id'].unique())

# Emerging tournament players
emerging_comps = comps[comps['comp_name'].str.contains('Emerging|Rising', case=False, na=False)]
emerging_players = set(mapping[mapping['comp_id'].isin(emerging_comps['comp_id'])]['player_id'].unique())

# Past IPL players (released / uncontracted in 2026)
all_ipl_comps = set(comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]['comp_id'])
all_ipl_players = set(mapping[mapping['comp_id'].isin(all_ipl_comps)]['player_id'].unique())
released_ipl_players = (all_ipl_players - ipl_2026_players)

# Target pool: NOT in IPL 2026 franchise, NOT Pakistan
available_targets = set(mapping['player_id'].unique()) - ipl_2026_players - pak_players

# Re-parse booleans
for col in ['is_four', 'is_six', 'is_wicket', 'is_dot', 'is_legal']:
    bbb[col] = bbb[col].astype(str).str.strip().str.lower().isin(['true', '1'])

# 1. BATTING METRICS
def compute_batting(df):
    balls = len(df)
    if balls == 0:
        return pd.Series({'balls': 0, 'runs': 0, 'sr': np.nan, 'avg': np.nan, 'bdry': np.nan, 'dot': np.nan, 'imp': np.nan})
    runs = df['runs'].sum()
    fours = df['is_four'].sum()
    sixes = df['is_six'].sum()
    dismissals = df['is_wicket'].sum()
    dots = ((df['runs'] == 0) & (df['extras_type'] == 'None')).sum()
    return pd.Series({
        'balls': balls,
        'runs': runs,
        'sr': (runs / balls * 100) if balls > 0 else 0,
        'avg': (runs / dismissals) if dismissals > 0 else runs * 1.5,
        'bdry': ((fours + sixes) / balls * 100) if balls > 0 else 0,
        'dot': (dots / balls * 100) if balls > 0 else 0,
        'imp': ((runs + 10 * sixes + 5 * fours) / balls) if balls > 0 else 0
    })

bat_all = bbb[bbb['striker_id'].isin(available_targets)].groupby('striker_id').apply(compute_batting).reset_index()
bat_all.columns = ['player_id'] + ['all_' + c for c in bat_all.columns[1:]]

hp_bbb = bbb[(bbb['pressure_category'] == 'High') & (bbb['striker_id'].isin(available_targets))]
bat_hp = hp_bbb.groupby('striker_id').apply(compute_batting).reset_index()
bat_hp.columns = ['player_id'] + ['hp_' + c for c in bat_hp.columns[1:]]

batters = bat_all.merge(bat_hp, on='player_id', how='left')

bat_matches = bbb.groupby('striker_id')['match_id'].nunique().reset_index()
bat_matches.columns = ['player_id', 'matches']
bat_order = bbb.groupby('striker_id')['batting_order'].agg(lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 0).reset_index()
bat_order.columns = ['player_id', 'order']

batters = batters.merge(bat_matches, on='player_id', how='left')
batters = batters.merge(bat_order, on='player_id', how='left')
batters = batters.merge(player_names, on='player_id', how='left')

# Criteria for auction target batters:
# >= 100 balls total, >= 25 pressure balls, order <= 7, matches >= 10
bat_elig = batters[(batters['all_balls'] >= 100) & (batters['hp_balls'] >= 25) & (batters['order'] <= 7) & (batters['matches'] >= 10)].copy()

bat_elig['sr_uplift'] = (bat_elig['hp_sr'] - bat_elig['all_sr']) / bat_elig['all_sr']
bat_elig['avg_uplift'] = ((bat_elig['hp_avg'] - bat_elig['all_avg']) / bat_elig['all_avg']).clip(-1, 3)
bat_elig['bdry_uplift'] = (bat_elig['hp_bdry'] - bat_elig['all_bdry']) / bat_elig['all_bdry'].clip(lower=1)
bat_elig['dot_uplift'] = (bat_elig['all_dot'] - bat_elig['hp_dot']) / bat_elig['all_dot'].clip(lower=1)
bat_elig['imp_uplift'] = (bat_elig['hp_imp'] - bat_elig['all_imp']) / bat_elig['all_imp'].clip(lower=0.1)

K_BAT = 40
for col in ['sr_uplift', 'avg_uplift', 'bdry_uplift', 'dot_uplift', 'imp_uplift']:
    m = bat_elig[col].mean()
    f = bat_elig['hp_balls'] / (bat_elig['hp_balls'] + K_BAT)
    bat_elig[col] = m + f * (bat_elig[col] - m)

def zscore(s):
    std = s.std()
    return (s - s.mean()) / std if std > 0 else s * 0

bat_elig['PBS'] = (
    0.30 * zscore(bat_elig['sr_uplift']) +
    0.20 * zscore(bat_elig['avg_uplift']) +
    0.20 * zscore(bat_elig['bdry_uplift']) +
    0.15 * zscore(bat_elig['dot_uplift']) +
    0.15 * zscore(bat_elig['imp_uplift'])
)

# Consistency multiplier
hp_per_match_bat = bbb[(bbb['pressure_category'] == 'High') & (bbb['striker_id'].isin(bat_elig['player_id']))].groupby(
    ['striker_id', 'match_id']
).apply(lambda df: pd.Series({
    'match_sr': df['runs'].sum() / len(df) * 100 if len(df) > 0 else 0,
    'match_balls': len(df)
})).reset_index()
hp_per_match_bat = hp_per_match_bat[hp_per_match_bat['match_balls'] >= 4]

bat_consistency = hp_per_match_bat.groupby('striker_id').agg(
    sr_std=('match_sr', 'std'),
    sr_mean=('match_sr', 'mean')
).reset_index()
bat_consistency.columns = ['player_id', 'bat_sr_std', 'bat_sr_mean']
bat_consistency['bat_cv'] = bat_consistency['bat_sr_std'] / bat_consistency['bat_sr_mean'].clip(lower=1)
bat_consistency['bat_multiplier'] = 0.75 + 0.25 / (1 + bat_consistency['bat_cv'].fillna(1))

bat_elig = bat_elig.merge(bat_consistency[['player_id', 'bat_multiplier']], on='player_id', how='left')
bat_elig['bat_multiplier'] = bat_elig['bat_multiplier'].fillna(0.75)
bat_elig['PBS_final'] = bat_elig['PBS'] * bat_elig['bat_multiplier']

# Tag type
def get_talent_tag(pid):
    if pid in emerging_players:
        return "Raw Talent (Emerging)"
    elif pid in released_ipl_players:
        return "Uncontracted / Free Agent"
    else:
        return "International Auction Target"

bat_elig['talent_category'] = bat_elig['player_id'].apply(get_talent_tag)
bat_elig = bat_elig.sort_values('PBS_final', ascending=False).reset_index(drop=True)
bat_elig['rank'] = range(1, len(bat_elig) + 1)

# 2. BOWLING METRICS
def compute_bowling(df):
    balls = len(df)
    if balls == 0:
        return pd.Series({'balls': 0, 'runs': 0, 'econ': np.nan, 'sr': np.nan, 'dot': np.nan, 'bdry': np.nan, 'ext': np.nan, 'wkts': 0})
    runs_conceded = df['total_runs'].sum()
    legal_balls = df['is_legal'].sum()
    overs = legal_balls / 6
    bowler_dismissals = ['Bowled', 'Caught', 'LBW', 'Stump', 'Hit Wicket']
    wickets = df[df['dismissal_type'].isin(bowler_dismissals)]['is_wicket'].sum()
    dots = ((df['runs'] == 0) & (df['extras_type'] == 'None')).sum()
    boundaries_conceded = (df['is_four'].sum() + df['is_six'].sum())
    extras = df[df['extras_type'].isin(['wide', 'Overstep'])].shape[0]
    return pd.Series({
        'balls': balls,
        'runs': runs_conceded,
        'econ': (runs_conceded / overs) if overs > 0 else 0,
        'sr': (legal_balls / wickets) if wickets > 0 else legal_balls * 1.5,
        'dot': (dots / balls * 100) if balls > 0 else 0,
        'bdry': (boundaries_conceded / balls * 100) if balls > 0 else 0,
        'ext': (extras / balls * 100) if balls > 0 else 0,
        'wkts': wickets
    })

bowl_all = bbb[bbb['bowler_id'].isin(available_targets)].groupby('bowler_id').apply(compute_bowling).reset_index()
bowl_all.columns = ['player_id'] + ['all_' + c for c in bowl_all.columns[1:]]

hp_bbb_bowl = bbb[(bbb['pressure_category'] == 'High') & (bbb['bowler_id'].isin(available_targets))]
bowl_hp = hp_bbb_bowl.groupby('bowler_id').apply(compute_bowling).reset_index()
bowl_hp.columns = ['player_id'] + ['hp_' + c for c in bowl_hp.columns[1:]]

bowlers = bowl_all.merge(bowl_hp, on='player_id', how='left')

bowl_matches = bbb.groupby('bowler_id')['match_id'].nunique().reset_index()
bowl_matches.columns = ['player_id', 'matches']

bowlers = bowlers.merge(bowl_matches, on='player_id', how='left')
bowlers = bowlers.merge(player_names, on='player_id', how='left')

# Criteria for auction target bowlers:
# >= 120 balls total, >= 24 pressure balls, matches >= 10
bowl_elig = bowlers[(bowlers['all_balls'] >= 120) & (bowlers['hp_balls'] >= 24) & (bowlers['matches'] >= 10)].copy()

bowl_elig['econ_uplift'] = (bowl_elig['all_econ'] - bowl_elig['hp_econ']) / bowl_elig['all_econ'].clip(lower=1)
bowl_elig['sr_uplift'] = ((bowl_elig['all_sr'] - bowl_elig['hp_sr']) / bowl_elig['all_sr'].clip(lower=1)).clip(-1, 2)
bowl_elig['dot_uplift'] = (bowl_elig['hp_dot'] - bowl_elig['all_dot']) / bowl_elig['all_dot'].clip(lower=1)
bowl_elig['bdry_uplift'] = (bowl_elig['all_bdry'] - bowl_elig['hp_bdry']) / bowl_elig['all_bdry'].clip(lower=1)
bowl_elig['ext_uplift'] = ((bowl_elig['all_ext'] - bowl_elig['hp_ext']) / bowl_elig['all_ext'].clip(lower=0.1)).clip(-2, 2)

K_BOWL = 50
for col in ['econ_uplift', 'sr_uplift', 'dot_uplift', 'bdry_uplift', 'ext_uplift']:
    m = bowl_elig[col].mean()
    f = bowl_elig['hp_balls'] / (bowl_elig['hp_balls'] + K_BOWL)
    bowl_elig[col] = m + f * (bowl_elig[col] - m)

bowl_elig['PBoS'] = (
    0.30 * zscore(bowl_elig['econ_uplift']) +
    0.25 * zscore(bowl_elig['sr_uplift']) +
    0.20 * zscore(bowl_elig['dot_uplift']) +
    0.15 * zscore(bowl_elig['bdry_uplift']) +
    0.10 * zscore(bowl_elig['ext_uplift'])
)

hp_per_match_bowl = bbb[(bbb['pressure_category'] == 'High') & (bbb['bowler_id'].isin(bowl_elig['player_id']))].groupby(
    ['bowler_id', 'match_id']
).apply(lambda df: pd.Series({
    'match_econ': df['total_runs'].sum() / (df['is_legal'].sum() / 6) if df['is_legal'].sum() > 0 else 0,
    'match_balls': len(df)
})).reset_index()
hp_per_match_bowl = hp_per_match_bowl[hp_per_match_bowl['match_balls'] >= 4]

bowl_consistency = hp_per_match_bowl.groupby('bowler_id').agg(
    econ_std=('match_econ', 'std'),
    econ_mean=('match_econ', 'mean')
).reset_index()
bowl_consistency.columns = ['player_id', 'bowl_econ_std', 'bowl_econ_mean']
bowl_consistency['bowl_cv'] = bowl_consistency['bowl_econ_std'] / bowl_consistency['bowl_econ_mean'].clip(lower=1)
bowl_consistency['bowl_multiplier'] = 0.75 + 0.25 / (1 + bowl_consistency['bowl_cv'].fillna(1))

bowl_elig = bowl_elig.merge(bowl_consistency[['player_id', 'bowl_multiplier']], on='player_id', how='left')
bowl_elig['bowl_multiplier'] = bowl_elig['bowl_multiplier'].fillna(0.75)
bowl_elig['PBoS_final'] = bowl_elig['PBoS'] * bowl_elig['bowl_multiplier']

bowl_elig['talent_category'] = bowl_elig['player_id'].apply(get_talent_tag)
bowl_elig = bowl_elig.sort_values('PBoS_final', ascending=False).reset_index(drop=True)
bowl_elig['rank'] = range(1, len(bowl_elig) + 1)

print("\n=== TOP 10 AUCTION TARGET BATTERS (FOR RR AUCTION 2027) ===")
top10_bat = bat_elig.head(10)
for _, r in top10_bat.iterrows():
    print(f"Rank {int(r['rank']):>2}: {r['player_name']:<24} | {r['talent_category']:<26} | SR: {r['all_sr']:.1f}->{r['hp_sr']:.1f} (+{r['sr_uplift']*100:.1f}%) | Avg: {r['all_avg']:.1f}->{r['hp_avg']:.1f} | balls={int(r['hp_balls']):>3} | PBS: {r['PBS_final']:.4f}")

print("\n=== TOP 10 AUCTION TARGET BOWLERS (FOR RR AUCTION 2027) ===")
top10_bowl = bowl_elig.head(10)
for _, r in top10_bowl.iterrows():
    print(f"Rank {int(r['rank']):>2}: {r['player_name']:<24} | {r['talent_category']:<26} | Econ: {r['all_econ']:.2f}->{r['hp_econ']:.2f} (+{r['econ_uplift']*100:.1f}%) | Wkts: {int(r['hp_wkts']):>2} | balls={int(r['hp_balls']):>3} | PBoS: {r['PBoS_final']:.4f}")

# Save results
bat_elig.to_csv(os.path.join(OUTPUT_DIR, "auction_targets_batters_ranked.csv"), index=False)
bowl_elig.to_csv(os.path.join(OUTPUT_DIR, "auction_targets_bowlers_ranked.csv"), index=False)
top10_bat.to_csv(os.path.join(OUTPUT_DIR, "top10_auction_batters.csv"), index=False)
top10_bowl.to_csv(os.path.join(OUTPUT_DIR, "top10_auction_bowlers.csv"), index=False)
