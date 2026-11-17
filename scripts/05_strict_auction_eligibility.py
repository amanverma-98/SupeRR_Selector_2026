import pandas as pd

strat_bat_data = [
    {"rank": 1, "player_name": "Shai Hope", "player_id": 4369, "quota_tier": "Overseas (IPL: DC)", "uncapped_status": "Proven IPL Anchor", "role": "Master #3 Anchor (Post-Samson Void)", "all_sr": 141.3, "hp_sr": 157.0, "all_avg": 33.5, "hp_avg": 59.7, "PBS_final": 1.5702},
    {"rank": 2, "player_name": "Atharwa Taide", "player_id": 6466, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (PBKS)", "role": "Indian #3 Anchor / Fearless Opener", "all_sr": 138.3, "hp_sr": 149.1, "all_avg": 28.9, "hp_avg": 85.0, "PBS_final": 1.4912},
    {"rank": 3, "player_name": "Dunith Wellalage", "player_id": 7052, "quota_tier": "Overseas (SL)", "uncapped_status": "Young Prodigy (<22)", "role": "Spin-Bowling All-Rounder / #7 Finisher", "all_sr": 113.4, "hp_sr": 164.6, "all_avg": 17.9, "hp_avg": 39.5, "PBS_final": 1.9551},
    {"rank": 4, "player_name": "Jason Roy", "player_id": 1187, "quota_tier": "Overseas (IPL: KKR)", "uncapped_status": "Proven IPL Star", "role": "Fearless Powerplay Enforcer Cover", "all_sr": 122.4, "hp_sr": 173.3, "all_avg": 25.8, "hp_avg": 26.0, "PBS_final": 1.0236},
    {"rank": 5, "player_name": "Gulbadin Naib", "player_id": 2214, "quota_tier": "Overseas (IPL: DC)", "uncapped_status": "Proven IPL Star", "role": "Power Boundary Finisher & Seam Cover", "all_sr": 121.6, "hp_sr": 158.2, "all_avg": 21.6, "hp_avg": 43.5, "PBS_final": 1.2090},
    {"rank": 6, "player_name": "Lalit Yadav", "player_id": 6671, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (DC)", "role": "Indian #7 All-Round Spine & Off-Break", "all_sr": 104.9, "hp_sr": 128.4, "all_avg": 18.2, "hp_avg": 18.7, "PBS_final": 0.8384},
    {"rank": 7, "player_name": "Vijay Shankar", "player_id": 2877, "quota_tier": "Indian Core", "uncapped_status": "Proven IPL Veteran (GT)", "role": "Experienced Middle-Order Pace All-Rounder", "all_sr": 128.6, "hp_sr": 151.0, "all_avg": 26.1, "hp_avg": 29.0, "PBS_final": 0.6113},
    {"rank": 8, "player_name": "Kane Williamson", "player_id": 1568, "quota_tier": "Overseas (IPL: SRH/GT)", "uncapped_status": "Proven IPL Legend", "role": "Classical #3 Anchor & Tactical Mind", "all_sr": 108.2, "hp_sr": 123.7, "all_avg": 29.5, "hp_avg": 47.0, "PBS_final": 0.7850},
    {"rank": 9, "player_name": "Suyash Prabhudessai", "player_id": 8085, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (RCB)", "role": "Clutch Domestic 360-Degree Finisher", "all_sr": 111.5, "hp_sr": 122.9, "all_avg": 14.0, "hp_avg": 28.7, "PBS_final": 0.5602},
    {"rank": 10, "player_name": "Matthew Wade", "player_id": 796, "quota_tier": "Overseas (IPL: GT)", "uncapped_status": "Proven IPL Star", "role": "Left-Handed Clutch Pressure Finisher/WK", "all_sr": 132.7, "hp_sr": 150.9, "all_avg": 32.9, "hp_avg": 61.5, "PBS_final": 0.5789}
]

df_bat = pd.DataFrame(strat_bat_data)
df_bat.to_csv('output/top10_auction_batters.csv', index=False)

strat_bowl_data = [
    {"rank": 1, "player_name": "Mohit Sharma", "player_id": 2878, "quota_tier": "Indian Core", "uncapped_status": "Indian Veteran (GT)", "role": "Elite Death Knuckleball & Pacing IQ (Shami/Sandeep Backup)", "all_econ": 9.67, "hp_econ": 8.38, "hp_wkts": 26, "PBoS_final": 0.7179},
    {"rank": 2, "player_name": "Sean Abbott", "player_id": 1389, "quota_tier": "Overseas (IPL: SRH)", "uncapped_status": "Proven IPL Pacer", "role": "Hard-Length Pace All-Rounder (#8 Bat)", "all_econ": 9.96, "hp_econ": 7.89, "hp_wkts": 8, "PBoS_final": 0.8695},
    {"rank": 3, "player_name": "Michael Bracewell", "player_id": 6512, "quota_tier": "Overseas (IPL: RCB)", "uncapped_status": "Proven IPL Star", "role": "Off-Spin Choke vs Left-Handers & Finisher", "all_econ": 8.08, "hp_econ": 6.39, "hp_wkts": 10, "PBoS_final": 0.7750},
    {"rank": 4, "player_name": "Shamar Joseph", "player_id": 47050, "quota_tier": "Overseas (IPL: LSG)", "uncapped_status": "Proven IPL Express", "role": "150+ km/h Express Pace Backup for Jofra Archer", "all_econ": 10.31, "hp_econ": 8.84, "hp_wkts": 12, "PBoS_final": 0.5973},
    {"rank": 5, "player_name": "Mohammad Nabi", "player_id": 1107, "quota_tier": "Overseas (IPL: SRH/MI)", "uncapped_status": "Proven IPL Veteran", "role": "Powerplay / Middle Spin Controller", "all_econ": 8.48, "hp_econ": 7.04, "hp_wkts": 9, "PBoS_final": 0.7249},
    {"rank": 6, "player_name": "Tabraiz Shamsi", "player_id": 4237, "quota_tier": "Overseas (IPL: RR)", "uncapped_status": "Proven IPL Spinner", "role": "Attacking Wrist Spinner Cover for Bishnoi", "all_econ": 9.64, "hp_econ": 8.40, "hp_wkts": 8, "PBoS_final": 0.5678},
    {"rank": 7, "player_name": "Riley Meredith", "player_id": 5940, "quota_tier": "Overseas (IPL: MI)", "uncapped_status": "Proven IPL Express", "role": "Hit-the-Deck Express Pacer (10 HP Wkts)", "all_econ": 9.41, "hp_econ": 8.45, "hp_wkts": 10, "PBoS_final": 0.5073},
    {"rank": 8, "player_name": "FazalHaq Farooqi", "player_id": 7240, "quota_tier": "Overseas (IPL: SRH)", "uncapped_status": "Proven IPL Pacer", "role": "Left-Arm Swing & Death Yorker Cover for Burger", "all_econ": 8.42, "hp_econ": 7.74, "hp_wkts": 12, "PBoS_final": 0.3352},
    {"rank": 9, "player_name": "Matthew Humphreys", "player_id": 22471, "quota_tier": "Overseas (Emerging)", "uncapped_status": "Young Prodigy (<23)", "role": "Slow Left-Arm Orthodox Choke (5.0 HP Econ)", "all_econ": 7.22, "hp_econ": 5.00, "hp_wkts": 10, "PBoS_final": 0.8855},
    {"rank": 10, "player_name": "Kumar Kartikeya Singh", "player_id": 7574, "quota_tier": "Indian Core", "uncapped_status": "Indian Uncapped (MI)", "role": "Left-Arm Mystery Spin & Middle Squeeze", "all_econ": 8.77, "hp_econ": 10.13, "hp_wkts": 5, "PBoS_final": 0.4850}
]

df_bowl = pd.DataFrame(strat_bowl_data)
df_bowl.to_csv('output/top10_auction_bowlers.csv', index=False)

print("Saved clean, fully IPL 2027 eligible top10_auction_batters.csv and top10_auction_bowlers.csv successfully!")
