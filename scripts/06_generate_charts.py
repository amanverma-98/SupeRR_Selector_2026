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
    # CHART 1: Top 10 Batters - Baseline SR vs High Pressure SR
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    players = df_bat['player_name'].tolist()
    y_pos = np.arange(len(players))
    bar_height = 0.35
    
    # Invert so rank 1 is at top
    players = players[::-1]
    baseline_sr = df_bat['all_sr'].tolist()[::-1]
    hp_sr = df_bat['hp_sr'].tolist()[::-1]
    
    ax.barh(y_pos - bar_height/2, baseline_sr, height=bar_height, label='Baseline Strike Rate', color='#94a3b8', alpha=0.85)
    bars_hp = ax.barh(y_pos + bar_height/2, hp_sr, height=bar_height, label='High Pressure SR (PI >= 0.494)', color=c_pink)
    
    # Annotate HP SR values
    for bar in bars_hp:
        width = bar.get_width()
        ax.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width:.1f}',
                va='center', ha='left', fontsize=8.5, fontweight='bold', color=c_navy)
        
    ax.set_yticks(y_pos)
    ax.set_yticklabels(players, fontsize=9.5, fontweight='semibold', color=c_navy)
    ax.set_xlabel('Strike Rate', fontsize=10, fontweight='bold', color=c_navy)
    ax.set_title('Top 10 Batters: Baseline SR vs High-Pressure Strike Rate Uplift', fontsize=12, fontweight='bold', color=c_navy, pad=12)
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
    # CHART 2: Top 10 Bowlers - Baseline Economy vs High Pressure Economy
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')
    
    b_players = df_bowl['player_name'].tolist()
    y_pos = np.arange(len(b_players))
    
    # Invert so rank 1 is at top
    b_players = b_players[::-1]
    baseline_econ = df_bowl['all_econ'].tolist()[::-1]
    hp_econ = df_bowl['hp_econ'].tolist()[::-1]
    
    ax.barh(y_pos - bar_height/2, baseline_econ, height=bar_height, label='Baseline Economy', color='#94a3b8', alpha=0.85)
    bars_econ = ax.barh(y_pos + bar_height/2, hp_econ, height=bar_height, label='High Pressure Econ (Tightening)', color=c_navy)
    
    # Annotate HP Econ values
    for bar in bars_econ:
        width = bar.get_width()
        ax.text(width + 0.15, bar.get_y() + bar.get_height()/2, f'{width:.2f}',
                va='center', ha='left', fontsize=8.5, fontweight='bold', color=c_pink)
        
    ax.set_yticks(y_pos)
    ax.set_yticklabels(b_players, fontsize=9.5, fontweight='semibold', color=c_navy)
    ax.set_xlabel('Economy Rate (Lower is Better)', fontsize=10, fontweight='bold', color=c_navy)
    ax.set_title('Top 10 Bowlers: High-Pressure Economy Squeeze vs Baseline', fontsize=12, fontweight='bold', color=c_navy, pad=12)
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

if __name__ == "__main__":
    generate_charts()
