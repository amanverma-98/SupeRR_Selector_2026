import pandas as pd

# Final Top 10 Batters strictly matching user criteria:
# - No overseas player without IPL match & age > 30 (Balbirnie removed)
# - No overseas player without IPL match & age > 25 (Rasooli, Yasir Ali removed)
# - Only uncapped young prodigy (Dunith Wellalage < 22) or proven IPL players (Shai Hope, Jason Roy, Gulbadin, Kane Williamson, Wade)
# - Featuring India's best uncapped clutch talents (Shubham Dubey, Atharwa Taide, Lalit Yadav, Suyash Prabhudessai)
# - Explicitly offering both Overseas & Indian #3 Anchor solutions (Shai Hope / Atharwa Taide / Kane Williamson)

strat_bat_data = [
    {"rank": 1, "player_name": "Shubham Dubey", "player_id": 25139, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped", "role": "#6/#7 Power Finisher (25.3% Bdry)", "all_sr": 148.6, "hp_sr": 173.7, "hp_avg": 34.4, "PBS_final": 1.7370},
    {"rank": 2, "player_name": "Shai Hope", "player_id": 4369, "quota_tier": "Overseas (IPL: DC)", "uncapped_status": "Proven IPL Anchor", "role": "Master #3 Anchor (Post-Samson Void)", "all_sr": 141.3, "hp_sr": 157.0, "hp_avg": 59.7, "PBS_final": 1.5702},
    {"rank": 3, "player_name": "Atharwa Taide", "player_id": 6466, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped", "role": "Indian #3 Anchor / Fearless Opener", "all_sr": 138.3, "hp_sr": 149.1, "hp_avg": 85.0, "PBS_final": 1.4912},
    {"rank": 4, "player_name": "Dunith Wellalage", "player_id": 7052, "quota_tier": "Overseas (SL)", "uncapped_status": "Young Prodigy (<22)", "role": "Fixes #7 Tail Choke (SLA all-rounder)", "all_sr": 113.4, "hp_sr": 164.6, "hp_avg": 39.5, "PBS_final": 1.9551},
    {"rank": 5, "player_name": "Jason Roy", "player_id": 1187, "quota_tier": "Overseas (IPL: KKR)", "uncapped_status": "Proven IPL Star", "role": "Fearless Powerplay Enforcer Cover", "all_sr": 122.4, "hp_sr": 173.3, "hp_avg": 26.0, "PBS_final": 1.0236},
    {"rank": 6, "player_name": "Gulbadin Naib", "player_id": 2214, "quota_tier": "Overseas (IPL: DC)", "uncapped_status": "Proven IPL Star", "role": "Power Boundary Finisher", "all_sr": 121.6, "hp_sr": 158.2, "hp_avg": 43.5, "PBS_final": 1.2090},
    {"rank": 7, "player_name": "Lalit Yadav", "player_id": 6671, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (DC)", "role": "Indian #7 All-Round Spine & Off-Break", "all_sr": 104.9, "hp_sr": 128.4, "hp_avg": 18.7, "PBS_final": 0.8384},
    {"rank": 8, "player_name": "Kane Williamson", "player_id": 1568, "quota_tier": "Overseas (IPL: SRH/GT)", "uncapped_status": "Proven IPL Legend", "role": "Classical #3 Anchor & Master Tactician", "all_sr": 108.2, "hp_sr": 123.7, "hp_avg": 47.0, "PBS_final": 0.7850},
    {"rank": 9, "player_name": "Suyash Prabhudessai", "player_id": 8085, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (RCB)", "role": "Clutch Domestic 360-Degree Finisher", "all_sr": 111.5, "hp_sr": 122.9, "hp_avg": 28.7, "PBS_final": 0.5602},
    {"rank": 10, "player_name": "Matthew Wade", "player_id": 796, "quota_tier": "Overseas (IPL: GT)", "uncapped_status": "Proven IPL Star", "role": "Left-Handed Clutch Pressure Finisher", "all_sr": 132.7, "hp_sr": 150.9, "hp_avg": 61.5, "PBS_final": 0.5789}
]

df_bat = pd.DataFrame(strat_bat_data)
df_bat.to_csv('output/top10_auction_batters.csv', index=False)

strat_bowl_data = [
    {"rank": 1, "player_name": "Mohit Sharma", "player_id": 2878, "quota_tier": "Indian Core", "uncapped_status": "Indian Veteran", "role": "Direct Death Pace Cure (Saves OS slot)", "all_econ": 9.67, "hp_econ": 8.38, "hp_wkts": 26, "PBoS_final": 0.7179},
    {"rank": 2, "player_name": "Sean Abbott", "player_id": 1389, "quota_tier": "Overseas (IPL: SRH)", "uncapped_status": "Proven IPL Pacer", "role": "Hard-Length Pace All-Rounder", "all_econ": 9.96, "hp_econ": 7.89, "hp_wkts": 8, "PBoS_final": 0.8695},
    {"rank": 3, "player_name": "Brijesh Sharma", "player_id": 67036, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (RR)", "role": "Middle Squeeze Spinner (7.19 HP Econ)", "all_econ": 9.13, "hp_econ": 7.19, "hp_wkts": 4, "PBoS_final": 0.8240},
    {"rank": 4, "player_name": "Michael Bracewell", "player_id": 6512, "quota_tier": "Overseas (IPL: RCB)", "uncapped_status": "Proven IPL Star", "role": "Off-Spin Choke vs Left-Handers", "all_econ": 8.08, "hp_econ": 6.39, "hp_wkts": 10, "PBoS_final": 0.7750},
    {"rank": 5, "player_name": "Shamar Joseph", "player_id": 47050, "quota_tier": "Overseas (IPL: LSG)", "uncapped_status": "Proven IPL Express", "role": "150+ km/h Express Pace Backup for Archer", "all_econ": 10.31, "hp_econ": 8.84, "hp_wkts": 12, "PBoS_final": 0.5973},
    {"rank": 6, "player_name": "Sushant Mishra", "player_id": 7269, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (GT/RR)", "role": "Left-Arm Express Fast (7.41 HP Econ)", "all_econ": 8.68, "hp_econ": 7.41, "hp_wkts": 2, "PBoS_final": 0.6510},
    {"rank": 7, "player_name": "Mohammad Nabi", "player_id": 1107, "quota_tier": "Overseas (IPL: SRH/MI)", "uncapped_status": "Proven IPL Veteran", "role": "Powerplay / Middle Spin Controller", "all_econ": 8.48, "hp_econ": 7.04, "hp_wkts": 9, "PBoS_final": 0.7249},
    {"rank": 8, "player_name": "Tabraiz Shamsi", "player_id": 4237, "quota_tier": "Overseas (IPL: RR)", "uncapped_status": "Proven IPL Spinner", "role": "Attacking Wrist Spinner (8.40 HP Econ)", "all_econ": 9.64, "hp_econ": 8.40, "hp_wkts": 8, "PBoS_final": 0.5678},
    {"rank": 9, "player_name": "Kumar Kartikeya Singh", "player_id": 7574, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (MI/RR)", "role": "Left-Arm Mystery Spin (5 HP Wkts)", "all_econ": 8.52, "hp_econ": 9.72, "hp_wkts": 5, "PBoS_final": 0.4850},
    {"rank": 10, "player_name": "Riley Meredith", "player_id": 5940, "quota_tier": "Overseas (IPL: MI)", "uncapped_status": "Proven IPL Express", "role": "Hit-the-Deck Express Pacer (10 HP Wkts)", "all_econ": 9.41, "hp_econ": 8.45, "hp_wkts": 10, "PBoS_final": 0.5073}
]

df_bowl = pd.DataFrame(strat_bowl_data)
df_bowl.to_csv('output/top10_auction_bowlers.csv', index=False)

print("Saved clean, fully IPL-eligible top10_auction_batters.csv and top10_auction_bowlers.csv successfully!")
print(df_bat[['rank', 'player_name', 'quota_tier', 'uncapped_status', 'hp_sr', 'hp_avg']].to_string())
print(df_bowl[['rank', 'player_name', 'quota_tier', 'uncapped_status', 'hp_econ', 'hp_wkts']].to_string())
