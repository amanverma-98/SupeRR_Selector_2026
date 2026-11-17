import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_charts():
    os.makedirs("output/charts", exist_ok=True)
    
    # 1. Load the updated Top 10 CSVs
    df_bat = pd.read_csv("output/top10_auction_batters.csv")
    df_bowl = pd.read_csv("output/top10_auction_bowlers.csv")
    
    # Color palette
    c_navy = "#001c58"
    c_pink = "#ea1b86"
    c_gold = "#eab308"
    c_slate = "#475569"
    c_light = "#f8fafc"
    
    # -------------------------------------------------------------
    # CHART 1 (C2): Top 10 Batters - Baseline SR vs High Pressure SR
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    players = df_bat['player_name'].tolist()
    y_pos = np.arange(len(players))
    bar_height = 0.35
    
    players = players[::-1]
    baseline_sr = df_bat['all_sr'].tolist()[::-1]
    hp_sr = df_bat['hp_sr'].tolist()[::-1]
    
    ax.barh(y_pos - bar_height/2, baseline_sr, height=bar_height, label='Baseline Strike Rate', color='#94a3b8', alpha=0.85)
    bars_hp = ax.barh(y_pos + bar_height/2, hp_sr, height=bar_height, label='High Pressure SR (PI >= 0.494)', color=c_pink)
    
    for bar in bars_hp:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width:.1f}',
                va='center', ha='left', fontsize=8.5, fontweight='bold', color=c_navy)
        
    ax.set_yticks(y_pos)
    ax.set_yticklabels(players, fontsize=9.5, fontweight='semibold', color=c_navy)
    ax.set_xlabel('Strike Rate', fontsize=10, fontweight='bold', color=c_navy)
    ax.set_title('Top 10 Auction Batters: Baseline SR vs High-Pressure Strike Rate Uplift', fontsize=12, fontweight='bold', color=c_navy, pad=12)
    ax.set_xlim(0, 205)
    ax.legend(loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=9)
    ax.grid(axis='x', linestyle='--', alpha=0.3, color='#94a3b8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cbd5e1')
    ax.spines['bottom'].set_color('#cbd5e1')
    
    plt.tight_layout()
    chart2_path = "output/charts/C2_top10_batters_sr_updated.png"
    plt.savefig(chart2_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {chart2_path}")

    # -------------------------------------------------------------
    # CHART 2 (C3): Top 10 Bowlers - Baseline Economy vs High Pressure Economy
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    b_players = df_bowl['player_name'].tolist()
    y_pos = np.arange(len(b_players))
    
    b_players = b_players[::-1]
    baseline_econ = df_bowl['all_econ'].tolist()[::-1]
    hp_econ = df_bowl['hp_econ'].tolist()[::-1]
    
    ax.barh(y_pos - bar_height/2, baseline_econ, height=bar_height, label='Baseline Economy', color='#94a3b8', alpha=0.85)
    bars_econ = ax.barh(y_pos + bar_height/2, hp_econ, height=bar_height, label='High Pressure Econ (Tightening)', color=c_navy)
    
    for bar in bars_econ:
        width = bar.get_width()
        ax.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{width:.2f}',
                va='center', ha='left', fontsize=8.5, fontweight='bold', color=c_pink)
        
    ax.set_yticks(y_pos)
    ax.set_yticklabels(b_players, fontsize=9.5, fontweight='semibold', color=c_navy)
    ax.set_xlabel('Economy Rate (Lower is Better)', fontsize=10, fontweight='bold', color=c_navy)
    ax.set_title('Top 10 Auction Bowlers: High-Pressure Economy Squeeze vs Baseline', fontsize=12, fontweight='bold', color=c_navy, pad=12)
    ax.set_xlim(0, 12.5)
    ax.legend(loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=9)
    ax.grid(axis='x', linestyle='--', alpha=0.3, color='#94a3b8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cbd5e1')
    ax.spines['bottom'].set_color('#cbd5e1')
    
    plt.tight_layout()
    chart3_path = "output/charts/C3_top10_bowlers_econ_updated.png"
    plt.savefig(chart3_path, bbox_inches='tight')
    plt.close()
    print(f"Saved: {chart3_path}")

    # -------------------------------------------------------------
    # CHART 7: Top 3 Batters Multi-Metric Radar/Bar
    # -------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=300)
    top3_b = df_bat.head(3)
    metrics = ['all_sr', 'hp_sr', 'all_avg', 'hp_avg']
    labels = ['Base SR', 'HP SR', 'Base Avg', 'HP Avg']
    colors = ['#94a3b8', c_pink, '#94a3b8', c_navy]
    
    for idx, (_, row) in enumerate(top3_b.iterrows()):
        ax = axes[idx]
        vals = [row['all_sr'], row['hp_sr'], row['all_avg'], row['hp_avg']]
        bars = ax.bar(labels, vals, color=colors, width=0.55)
        ax.set_title(f"Rank {row['rank']}: {row['player_name']}\n({row['quota_tier']})", fontsize=10, fontweight='bold', color=c_navy)
        ax.set_ylim(0, max(vals) * 1.25)
        for b in bars:
            h = b.get_height()
            ax.text(b.get_x() + b.get_width()/2, h + 1.5, f"{h:.1f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', linestyle='--', alpha=0.3)
        
    plt.suptitle("Top 3 Auction Batters: Pressure Resilience Breakdown", fontsize=12, fontweight='bold', color=c_navy)
    plt.tight_layout()
    plt.savefig("output/charts/C7_top3_batters_metrics.png", bbox_inches='tight')
    plt.close()

    # -------------------------------------------------------------
    # CHART 8: Top 3 Bowlers Multi-Metric
    # -------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(12, 4), dpi=300)
    top3_bw = df_bowl.head(3)
    b_labels = ['Base Econ', 'HP Econ', 'HP Wkts']
    b_colors = ['#94a3b8', c_navy, c_pink]
    
    for idx, (_, row) in enumerate(top3_bw.iterrows()):
        ax = axes[idx]
        vals = [row['all_econ'], row['hp_econ'], row['hp_wkts']]
        bars = ax.bar(b_labels, vals, color=b_colors, width=0.55)
        ax.set_title(f"Rank {row['rank']}: {row['player_name']}\n({row['quota_tier']})", fontsize=10, fontweight='bold', color=c_navy)
        ax.set_ylim(0, max(vals) * 1.25)
        for b in bars:
            h = b.get_height()
            ax.text(b.get_x() + b.get_width()/2, h + 0.3, f"{h:.1f}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(axis='y', linestyle='--', alpha=0.3)
        
    plt.suptitle("Top 3 Auction Bowlers: Pressure Tightening Breakdown", fontsize=12, fontweight='bold', color=c_navy)
    plt.tight_layout()
    plt.savefig("output/charts/C8_top3_bowlers_metrics.png", bbox_inches='tight')
    plt.close()
    print("Saved C7 and C8 successfully!")

if __name__ == "__main__":
    generate_charts()
