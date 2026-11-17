# -*- coding: utf-8 -*-
import base64
import os
import shutil

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return "data:image/png;base64," + base64.b64encode(img_file.read()).decode("utf-8")

def build():
    print("Encoding all 10 analytical charts to base64...")
    c1 = get_base64_image("output/charts/C1_pressure_distribution.png")
    c9 = get_base64_image("output/charts/C9_pressure_by_phase.png")
    c10 = get_base64_image("output/charts/C10_pi_by_stage.png")
    c6 = get_base64_image("output/charts/C6_heatmap_pressure.png")
    c2 = get_base64_image("output/charts/C2_top10_batters_sr_updated.png")
    c4 = get_base64_image("output/charts/C4_scatter_batters.png")
    c7 = get_base64_image("output/charts/C7_top3_batters_metrics.png")
    c3 = get_base64_image("output/charts/C3_top10_bowlers_econ_updated.png")
    c5 = get_base64_image("output/charts/C5_scatter_bowlers.png")
    c8 = get_base64_image("output/charts/C8_top3_bowlers_metrics.png")
    print("All 10 charts encoded successfully.")

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals — SupeRR Selector: High Pressure Analytics Engine</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', monospace; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: #001033; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #ea1b86; border-radius: 3px; }
    .chart-card:hover { transform: translateY(-2px); }
    @keyframes pulse-sub {
      0%, 100% { border-color: rgba(234, 27, 134, 0.4); box-shadow: 0 0 15px rgba(234, 27, 134, 0.2); }
      50% { border-color: rgba(234, 27, 134, 1); box-shadow: 0 0 25px rgba(234, 27, 134, 0.5); }
    }
    .animate-sub-in { animation: pulse-sub 2s infinite ease-in-out; }
    @keyframes pulse-bowl {
      0%, 100% { border-color: rgba(16, 185, 129, 0.4); box-shadow: 0 0 15px rgba(16, 185, 129, 0.2); }
      50% { border-color: rgba(16, 185, 129, 1); box-shadow: 0 0 25px rgba(16, 185, 129, 0.5); }
    }
    .animate-bowl-in { animation: pulse-bowl 2s infinite ease-in-out; }
  </style>
</head>
<body class="bg-[#020919] text-slate-100 min-h-screen custom-scroll antialiased selection:bg-[#ea1b86] selection:text-white">

  <!-- TOP APP HEADER -->
  <header class="border-b border-blue-900/60 bg-[#001238]/95 backdrop-blur sticky top-0 z-50 shadow-xl">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-18 py-3 flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center gap-3.5">
        <div class="w-11 h-11 rounded-xl bg-gradient-to-br from-[#ea1b86] via-[#b51065] to-[#001c58] p-0.5 shadow-lg shadow-pink-500/25 flex items-center justify-center font-extrabold text-white text-xl tracking-wider">
          RR
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#ea1b86]">Rajasthan Royals Strategy Group</span>
            <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-amber-400/20 text-amber-300 border border-amber-400/40">TATA IPL 2027</span>
          </div>
          <h1 class="text-base sm:text-lg font-bold text-white tracking-tight flex items-center gap-2">
            <span>IPL 2027 Auction War Room & Pressure Analytics Engine</span>
          </h1>
        </div>
      </div>

      <!-- Real-Time Metrics Strip -->
      <div class="flex items-center gap-2 sm:gap-3 text-xs font-mono">
        <div class="bg-blue-950/80 border border-blue-800/70 px-3 py-1.5 rounded-lg flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span class="text-slate-400">Database:</span>
          <span class="font-bold text-white">199,208 Balls</span>
        </div>
        <div class="bg-pink-950/60 border border-pink-700/60 px-3 py-1.5 rounded-lg flex items-center gap-2">
          <span class="text-pink-300">Retained Roster:</span>
          <span class="font-bold text-pink-200">19 Players (Mohd. Shami Added!)</span>
        </div>
      </div>
    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <nav class="bg-[#001744] border-b border-blue-900/70 sticky top-[69px] z-40 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex overflow-x-auto gap-1 py-2 text-xs sm:text-sm font-semibold">
      <button onclick="switchTab('tab-xi')" id="btn-tab-xi" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 bg-[#ea1b86] text-white shadow-md shadow-pink-600/30">
        <span>🏆</span> Squad Builder & Matchday Simulator
      </button>
      <button onclick="switchTab('tab-charts')" id="btn-tab-charts" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>📊</span> All Analytical Data Charts
      </button>
      <button onclick="switchTab('tab-batters')" id="btn-tab-batters" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>🏏</span> Batters Pressure Analytics
      </button>
      <button onclick="switchTab('tab-bowlers')" id="btn-tab-bowlers" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>🎯</span> Bowlers Pressure Analytics
      </button>
      <button onclick="switchTab('tab-simulator')" id="btn-tab-simulator" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>⚡</span> Live Pressure Index Calculator
      </button>
    </div>
  </nav>

  <!-- MAIN WRAPPER -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">

    <!-- ============================================================== -->
    <!-- TAB 1: SQUAD BUILDER & MATCHDAY SIMULATOR                      -->
    <!-- ============================================================== -->
    <div id="tab-xi" class="tab-content space-y-6">

      <!-- Official Retentions Hero Banner -->
      <div class="bg-gradient-to-r from-[#001c58] via-[#002677] to-[#ea1b86]/30 border border-blue-700/80 rounded-2xl p-5 shadow-2xl relative overflow-hidden">
        <div class="flex flex-wrap items-center justify-between gap-4 relative z-10">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-bold font-mono uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                Official TATA IPL 2027 Retentions
              </span>
              <span class="text-xs text-slate-300 font-mono">19 Players Locked • 6 Auction Slots Open</span>
            </div>
            <h2 class="text-lg sm:text-xl font-extrabold text-white mt-1">
              Mohd. Shami Joins the Royals: The Bowling Crisis is Resolved!
            </h2>
            <p class="text-xs sm:text-sm text-slate-200 mt-1 max-w-3xl leading-relaxed">
              With <b>Mohd. Shami</b> (Purple Cap Winner) partnering <b>Jofra Archer</b> (150+ km/h), <b>Sandeep Sharma</b> (death knuckleballs), <b>Ravi Bishnoi</b>, and <b>Ravindra Jadeja</b>, Rajasthan Royals field the most fearsome bowling attack in the IPL. The auction focus shifts directly to securing the <b>#3 Anchor (Shai Hope / Atharwa Taide)</b>!
            </p>
          </div>
          <div class="flex flex-col items-end gap-1.5 shrink-0">
            <span class="text-xs font-mono text-pink-300 bg-pink-950/80 border border-pink-700 px-3 py-1.5 rounded-lg font-bold">
              5 OS Retained (3 OS Slots Left)
            </span>
            <span class="text-[11px] text-slate-400 font-mono">BCCI Playing XI Limit: Max 4 OS</span>
          </div>
        </div>
      </div>

      <!-- Tactical Controls Bar -->
      <div class="bg-[#001744] border border-blue-900/60 p-5 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        
        <!-- Combination Blueprint Selector -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3">
          <span class="text-xs font-bold text-slate-300 uppercase tracking-wider font-mono">Championship Blueprint:</span>
          <div class="flex gap-2">
            <button onclick="setCombination('comboA')" id="btn-comboA" class="p-3 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-bold text-left transition shadow-sm shadow-pink-500/20">
              <div class="text-xs flex items-center gap-1.5">
                <span>🛡️</span> Option A: Classical Anchor Balance
              </div>
              <div class="text-[10px] text-pink-200 font-normal mt-0.5">Shai Hope #3 (59.7 HP Avg) + Shami & Archer</div>
            </button>
            <button onclick="setCombination('comboB')" id="btn-comboB" class="p-3 rounded-xl border border-blue-800 bg-blue-900/30 text-slate-300 font-semibold text-left transition hover:border-blue-600">
              <div class="text-xs flex items-center gap-1.5">
                <span>⚡</span> Option B: Dual Express Pace Firepower
              </div>
              <div class="text-[10px] text-slate-400 font-normal mt-0.5">Atharwa Taide #3 (85.0 HP Avg) + Dual 150+ km/h</div>
            </button>
          </div>
        </div>

        <!-- Match Scenario Selector -->
        <div class="flex items-center gap-3">
          <span class="text-xs font-bold text-slate-300 uppercase tracking-wider font-mono">Match Strategy:</span>
          <div class="bg-blue-950 p-1 rounded-xl border border-blue-800 flex gap-1">
            <button onclick="setMatchScenario('bowl_first')" id="btn-scen-bowl" class="px-4 py-2 rounded-lg font-bold text-xs bg-[#ea1b86] text-white transition">
              Bowling 1st (Plan A)
            </button>
            <button onclick="setMatchScenario('bat_first')" id="btn-scen-bat" class="px-4 py-2 rounded-lg font-bold text-xs bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition">
              Batting 1st (Plan B)
            </button>
          </div>
        </div>

      </div>

      <!-- Matchday Playing XI Roster Card -->
      <div class="bg-[#001744]/90 border border-blue-900/70 rounded-2xl p-6 shadow-2xl">
        <div class="flex flex-wrap items-center justify-between pb-4 mb-4 border-b border-blue-900/60 gap-3">
          <div>
            <div class="flex items-center gap-2">
              <h3 id="lineup-title" class="text-base sm:text-lg font-bold text-white tracking-tight">
                Starting XI: Bowling First (Tactical Anchor Blueprint)
              </h3>
              <span id="sub-state-badge" class="text-xs px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30 font-mono">
                Pre-Impact Sub (Bowling Phase)
              </span>
            </div>
            <p id="lineup-subtitle" class="text-xs text-slate-300 mt-1">
              <b>Tactical Anchor Blueprint:</b> Shai Hope anchors at #3 (59.7 HP Avg), Mohd. Shami + Jofra Archer + Sandeep Sharma lead the pace fortress.
            </p>
          </div>

          <!-- Impact Sub Execute Button -->
          <div class="flex items-center gap-3">
            <button onclick="toggleImpactSubExecution()" id="btn-execute-sub" class="px-4 py-2 rounded-xl text-xs font-bold font-mono bg-gradient-to-r from-[#ea1b86] to-[#b51065] text-white hover:opacity-90 shadow-md shadow-pink-600/30 flex items-center gap-2 transition">
              <span>🔄</span> <span id="execute-sub-text">Execute Chase Impact Sub (Bring Dubey IN)</span>
            </button>
          </div>
        </div>

        <!-- 11 Lineup Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3" id="lineup-grid">
          <!-- Populated dynamically via JS -->
        </div>

        <!-- Dynamic Impact Player Tactical Dugout Console -->
        <div class="mt-5" id="impact-banner">
          <!-- Populated dynamically via JS -->
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 2: ALL ANALYTICAL DATA CHARTS (10 CORE VISUAL MODELS)      -->
    <!-- ============================================================== -->
    <div id="tab-charts" class="tab-content hidden space-y-8">
      
      <!-- Top Banner -->
      <div class="bg-[#001744] border border-blue-900/60 p-6 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Comprehensive Empirical Evidence Suite</span>
          <h2 class="text-lg font-bold text-white">All Analytical Data Charts & Visual Models</h2>
          <p class="text-xs text-slate-300 mt-0.5">10 empirical visualizations generated across 199,208 deliveries (843 matches, 2022–2026). Click any chart to view high-resolution fullscreen.</p>
        </div>
        <div class="text-xs font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1.5 rounded-lg flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          10 Analytical Charts Displayed
        </div>
      </div>

      <!-- SECTION 1: DELIVERY-LEVEL PRESSURE MODELING (FOUNDATIONS) -->
      <div class="space-y-4">
        <div class="flex items-center gap-2.5 pb-2 border-b border-blue-900/60">
          <span class="text-base">🔬</span>
          <h3 class="text-sm font-bold uppercase tracking-wider text-pink-400 font-mono">Section A: Delivery-Level Pressure Modeling (199,208 Deliveries)</h3>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

          <!-- Chart 1: Continuous Pressure Index Distribution -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 1: Distribution</span>
                <h3 class="text-sm font-bold text-white">Continuous Pressure Index (PI) Distribution</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">199,208 Deliveries</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-1', 'Continuous Pressure Index (PI) Distribution across 199,208 Deliveries')">
              <img id="chart-img-1" src="__CHART_1__" alt="Pressure Distribution" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Empirical Partitioning:</b> Low (&lt;0.322, 40.0%), Medium (0.322–0.494, 36.2%), and <b class="text-pink-400">High Pressure (&ge;0.494, 23.8% — 47,446 balls)</b>. Captures true high-leverage deliveries across 843 matches.
            </div>
          </div>

          <!-- Chart 2: Pressure by Match Phase -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 2: Match Phases</span>
                <h3 class="text-sm font-bold text-white">Pressure Leverage Across Match Phases</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">PP vs Mid vs Death</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-9', 'Pressure Leverage Across Powerplay, Middle, and Death Overs')">
              <img id="chart-img-9" src="__CHART_9__" alt="Pressure by Phase" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Phase Variance:</b> Death Overs (Overs 17–20) experience extreme mean pressure (<b class="text-pink-400">PI = 0.684</b>) compared to Middle (0.428) and Powerplay (0.320). Drives need for designated closers.
            </div>
          </div>

          <!-- Chart 3: Tournament Stakes Comparison -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 3: Tournament Stakes</span>
                <h3 class="text-sm font-bold text-white">Tournament Stage Pressure: Playoffs vs League</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Stage Leverage</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-10', 'Tournament Stakes Comparison: Playoff / Final vs League Matches')">
              <img id="chart-img-10" src="__CHART_10__" alt="Stage Comparison" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Knockout Multiplier:</b> Playoff / Final deliveries carry a +15% upward baseline shift in pressure index due to single-elimination tournament jeopardy.
            </div>
          </div>

          <!-- Chart 4: 2D Pressure Heatmap -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 4: 2D Heatmap</span>
                <h3 class="text-sm font-bold text-white">Pressure Index Heatmap: Wickets Lost vs Balls Left</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">State Matrix</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-6', '2D Pressure Index Heatmap: Wickets Lost vs Balls Remaining')">
              <img id="chart-img-6" src="__CHART_6__" alt="Pressure Heatmap" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Non-Linear Squeeze:</b> Pressure compounds asymptotically when &ge;5 wickets have fallen with &lt;30 deliveries remaining (PI &gt; 0.82).
            </div>
          </div>

        </div>
      </div>

      <!-- SECTION 2: BATTERS PRESSURE PERFORMANCE & CLUTCH SCORING -->
      <div class="space-y-4">
        <div class="flex items-center gap-2.5 pb-2 border-b border-blue-900/60">
          <span class="text-base">🏏</span>
          <h3 class="text-sm font-bold uppercase tracking-wider text-pink-400 font-mono">Section B: Batters Pressure Performance & Clutch Scoring (Top 10 Targets)</h3>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Chart 5: Top 10 Batters SR Uplift -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 5: SR Uplift</span>
                <h3 class="text-sm font-bold text-white">Top 10 Batters: Baseline vs HP SR</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Auction Top 10</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-2', 'Top 10 Batters: Baseline Strike Rate vs High-Pressure Strike Rate Uplift')">
              <img id="chart-img-2" src="__CHART_2__" alt="Top 10 Batters SR" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Key Takeaway:</b> Shai Hope anchors at <b class="text-pink-400">157.0 HP SR (59.7 HP Avg)</b> solving post-Samson void. Atharwa Taide delivers 149.1 HP SR and 85.0 HP Avg!
            </div>
          </div>

          <!-- Chart 6: Batters Clutch Quadrants -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 6: Clutch Quadrant</span>
                <h3 class="text-sm font-bold text-white">Batters: HP Strike Rate vs Dot Ball %</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Scatter</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-4', 'Batters Clutch Quadrant Analysis: High-Pressure Strike Rate vs Dot Ball %')">
              <img id="chart-img-4" src="__CHART_4__" alt="Batters Scatter" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Clutch Elite:</b> Top-right quadrant isolates players with high HP SR (&gt;150) and low dot ball rates (&lt;32%), confirming Wellalage and Roy as ice-cool finishers.
            </div>
          </div>

          <!-- Chart 7: Top 3 Batters Multi-Metric Radar -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 7: Multi-Metric</span>
                <h3 class="text-sm font-bold text-white">Top 3 Batters: Dimensional Profiles</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Radar Profiles</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-7', 'Top 3 Batters Multi-Metric Dimensional Profile Breakdown')">
              <img id="chart-img-7" src="__CHART_7__" alt="Top 3 Batters Metrics" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Role Symmetry:</b> Shai Hope dominates Average (59.7), Atharwa Taide balances fearless aggression with 85.0 HP Avg, and Wellalage adds 164.6 HP SR lower hitting.
            </div>
          </div>

        </div>
      </div>

      <!-- SECTION 3: BOWLERS PRESSURE PERFORMANCE & CLUTCH SQUEEZE -->
      <div class="space-y-4">
        <div class="flex items-center gap-2.5 pb-2 border-b border-blue-900/60">
          <span class="text-base">🎯</span>
          <h3 class="text-sm font-bold uppercase tracking-wider text-pink-400 font-mono">Section C: Bowlers Pressure Performance & Clutch Squeeze (Top 10 Targets)</h3>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

          <!-- Chart 8: Top 10 Bowlers Economy Squeeze -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 8: Econ Squeeze</span>
                <h3 class="text-sm font-bold text-white">Top 10 Bowlers: Baseline vs HP Econ</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Auction Top 10</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-3', 'Top 10 Bowlers: High-Pressure Economy Squeeze vs Baseline')">
              <img id="chart-img-3" src="__CHART_3__" alt="Top 10 Bowlers Economy" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Key Takeaway:</b> Mohit Sharma restricts death batters to <b class="text-emerald-400">8.38 HP Econ</b> (26 wickets). Sean Abbott chokes scoring to 7.89 HP Econ.
            </div>
          </div>

          <!-- Chart 9: Bowlers Clutch Quadrants -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 9: Clutch Quadrant</span>
                <h3 class="text-sm font-bold text-white">Bowlers: HP Economy vs Dot Ball %</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Scatter</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-5', 'Bowlers Clutch Quadrant Analysis: High-Pressure Economy vs Dot Ball %')">
              <img id="chart-img-5" src="__CHART_5__" alt="Bowlers Scatter" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Squeeze Elite:</b> Top-left quadrant isolates bowlers with sub-8.5 HP Economy and &gt;35% Dot Ball frequency under extreme pressure.
            </div>
          </div>

          <!-- Chart 10: Top 3 Bowlers Multi-Metric Radar -->
          <div class="bg-[#001744] border border-blue-900/60 rounded-2xl overflow-hidden shadow-xl flex flex-col justify-between chart-card border-blue-800/60 hover:border-pink-500/60 transition duration-150">
            <div class="p-4 border-b border-blue-900/60 flex items-center justify-between">
              <div>
                <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider">Chart 10: Multi-Metric</span>
                <h3 class="text-sm font-bold text-white">Top 3 Bowlers: Dimensional Profiles</h3>
              </div>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-blue-950 text-slate-300 border border-blue-800">Radar Profiles</span>
            </div>
            <div class="p-4 bg-slate-950/60 flex items-center justify-center cursor-pointer" onclick="openChartModal('chart-img-8', 'Top 3 Bowlers Multi-Metric Dimensional Profile Breakdown')">
              <img id="chart-img-8" src="__CHART_8__" alt="Top 3 Bowlers Metrics" class="w-full h-auto max-h-64 object-contain rounded-lg transition duration-200">
            </div>
            <div class="p-4 bg-blue-950/40 border-t border-blue-900/50 text-xs text-slate-300">
              <b class="text-white font-mono">Surgical Discipline:</b> Mohit Sharma leads in Wickets (26), Sean Abbott in tight containment (7.89 Econ), and Michael Bracewell in off-spin choke (6.39 Econ).
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 3: BATTERS PRESSURE ANALYTICS (RANKED TABLE & DOSSIERS)    -->
    <!-- ============================================================== -->
    <div id="tab-batters" class="tab-content hidden space-y-6">
      
      <!-- Table Header & Filters -->
      <div class="bg-[#001744] border border-blue-900/60 p-5 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Quantitative Auction Dossiers</span>
          <h2 class="text-lg font-bold text-white">Top 10 Pressure Batters (Auction Targets)</h2>
        </div>
        <div class="flex items-center gap-3">
          <select id="bat-filter" onchange="renderBattersTable()" class="bg-blue-950 border border-blue-800 text-xs rounded-xl px-3 py-2 text-white font-mono focus:outline-none focus:border-pink-500">
            <option value="all">All Targets (10 Players)</option>
            <option value="indian">Indian Core Only (4 Players)</option>
            <option value="overseas">Overseas Targets Only (6 Players)</option>
          </select>
        </div>
      </div>

      <!-- Batters Table -->
      <div class="bg-[#001744]/90 border border-blue-900/70 rounded-2xl overflow-hidden shadow-2xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-blue-950/90 text-slate-300 font-mono uppercase text-[10px] tracking-wider border-b border-blue-900">
              <tr>
                <th class="py-3 px-4 text-center">Rank</th>
                <th class="py-3 px-4">Player & ID</th>
                <th class="py-3 px-4">Quota Tier</th>
                <th class="py-3 px-4">Tactical Role for RR</th>
                <th class="py-3 px-4 text-right">Base SR</th>
                <th class="py-3 px-4 text-right">HP SR (&ge;0.494)</th>
                <th class="py-3 px-4 text-right">HP Avg</th>
                <th class="py-3 px-4 text-right">PBS Score</th>
              </tr>
            </thead>
            <tbody id="batters-tbody" class="divide-y divide-blue-900/50 font-mono">
              <!-- Populated dynamically via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tactical Roles Breakdown Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">#3 Anchor Solution</span>
          <h4 class="text-sm font-bold text-white mt-1">Shai Hope & Atharwa Taide</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Fixes Rajasthan Royals' middle-order collapse void post-Samson. Shai Hope delivers an elite <b class="text-white">59.7 HP Avg</b>, while Atharwa Taide offers an Indian anchor option with <b class="text-white">85.0 HP Avg</b>.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">Middle-Order Balance</span>
          <h4 class="text-sm font-bold text-white mt-1">Vijay Shankar & Lalit Yadav</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Experienced Indian all-round stability. Vijay Shankar brings <b class="text-white">151.0 HP SR</b> and Lalit Yadav delivers off-spin control and death strike capability.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">Under-22 Prodigy Pick</span>
          <h4 class="text-sm font-bold text-white mt-1">Dunith Wellalage (Sri Lanka)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Elite raw young international talent: <b class="text-emerald-300 font-bold">164.6 HP SR</b> and 39.5 HP Avg with tight left-arm orthodox bowling. High-ceiling future franchise spine.</p>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 4: BOWLERS PRESSURE ANALYTICS (RANKED TABLE & DOSSIERS)    -->
    <!-- ============================================================== -->
    <div id="tab-bowlers" class="tab-content hidden space-y-6">
      
      <!-- Table Header & Filters -->
      <div class="bg-[#001744] border border-blue-900/60 p-5 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Quantitative Auction Dossiers</span>
          <h2 class="text-lg font-bold text-white">Top 10 Pressure Bowlers (Auction Targets)</h2>
        </div>
        <div class="flex items-center gap-3">
          <select id="bowl-filter" onchange="renderBowlersTable()" class="bg-blue-950 border border-blue-800 text-xs rounded-xl px-3 py-2 text-white font-mono focus:outline-none focus:border-pink-500">
            <option value="all">All Targets (10 Players)</option>
            <option value="indian">Indian Core Only (2 Players)</option>
            <option value="overseas">Overseas Targets Only (8 Players)</option>
          </select>
        </div>
      </div>

      <!-- Bowlers Table -->
      <div class="bg-[#001744]/90 border border-blue-900/70 rounded-2xl overflow-hidden shadow-2xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-blue-950/90 text-slate-300 font-mono uppercase text-[10px] tracking-wider border-b border-blue-900">
              <tr>
                <th class="py-3 px-4 text-center">Rank</th>
                <th class="py-3 px-4">Player & ID</th>
                <th class="py-3 px-4">Quota Tier</th>
                <th class="py-3 px-4">Tactical Role for RR</th>
                <th class="py-3 px-4 text-right">Base Econ</th>
                <th class="py-3 px-4 text-right">HP Econ (&ge;0.494)</th>
                <th class="py-3 px-4 text-right">HP Wkts</th>
                <th class="py-3 px-4 text-right">PBoS Score</th>
              </tr>
            </thead>
            <tbody id="bowlers-tbody" class="divide-y divide-blue-900/50 font-mono">
              <!-- Populated dynamically via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tactical Roles Breakdown Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">Workload Insurance</span>
          <h4 class="text-sm font-bold text-white mt-1">Mohit Sharma (GT / India)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Veteran Indian death overs closer: drops economy to <b class="text-emerald-300 font-bold">8.38 HP Econ with 26 wickets</b>. Provides vital rotation cover for Shami and Sandeep Sharma.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">Hard-Length Pace All-Rounder</span>
          <h4 class="text-sm font-bold text-white mt-1">Sean Abbott (SRH / Australia)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">7.89 HP Economy and 8 HP wickets. Hits a hard length in middle overs and extends RR's lower-order batting spine at #8.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider font-mono">150+ km/h Express Cover</span>
          <h4 class="text-sm font-bold text-white mt-1">Shamar Joseph (LSG / WI)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Raw express pace backup for Jofra Archer: restricts scoring to <b class="text-cyan-300 font-bold">8.84 HP Econ</b> while capturing 12 high-pressure wickets.</p>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: LIVE PRESSURE INDEX SIMULATOR & CALCULATOR              -->
    <!-- ============================================================== -->
    <div id="tab-simulator" class="tab-content hidden space-y-6">
      
      <div class="bg-[#001744] border border-blue-900/60 p-6 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Continuous Match State Model</span>
          <h2 class="text-lg font-bold text-white">Interactive Pressure Index (PI) Calculator</h2>
          <p class="text-xs text-slate-300 mt-0.5">Test real-time match leverage by adjusting Required Run Rate, Wickets Lost, Balls Remaining, and Match Stage.</p>
        </div>
        <div class="text-xs font-mono text-pink-400 bg-pink-500/10 border border-pink-500/30 px-3 py-1.5 rounded-lg">
          Live Continuous Formula
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Controls Column (Sliders) -->
        <div class="lg:col-span-2 bg-[#001744]/90 border border-blue-900/70 p-6 rounded-2xl shadow-2xl space-y-5">
          <h3 class="text-sm font-bold text-white uppercase tracking-wider font-mono border-b border-blue-900/60 pb-3 flex items-center justify-between">
            <span>Match State Parameters</span>
            <span class="text-xs text-slate-400 font-normal">Adjust values dynamically</span>
          </h3>

          <!-- Slider 1: Required Run Rate -->
          <div>
            <div class="flex justify-between items-center text-xs mb-1.5">
              <span class="font-bold text-slate-200">Required Run Rate (RRR):</span>
              <span id="val-rrr" class="font-mono font-bold text-pink-400 bg-pink-500/10 px-2 py-0.5 rounded border border-pink-500/20">11.5 RPO</span>
            </div>
            <input type="range" id="slider-rrr" min="4.0" max="18.0" step="0.1" value="11.5" oninput="calculatePI()" class="w-full accent-[#ea1b86] cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
              <span>4.0 (Comfortable)</span>
              <span>10.0 (Tense)</span>
              <span>18.0 (Extreme)</span>
            </div>
          </div>

          <!-- Slider 2: Wickets Lost -->
          <div>
            <div class="flex justify-between items-center text-xs mb-1.5">
              <span class="font-bold text-slate-200">Wickets Lost:</span>
              <span id="val-wickets" class="font-mono font-bold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">6 Wickets</span>
            </div>
            <input type="range" id="slider-wickets" min="0" max="9" step="1" value="6" oninput="calculatePI()" class="w-full accent-amber-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
              <span>0 (Full Resources)</span>
              <span>5 (Middle Order)</span>
              <span>9 (Last Wicket)</span>
            </div>
          </div>

          <!-- Slider 3: Balls Remaining -->
          <div>
            <div class="flex justify-between items-center text-xs mb-1.5">
              <span class="font-bold text-slate-200">Balls Remaining:</span>
              <span id="val-balls" class="font-mono font-bold text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20">18 Balls</span>
            </div>
            <input type="range" id="slider-balls" min="1" max="120" step="1" value="18" oninput="calculatePI()" class="w-full accent-cyan-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
              <span>1 (Final Ball)</span>
              <span>30 (Death Overs)</span>
              <span>120 (Powerplay Start)</span>
            </div>
          </div>

          <!-- Slider 4: Target Score -->
          <div>
            <div class="flex justify-between items-center text-xs mb-1.5">
              <span class="font-bold text-slate-200">Target Score:</span>
              <span id="val-target" class="font-mono font-bold text-blue-400 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">185 Runs</span>
            </div>
            <input type="range" id="slider-target" min="120" max="240" step="5" value="185" oninput="calculatePI()" class="w-full accent-blue-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-1">
              <span>120 (Low)</span>
              <span>175 (Par SMS)</span>
              <span>240 (Monster)</span>
            </div>
          </div>

          <!-- Match Stage Toggle -->
          <div>
            <div class="flex justify-between items-center text-xs mb-2">
              <span class="font-bold text-slate-200">Tournament Stage:</span>
              <span id="val-stage" class="font-mono font-bold text-purple-400 bg-purple-500/10 px-2 py-0.5 rounded border border-purple-500/20">Playoff / Final (+0.15)</span>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <button onclick="setSimStage('league')" id="btn-stage-league" class="py-2.5 rounded-xl border border-blue-800 bg-blue-950 text-slate-300 font-mono text-xs font-bold transition hover:border-blue-600">
                League Stage Match
              </button>
              <button onclick="setSimStage('playoff')" id="btn-stage-playoff" class="py-2.5 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-mono text-xs font-bold transition shadow-sm shadow-pink-500/20">
                Playoff / Final (Knockout)
              </button>
            </div>
          </div>

        </div>

        <!-- Real-Time Gauge & Output Column -->
        <div class="bg-[#001744]/90 border border-blue-900/70 p-6 rounded-2xl shadow-2xl flex flex-col justify-between">
          <div>
            <h3 class="text-sm font-bold text-white uppercase tracking-wider font-mono border-b border-blue-900/60 pb-3">
              Calculated Pressure Output
            </h3>

            <!-- Central Big PI Readout -->
            <div class="text-center py-6">
              <span class="text-xs font-mono text-slate-400 uppercase tracking-widest block">Continuous Pressure Index</span>
              <div id="gauge-pi-val" class="text-5xl font-black font-mono text-pink-400 my-2 tracking-tight">0.712</div>
              <span id="gauge-tier-pill" class="inline-block px-3 py-1 rounded-full text-xs font-bold font-mono uppercase tracking-wider bg-pink-500/20 text-pink-300 border border-pink-500/40 animate-pulse">
                High Pressure Delivery
              </span>
            </div>

            <!-- Component Contribution Breakdown -->
            <div class="space-y-3 pt-2 border-t border-blue-900/60 text-xs">
              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-slate-300">Run Rate Leverage (w=0.35)</span>
                  <span id="bar-val-rrr" class="font-mono text-pink-400">0.245</span>
                </div>
                <div class="w-full bg-blue-950 h-2 rounded-full overflow-hidden">
                  <div id="bar-fill-rrr" class="bg-pink-500 h-full rounded-full transition-all duration-200" style="width: 70%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-slate-300">Resource Depletion (w=0.25)</span>
                  <span id="bar-val-wickets" class="font-mono text-amber-400">0.167</span>
                </div>
                <div class="w-full bg-blue-950 h-2 rounded-full overflow-hidden">
                  <div id="bar-fill-wickets" class="bg-amber-400 h-full rounded-full transition-all duration-200" style="width: 67%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] mb-1">
                  <span class="text-slate-300">Death Urgency (w=0.20)</span>
                  <span id="bar-val-balls" class="font-mono text-cyan-400">0.155</span>
                </div>
                <div class="w-full bg-blue-950 h-2 rounded-full overflow-hidden">
                  <div id="bar-fill-balls" class="bg-cyan-400 h-full rounded-full transition-all duration-200" style="width: 78%"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Tactical Recommendation -->
          <div class="bg-blue-950/80 border border-blue-800 p-4 rounded-xl mt-6">
            <span class="text-[10px] font-mono text-[#ea1b86] uppercase font-bold tracking-wider block">Recommended Tactical Action:</span>
            <p id="sim-recommendation" class="text-xs text-slate-200 mt-1 leading-relaxed">
              High Pressure Leverage: Deploy <b class="text-white">Mohd. Shami</b> (reverse yorker) or <b class="text-white">Jofra Archer</b> (150+ yorker). For chase: Requires <b class="text-pink-300 font-bold">Shai Hope</b> or <b class="text-pink-300 font-bold">Shubham Dubey</b>.
            </p>
          </div>
        </div>

      </div>

      <!-- Mathematical Formulation Card -->
      <div class="bg-[#001744]/90 border border-blue-900/70 p-6 rounded-2xl shadow-xl space-y-4">
        <h3 class="text-sm font-bold text-white uppercase tracking-wider font-mono border-b border-blue-900/60 pb-3 flex items-center gap-2">
          <span>📐</span> Continuous Pressure Index Mathematical Formulation
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed">
          The continuous Pressure Index (PI) evaluates match leverage ball-by-ball. Unlike discrete heuristics, it handles non-linear compounding of run-rate urgency and wicket loss.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs font-mono">
          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-pink-400 font-bold block">1. Run Rate Urgency</span>
            <p class="text-slate-300 text-[11px]">L_req = clip((RRR - 6.0) / 10.0, 0, 1)</p>
            <p class="text-slate-400 text-[10px]">Scales leverage linearly from 6.0 RPO (baseline) to 16.0 RPO (extreme).</p>
          </div>

          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-amber-400 font-bold block">2. Resource Depletion</span>
            <p class="text-slate-300 text-[11px]">W_adj = Wickets_Lost / 9.0</p>
            <p class="text-slate-400 text-[10px]">Measures remaining batting resources and collapse exposure.</p>
          </div>

          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-cyan-400 font-bold block">3. Death Urgency</span>
            <p class="text-slate-300 text-[11px]">D_exp = exp(-Balls_Remaining / 30.0)</p>
            <p class="text-slate-400 text-[10px]">Exponential escalation as deliveries run out in the death overs.</p>
          </div>

          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-purple-400 font-bold block">4. Match Consistency Factor</span>
            <p class="text-slate-300 text-[11px]">Multiplier = 0.75 + 0.25 / (1 + CV_match)</p>
            <p class="text-slate-400 text-[10px]">Penalizes volatile boom-or-bust performers; rewards ice-cool repeatability across matches.</p>
          </div>
        </div>
      </div>

    </div>

  </main>

  <!-- MODAL FOR FULLSCREEN CHART VIEW -->
  <div id="chart-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="bg-[#001744] border border-blue-700/80 rounded-2xl max-w-4xl w-full p-6 shadow-2xl relative">
      <div class="flex items-center justify-between pb-3 mb-4 border-b border-blue-800">
        <h3 id="modal-chart-title" class="text-base font-bold text-white font-mono">Chart View</h3>
        <button onclick="closeChartModal()" class="text-slate-400 hover:text-white text-xl font-bold px-2 py-1">✕</button>
      </div>
      <div class="flex items-center justify-center bg-slate-950/80 rounded-xl p-4">
        <img id="modal-chart-img" src="" alt="Enlarged Chart" class="max-h-[75vh] w-auto object-contain rounded">
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // DATA STORE: AUCTION TARGETS (EXCLUDING 19 RR RETAINED PLAYERS)
    const battersData = [
      { rank: 1, name: "Shai Hope", id: 4369, tier: "Overseas (DC)", status: "Proven IPL Anchor", role: "Master #3 Anchor (Post-Samson Void)", baseSr: 141.3, hpSr: 157.0, hpAvg: 59.7, score: 1.5702 },
      { rank: 2, name: "Atharwa Taide", id: 6466, tier: "Indian Core (PBKS)", status: "Indian Uncapped", role: "Indian #3 Anchor / Fearless Opener", baseSr: 138.3, hpSr: 149.1, hpAvg: 85.0, score: 1.4912 },
      { rank: 3, name: "Dunith Wellalage", id: 7052, tier: "Overseas (SL)", status: "Young Prodigy (<22)", role: "Spin All-Rounder / #7 Lower Hitter", baseSr: 113.4, hpSr: 164.6, hpAvg: 39.5, score: 1.9551 },
      { rank: 4, name: "Jason Roy", id: 1187, tier: "Overseas (KKR)", status: "Proven IPL Star", role: "Fearless Powerplay Enforcer Cover", baseSr: 122.4, hpSr: 173.3, hpAvg: 26.0, score: 1.0236 },
      { rank: 5, name: "Gulbadin Naib", id: 2214, tier: "Overseas (DC)", status: "Proven IPL Star", role: "Power Boundary Finisher & Seam Cover", baseSr: 121.6, hpSr: 158.2, hpAvg: 43.5, score: 1.2090 },
      { rank: 6, name: "Lalit Yadav", id: 6671, tier: "Indian Core (DC)", status: "Indian Uncapped", role: "Indian #7 All-Round Spine & Off-Break", baseSr: 104.9, hpSr: 128.4, hpAvg: 18.7, score: 0.8384 },
      { rank: 7, name: "Vijay Shankar", id: 2877, tier: "Indian Core (GT)", status: "Proven IPL Veteran", role: "Middle-Order Pace All-Rounder", baseSr: 128.6, hpSr: 151.0, hpAvg: 29.0, score: 0.6113 },
      { rank: 8, name: "Kane Williamson", id: 1568, tier: "Overseas (SRH/GT)", status: "Proven IPL Legend", role: "Classical #3 Anchor & Master Tactician", baseSr: 108.2, hpSr: 123.7, hpAvg: 47.0, score: 0.7850 },
      { rank: 9, name: "Suyash Prabhudessai", id: 8085, tier: "Indian Core (RCB)", status: "Indian Uncapped", role: "Clutch Domestic 360° Finisher", baseSr: 111.5, hpSr: 122.9, hpAvg: 28.7, score: 0.5602 },
      { rank: 10, name: "Matthew Wade", id: 796, tier: "Overseas (GT)", status: "Proven IPL Closer", role: "Clutch Wicketkeeper Finisher (LHB)", baseSr: 132.7, hpSr: 150.9, hpAvg: 61.5, score: 0.5789 }
    ];

    const bowlersData = [
      { rank: 1, name: "Mohit Sharma", id: 2878, tier: "Indian Core (GT)", status: "Indian Veteran Closer", role: "Death Knuckleball IQ (Workload Cover)", baseEcon: 9.67, hpEcon: 8.38, hpWkts: 26, score: 0.7179 },
      { rank: 2, name: "Sean Abbott", id: 1389, tier: "Overseas (SRH)", status: "Proven IPL Pacer", role: "Hard-Length Pace All-Rounder (#8 Bat)", baseEcon: 9.96, hpEcon: 7.89, hpWkts: 8, score: 0.8695 },
      { rank: 3, name: "Michael Bracewell", id: 6512, tier: "Overseas (RCB)", status: "Proven IPL Star", role: "Off-Spin Choke vs Left-Handers & Finisher", baseEcon: 8.08, hpEcon: 6.39, hpWkts: 10, score: 0.7750 },
      { rank: 4, name: "Shamar Joseph", id: 47050, tier: "Overseas (LSG)", status: "Proven IPL Express", role: "150+ km/h Express Pace Backup for Archer", baseEcon: 10.31, hpEcon: 8.84, hpWkts: 12, score: 0.5973 },
      { rank: 5, name: "Mohammad Nabi", id: 1107, tier: "Overseas (MI)", status: "Proven IPL Veteran", role: "Powerplay / Middle Spin Controller", baseEcon: 8.48, hpEcon: 7.04, hpWkts: 9, score: 0.7249 },
      { rank: 6, name: "Tabraiz Shamsi", id: 4237, tier: "Overseas (RR)", status: "Proven IPL Spinner", role: "Attacking Wrist Spinner Cover for Bishnoi", baseEcon: 9.64, hpEcon: 8.40, hpWkts: 8, score: 0.5678 },
      { rank: 7, name: "Riley Meredith", id: 5940, tier: "Overseas (MI)", status: "Proven IPL Express", role: "Hit-the-Deck Express Pacer (10 Wkts)", baseEcon: 9.41, hpEcon: 8.45, hpWkts: 10, score: 0.5073 },
      { rank: 8, name: "FazalHaq Farooqi", id: 7240, tier: "Overseas (SRH)", status: "Proven IPL Pacer", role: "Left-Arm Swing & Death Yorker Cover for Burger", baseEcon: 8.42, hpEcon: 7.74, hpWkts: 12, score: 0.3352 },
      { rank: 9, name: "Matthew Humphreys", id: 22471, tier: "Overseas (Emerging)", status: "Young Prodigy (<23)", role: "Slow Left-Arm Orthodox Choke", baseEcon: 7.22, hpEcon: 5.00, hpWkts: 10, score: 0.8855 },
      { rank: 10, name: "Kumar Kartikeya", id: 7574, tier: "Indian Core (MI)", status: "Indian Uncapped", role: "Left-Arm Mystery Spin & Middle Squeeze", baseEcon: 8.77, hpEcon: 10.13, hpWkts: 5, score: 0.4850 }
    ];

    // ==========================================================
    // CRICKET-ACCURATE SQUAD STATES & TACTICAL BLUEPRINTS
    // ==========================================================
    let currentScenario = 'bowl_first'; // 'bowl_first' or 'bat_first'
    let isSubExecuted = false;
    let currentCombo = 'comboA'; // 'comboA' (Tactical Anchor) or 'comboB' (Dual Express Pace)

    // ----------------------------------------------------------
    // BLUEPRINT A: TACTICAL ANCHOR (Shai Hope #3 + Mohd. Shami + Jofra Archer + Sandeep Sharma)
    // ----------------------------------------------------------
    const bowlFirstPreSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target #1", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option (RHB)", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher (RHB)", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 7, name: "Ravi Bishnoi", type: "IND", role: "Frontline Specialist Leg-Spinner (Bowler 2: 4 Overs)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 3: 4 Overs - Seam & Reverse)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace Spearhead (Bowler 4: 4 Overs)", highlight: "Starting Bowler 4", isSub: false },
      { pos: 10, name: "Sandeep Sharma", type: "IND", role: "Death Knuckleball Specialist (Bowler 5: 4 Overs)", highlight: "Starting Bowler 5", isSub: false },
      { pos: 11, name: "Sushant Mishra / Siddharth", type: "IND", role: "Left-Arm Seam / Spin Depth (Reserve Bowler)", highlight: "Retained Core", isSub: false }
    ];

    const bowlFirstPostSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target #1", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option (RHB)", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher (RHB)", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (LHB / SLA)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey (IMPACT SUB IN)", type: "IND", role: "Death Boundary Finisher (173.7 HP SR — Replaces Sandeep for Chase)", highlight: "🔥 IMPACT PLAYER ACTIVATED", isSub: true },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (4 Overs Completed)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace (4 Overs Completed)", highlight: "4 Overs Bowled", isSub: false },
      { pos: 10, name: "Ravi Bishnoi", type: "IND", role: "Frontline Specialist Leg-Spinner (4 Overs Completed)", highlight: "4 Overs Bowled", isSub: false },
      { pos: 11, name: "Sushant Mishra / Siddharth", type: "IND", role: "Domestic Support Core", highlight: "Retained Core", isSub: false }
    ];

    const batFirstPreSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target #1", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Captain", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 7, name: "Shubham Dubey", type: "IND", role: "Designated Death Power Finisher (173.7 HP SR across 99 balls!)", highlight: "Starting Batter #7", isSub: false },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 2: 4 Overs)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Strike (Bowler 3: 4 Overs)", highlight: "Starting Bowler 3", isSub: false },
      { pos: 10, name: "Ravi Bishnoi", type: "IND", role: "Specialist Leg-Spinner (Bowler 4: 4 Overs)", highlight: "Starting Bowler 4", isSub: false },
      { pos: 11, name: "Sushant Mishra", type: "IND", role: "Left-Arm Fast Bowler (Bowler 5: 4 Overs)", highlight: "Starting Bowler 5", isSub: false }
    ];

    const batFirstPostSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (Agile Outfield Fielding)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target #1", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Frontline Bowler 1", isSub: false },
      { pos: 7, name: "Sandeep Sharma (IMPACT BOWLER IN)", type: "IND", role: "Death Knuckleball Specialist (Bowler 5: 4 Overs — Replaces Dubey)", highlight: "🛡️ 5TH BOWLER ACTIVATED", isSub: true },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 2: 4 Overs)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Strike (Bowler 3: 4 Overs)", highlight: "Frontline Bowler 3", isSub: false },
      { pos: 10, name: "Ravi Bishnoi", type: "IND", role: "Specialist Leg-Spinner (Bowler 4: 4 Overs)", highlight: "Frontline Bowler 4", isSub: false },
      { pos: 11, name: "Sushant Mishra", type: "IND", role: "Left-Arm Fast Bowler", highlight: "Retained Core", isSub: false }
    ];

    // ----------------------------------------------------------
    // BLUEPRINT B: DUAL EXPRESS PACE (Atharwa Taide #3 IND + Archer & Burger / Joseph Dual 150+ km/h)
    // ----------------------------------------------------------
    const bowlFirstPreSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 7, name: "Ravi Bishnoi", type: "IND", role: "Frontline Specialist Leg-Spinner (Bowler 2: 4 Overs)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 3: 4 Overs)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 10, name: "Nandre Burger / S. Joseph", type: "OS", role: "145-150+ km/h Express Pace Missile (Bowler 5: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Sandeep Sharma", type: "IND", role: "Death Knuckleball Specialist (Bowler 6: 4 Overs)", highlight: "Starting Bowler 6", isSub: false }
    ];

    const bowlFirstPostSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (LHB / SLA)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey (IMPACT SUB IN)", type: "IND", role: "Death Boundary Finisher (173.7 HP SR — Replaces Sandeep for Chase)", highlight: "🔥 IMPACT PLAYER ACTIVATED", isSub: true },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (4 Overs Completed)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (4 Overs Completed)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 10, name: "Nandre Burger / S. Joseph", type: "OS", role: "145-150+ km/h Express Pace Missile (4 Overs Completed)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Ravi Bishnoi", type: "IND", role: "Frontline Specialist Leg-Spinner", highlight: "Retained Core", isSub: false }
    ];

    const batFirstPreSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (LHB Boundary Hitter)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Captain", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 7, name: "Shubham Dubey", type: "IND", role: "Designated Death Power Finisher (173.7 HP SR across 99 balls!)", highlight: "Starting Batter #7", isSub: false },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 2: 4 Overs)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 3: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 10, name: "Nandre Burger / S. Joseph", type: "OS", role: "145-150+ km/h Express Pace Missile (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Ravi Bishnoi", type: "IND", role: "Frontline Specialist Leg-Spinner (Bowler 5: 4 Overs)", highlight: "Starting Bowler 5", isSub: false }
    ];

    const batFirstPostSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Powerplay Prodigy (Agile Outfield Fielding)", highlight: "Retained Core", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Frontline Bowler 1", isSub: false },
      { pos: 7, name: "Sandeep Sharma (IMPACT BOWLER IN)", type: "IND", role: "Death Knuckleball Specialist (Bowler 5: 4 Overs — Replaces Dubey)", highlight: "🛡️ 5TH BOWLER ACTIVATED", isSub: true },
      { pos: 8, name: "Mohd. Shami", type: "IND", role: "Premier Strike Bowler (Bowler 2: 4 Overs)", highlight: "🔥 SHAMI RETAINED", isSub: false },
      { pos: 9, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 3: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 10, name: "Nandre Burger / S. Joseph", type: "OS", role: "145-150+ km/h Express Pace Missile (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Ravi Bishnoi", type: "IND", role: "Specialist Leg-Spinner (Frontline Bowler)", highlight: "Frontline Bowler", isSub: false }
    ];

    // ==========================================================
    // RENDER LINEUP ACCORDING TO COMBINATION, SCENARIO & SUB
    // ==========================================================
    function renderLineup() {
      const titleEl = document.getElementById('lineup-title');
      const subBadgeEl = document.getElementById('sub-state-badge');
      const subtitleEl = document.getElementById('lineup-subtitle');
      const executeBtn = document.getElementById('execute-sub-text');
      const banner = document.getElementById('impact-banner');

      // Subtitle updates according to Blueprint
      if (currentCombo === 'comboA') {
        subtitleEl.innerHTML = "<b>Tactical Anchor Blueprint:</b> Shai Hope anchors at #3 (59.7 HP Avg), Mohd. Shami + Jofra Archer + Sandeep Sharma form an unbreachable pace fortress.";
      } else {
        subtitleEl.innerHTML = "<b>Dual Express Pace Blueprint:</b> Atharwa Taide anchors at #3 (85.0 HP Avg), unleashing <b>Dual 150+ km/h pacers (Archer + Burger/Joseph)</b> alongside Shami!";
      }

      // Dataset selection matrix
      const datasetMatrix = {
        comboA: {
          bowl_first: { pre: bowlFirstPreSub_A, post: bowlFirstPostSub_A },
          bat_first:  { pre: batFirstPreSub_A,  post: batFirstPostSub_A }
        },
        comboB: {
          bowl_first: { pre: bowlFirstPreSub_B, post: bowlFirstPostSub_B },
          bat_first:  { pre: batFirstPreSub_B,  post: batFirstPostSub_B }
        }
      };

      const data = datasetMatrix[currentCombo][currentScenario][isSubExecuted ? 'post' : 'pre'];

      // Scenario State UI
      if (currentScenario === 'bowl_first') {
        if (!isSubExecuted) {
          titleEl.innerText = currentCombo === 'comboA' ? "Starting XI: Bowling First (Tactical Anchor Blueprint)" : "Starting XI: Bowling First (Dual Express Pace Blueprint)";
          subBadgeEl.innerText = "Pre-Impact Sub (Bowling Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30 font-mono";
          executeBtn.innerText = "Execute Chase Impact Sub (Bring Dubey IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-blue-950/70 border border-blue-800/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🛡️</span>
                <div>
                  <div class="text-xs font-bold text-blue-300 uppercase tracking-wider font-mono">1st Innings — Fielding & Bowling Phase (20 Overs)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">RR fields 5 frontline specialist bowlers delivering 20 complete overs: <b class="text-white">Mohd. Shami, Jofra Archer, Sandeep Sharma, Ravi Bishnoi, Ravindra Jadeja</b>. <b class="text-pink-300">Shubham Dubey</b> rests in the dugout.</div>
                </div>
              </div>
              <div class="bg-pink-950/50 border border-pink-700/60 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-pink-300 font-bold uppercase tracking-wider">Tactical Dugout Bench (Impact Reserve)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Shubham Dubey (Vidarbha / RR Retained)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/40 font-mono animate-pulse">CHASE SUB READY</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">173.7 HP SR across 99 balls | 25.3% Boundary Rate. Ready to swap in at innings break!</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">9 IND + 2 OS (Super Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        } else {
          titleEl.innerText = "Innings 2 Lineup: Chasing Target (Shubham Dubey Activated at #7)";
          subBadgeEl.innerText = "Post-Impact Sub (Chase Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/30 font-mono animate-pulse";
          executeBtn.innerText = "Reset to Pre-Sub Starting XI (Sandeep IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-pink-950/70 border border-pink-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🔥</span>
                <div>
                  <div class="text-xs font-bold text-pink-300 uppercase tracking-wider font-mono">2nd Innings — Run Chase (Firepower Activated)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Tactical substitution executed: Sandeep Sharma replaced by <b class="text-white">Shubham Dubey (173.7 HP SR)</b> at #7. Batting depth stacked to #8 to ice high-pressure chases!</div>
                </div>
              </div>
              <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-slate-400 font-bold uppercase tracking-wider">Tactical Dugout Bench (Subbed Out)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Sandeep Sharma (RR Retained Core)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-700/60 text-slate-300 border border-slate-600 font-mono">4 OVERS COMPLETE</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">Completed 4 overs of death knuckleballs in 1st Innings. Exits for chase batting firepower.</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">9 IND + 2 OS (Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        }
      } else {
        if (!isSubExecuted) {
          titleEl.innerText = currentCombo === 'comboA' ? "Starting XI: Batting First (Deep Batting Firepower - Hope #3)" : "Starting XI: Batting First (Deep Batting Firepower - Taide #3)";
          subBadgeEl.innerText = "Pre-Impact Sub (Batting Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/30 font-mono";
          executeBtn.innerText = "Execute Defense Impact Sub (Bring Sandeep IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-pink-950/70 border border-pink-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🏏</span>
                <div>
                  <div class="text-xs font-bold text-pink-300 uppercase tracking-wider font-mono">1st Innings — Batting Phase (Setting Target)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Shubham Dubey starts at #7 to provide maximum death overs boundary firepower. <b class="text-blue-300">Sandeep Sharma</b> rests in the dugout.</div>
                </div>
              </div>
              <div class="bg-blue-950/50 border border-blue-700/60 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-blue-300 font-bold uppercase tracking-wider">Tactical Dugout Bench (Impact Reserve)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Sandeep Sharma (RR Retained Core)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/40 font-mono animate-pulse">DEFENSE SUB READY</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">Master of death knuckleballs. Ready to enter for 2nd innings to activate 5 frontline specialist bowlers!</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">9 IND + 2 OS (Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        } else {
          titleEl.innerText = currentCombo === 'comboA' ? "Innings 2 Lineup: Defending Target (5 Bowlers Active - Shami & Sandeep Closers)" : "Innings 2 Lineup: Defending Target (5 Bowlers Active - Dual 150+ km/h Express)";
          subBadgeEl.innerText = "Post-Impact Sub (Defense Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-mono animate-pulse";
          executeBtn.innerText = "Reset to Pre-Sub Starting XI (Dubey IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-emerald-950/70 border border-emerald-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🛡️</span>
                <div>
                  <div class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">2nd Innings — Defending Target (5 Bowlers Active)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Batter replaced by <b class="text-white">Sandeep Sharma</b>. Gives RR 5 full frontline specialist bowlers delivering 4 overs each: <b class="text-white">Shami (4), Archer (4), Sandeep (4), Bishnoi (4), Jadeja (4) = 20 complete overs!</b></div>
                </div>
              </div>
              <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-slate-400 font-bold uppercase tracking-wider">Tactical Dugout Bench (Subbed Out)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Shubham Dubey (RR Retained Core)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-700/60 text-slate-300 border border-slate-600 font-mono">BATTING COMPLETE</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">Completed death boundary hitting duty in 1st Innings (173.7 HP SR). Exits for bowling defense.</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">9 IND + 2 OS (Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        }
      }

      // Render 11 Cards
      const grid = document.getElementById('lineup-grid');
      grid.innerHTML = data.map(p => `
        <div class="bg-blue-950/60 border ${p.isSub ? (currentScenario === 'bowl_first' ? 'border-pink-500 bg-pink-950/40 animate-sub-in' : 'border-emerald-500 bg-emerald-950/40 animate-bowl-in') : (p.type === 'IND' ? 'border-blue-700/60' : 'border-amber-500/50')} rounded-xl p-3.5 flex items-start justify-between gap-3 relative overflow-hidden group hover:border-pink-500 transition duration-150">
          <div class="flex items-start gap-3">
            <span class="w-6 h-6 rounded-md bg-blue-900/80 flex items-center justify-center font-mono font-bold text-xs ${p.type === 'IND' ? 'text-blue-300' : 'text-amber-300'}">${p.pos}</span>
            <div>
              <div class="font-bold text-sm text-white group-hover:text-pink-300 transition flex items-center gap-2">
                ${p.name}
              </div>
              <div class="text-[11px] text-slate-300 mt-0.5">${p.role}</div>
            </div>
          </div>
          <div class="text-right flex flex-col items-end">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono ${p.type === 'IND' ? 'bg-blue-500/20 text-blue-300 border border-blue-500/40' : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'}">${p.type}</span>
            <span class="text-[9px] ${p.isSub ? (currentScenario === 'bowl_first' ? 'text-pink-300 font-extrabold animate-pulse' : 'text-emerald-300 font-extrabold animate-pulse') : (p.highlight.includes('SHAMI') ? 'text-emerald-300 font-extrabold' : (p.highlight.includes('DUAL') ? 'text-cyan-300 font-bold' : 'text-pink-400'))} mt-1 font-semibold">${p.highlight}</span>
          </div>
        </div>
      `).join('');
    }

    function setMatchScenario(scenario) {
      currentScenario = scenario;
      isSubExecuted = false;
      document.getElementById('btn-scen-bowl').className = scenario === 'bowl_first' ? 'px-4 py-2 rounded-lg font-bold text-xs bg-[#ea1b86] text-white transition' : 'px-4 py-2 rounded-lg font-bold text-xs bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition';
      document.getElementById('btn-scen-bat').className = scenario === 'bat_first' ? 'px-4 py-2 rounded-lg font-bold text-xs bg-[#ea1b86] text-white transition' : 'px-4 py-2 rounded-lg font-bold text-xs bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition';
      renderLineup();
    }

    function toggleImpactSubExecution() {
      isSubExecuted = !isSubExecuted;
      renderLineup();
    }

    function setCombination(combo) {
      currentCombo = combo;
      document.getElementById('btn-comboA').className = combo === 'comboA' ? 'p-3 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-bold text-left transition shadow-sm shadow-pink-500/20' : 'p-3 rounded-xl border border-blue-800 bg-blue-900/30 text-slate-300 font-semibold text-left transition hover:border-blue-600';
      document.getElementById('btn-comboB').className = combo === 'comboB' ? 'p-3 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-bold text-left transition shadow-sm shadow-pink-500/20' : 'p-3 rounded-xl border border-blue-800 bg-blue-900/30 text-slate-300 font-semibold text-left transition hover:border-blue-600';
      renderLineup();
    }

    // BATTERS TABLE RENDER
    function renderBattersTable() {
      const filter = document.getElementById('bat-filter').value;
      const filtered = battersData.filter(p => {
        if (filter === 'indian') return p.tier.includes('Indian');
        if (filter === 'overseas') return p.tier.includes('Overseas');
        return true;
      });

      const tbody = document.getElementById('batters-tbody');
      tbody.innerHTML = filtered.map(p => `
        <tr class="hover:bg-blue-900/30 transition">
          <td class="py-2.5 px-4 font-bold text-center text-pink-400 font-mono">${p.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white flex items-center gap-2">
            <span>${p.name}</span>
            <span class="text-[10px] text-slate-400 font-mono">#${p.id}</span>
          </td>
          <td class="py-2.5 px-4">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono ${p.tier.includes('Indian') ? 'bg-blue-500/20 text-blue-300 border border-blue-500/40' : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'}">${p.tier}</span>
          </td>
          <td class="py-2.5 px-4 text-slate-300 font-sans">${p.role}</td>
          <td class="py-2.5 px-4 text-right font-mono text-slate-400">${p.baseSr.toFixed(1)}</td>
          <td class="py-2.5 px-4 text-right font-mono font-bold text-pink-400">${p.hpSr.toFixed(1)}</td>
          <td class="py-2.5 px-4 text-right font-mono text-emerald-400 font-bold">${p.hpAvg.toFixed(1)}</td>
          <td class="py-2.5 px-4 text-right font-mono font-black text-amber-300">${p.score.toFixed(4)}</td>
        </tr>
      `).join('');
    }

    // BOWLERS TABLE RENDER
    function renderBowlersTable() {
      const filter = document.getElementById('bowl-filter').value;
      const filtered = bowlersData.filter(p => {
        if (filter === 'indian') return p.tier.includes('Indian');
        if (filter === 'overseas') return p.tier.includes('Overseas');
        return true;
      });

      const tbody = document.getElementById('bowlers-tbody');
      tbody.innerHTML = filtered.map(p => `
        <tr class="hover:bg-blue-900/30 transition">
          <td class="py-2.5 px-4 font-bold text-center text-emerald-400 font-mono">${p.rank}</td>
          <td class="py-2.5 px-4 font-bold text-white flex items-center gap-2">
            <span>${p.name}</span>
            <span class="text-[10px] text-slate-400 font-mono">#${p.id}</span>
          </td>
          <td class="py-2.5 px-4">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold font-mono ${p.tier.includes('Indian') ? 'bg-blue-500/20 text-blue-300 border border-blue-500/40' : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'}">${p.tier}</span>
          </td>
          <td class="py-2.5 px-4 text-slate-300 font-sans">${p.role}</td>
          <td class="py-2.5 px-4 text-right font-mono text-slate-400">${p.baseEcon.toFixed(2)}</td>
          <td class="py-2.5 px-4 text-right font-mono font-bold text-emerald-400">${p.hpEcon.toFixed(2)}</td>
          <td class="py-2.5 px-4 text-right font-mono text-pink-400 font-bold">${p.hpWkts}</td>
          <td class="py-2.5 px-4 text-right font-mono font-black text-amber-300">${p.score.toFixed(4)}</td>
        </tr>
      `).join('');
    }

    // SIMULATOR REAL-TIME CALCULATION
    let simStage = 'playoff';

    function setSimStage(stage) {
      simStage = stage;
      document.getElementById('btn-stage-league').className = stage === 'league' ? 'py-2.5 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-mono text-xs font-bold transition shadow-sm shadow-pink-500/20' : 'py-2.5 rounded-xl border border-blue-800 bg-blue-950 text-slate-300 font-mono text-xs font-bold transition hover:border-blue-600';
      document.getElementById('btn-stage-playoff').className = stage === 'playoff' ? 'py-2.5 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-mono text-xs font-bold transition shadow-sm shadow-pink-500/20' : 'py-2.5 rounded-xl border border-blue-800 bg-blue-950 text-slate-300 font-mono text-xs font-bold transition hover:border-blue-600';
      document.getElementById('val-stage').innerText = stage === 'playoff' ? 'Playoff / Final (+0.15)' : 'League Stage (+0.00)';
      calculatePI();
    }

    function calculatePI() {
      const rrr = parseFloat(document.getElementById('slider-rrr').value);
      const wickets = parseInt(document.getElementById('slider-wickets').value);
      const balls = parseInt(document.getElementById('slider-balls').value);
      const target = parseInt(document.getElementById('slider-target').value);

      document.getElementById('val-rrr').innerText = rrr.toFixed(1) + ' RPO';
      document.getElementById('val-wickets').innerText = wickets + ' Wickets';
      document.getElementById('val-balls').innerText = balls + ' Balls (' + (20 - balls/6).toFixed(1) + ' ov)';
      document.getElementById('val-target').innerText = target + ' Runs';

      // Mathematical Formulation:
      // PI = w1*L_req + w2*W_adj + w3*D_exp + w4*T_stage + w5*S_target
      const l_req = Math.min(1.0, Math.max(0.0, (rrr - 6.0) / 10.0));
      const w_adj = Math.min(1.0, wickets / 9.0);
      const d_exp = Math.exp(-balls / 30.0);
      const t_stage = simStage === 'playoff' ? 1.0 : 0.0;
      const s_target = Math.min(1.0, Math.max(0.0, (target - 140.0) / 80.0));

      const w1 = 0.35, w2 = 0.25, w3 = 0.20, w4 = 0.12, w5 = 0.08;
      const pi = (w1 * l_req) + (w2 * w_adj) + (w3 * d_exp) + (w4 * t_stage) + (w5 * s_target);
      const clampedPI = Math.min(1.0, Math.max(0.0, pi));

      // UI Updates
      document.getElementById('gauge-pi-val').innerText = clampedPI.toFixed(3);

      const pill = document.getElementById('gauge-tier-pill');
      const rec = document.getElementById('sim-recommendation');
      if (clampedPI >= 0.494) {
        pill.innerText = "High Pressure Delivery (Clutch Zone)";
        pill.className = "mt-3 inline-block px-3 py-1 rounded-full text-xs font-bold font-mono uppercase tracking-wider bg-pink-500/20 text-pink-300 border border-pink-500/40 animate-pulse";
        rec.innerHTML = "High Pressure Leverage: Deploy <b class='text-white'>Mohd. Shami</b> (reverse yorker) or <b class='text-white'>Jofra Archer</b> (150+ yorker). For chase: Requires <b class='text-pink-300 font-bold'>Shai Hope</b> (59.7 HP Avg) or <b class='text-pink-300 font-bold'>Shubham Dubey</b> (173.7 HP SR).";
      } else if (clampedPI >= 0.322) {
        pill.innerText = "Medium Pressure Delivery";
        pill.className = "mt-3 inline-block px-3 py-1 rounded-full text-xs font-bold font-mono uppercase tracking-wider bg-amber-500/20 text-amber-300 border border-amber-500/40";
        rec.innerHTML = "Tactical Middle Leverage: Rotate strike with <b class='text-white'>Shai Hope</b> (59.7 HP Avg) and deploy <b class='text-white'>Ravindra Jadeja</b> to restrict run rate.";
      } else {
        pill.innerText = "Low Pressure Delivery";
        pill.className = "mt-3 inline-block px-3 py-1 rounded-full text-xs font-bold font-mono uppercase tracking-wider bg-blue-500/20 text-blue-300 border border-blue-500/40";
        rec.innerHTML = "Low Pressure Phase: Exploit field restrictions with <b class='text-white'>Yashasvi Jaiswal</b> and <b class='text-white'>Vaibhav Sooryavanshi</b>.";
      }

      // Bar fills
      document.getElementById('bar-val-rrr').innerText = (w1 * l_req).toFixed(3);
      document.getElementById('bar-fill-rrr').style.width = Math.min(100, Math.round(l_req * 100)) + '%';

      document.getElementById('bar-val-wickets').innerText = (w2 * w_adj).toFixed(3);
      document.getElementById('bar-fill-wickets').style.width = Math.min(100, Math.round(w_adj * 100)) + '%';

      document.getElementById('bar-val-balls').innerText = (w3 * d_exp).toFixed(3);
      document.getElementById('bar-fill-balls').style.width = Math.min(100, Math.round(d_exp * 100)) + '%';
    }

    // TAB SWITCHER
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.getElementById(tabId).classList.remove('hidden');

      document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.className = "tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40";
      });
      document.getElementById('btn-' + tabId).className = 'tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 bg-[#ea1b86] text-white shadow-md shadow-pink-600/30';
    }

    // MODAL HANDLERS
    function openChartModal(imgId, title) {
      document.getElementById('modal-chart-img').src = document.getElementById(imgId).src;
      document.getElementById('modal-chart-title').innerText = title;
      document.getElementById('chart-modal').classList.remove('hidden');
    }

    function closeChartModal() {
      document.getElementById('chart-modal').classList.add('hidden');
    }

    // INITIALIZE
    document.addEventListener('DOMContentLoaded', () => {
      renderLineup();
      renderBattersTable();
      renderBowlersTable();
      calculatePI();
    });
  </script>
</body>
</html>
"""

    print("Injecting 10 analytical charts into template...")
    html_content = html_template.replace("__CHART_1__", c1)
    html_content = html_content.replace("__CHART_9__", c9)
    html_content = html_content.replace("__CHART_10__", c10)
    html_content = html_content.replace("__CHART_6__", c6)
    html_content = html_content.replace("__CHART_2__", c2)
    html_content = html_content.replace("__CHART_4__", c4)
    html_content = html_content.replace("__CHART_7__", c7)
    html_content = html_content.replace("__CHART_3__", c3)
    html_content = html_content.replace("__CHART_5__", c5)
    html_content = html_content.replace("__CHART_8__", c8)

    # 1. Save to output/dashboard.html
    out_file = "output/dashboard.html"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved: {out_file} ({len(html_content)} characters)")

    # 2. Save to root index.html (for instant GitHub Pages deployment!)
    root_file = "index.html"
    with open(root_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved: {root_file} ({len(html_content)} characters) [GitHub Pages Ready!]")

    # 3. Save to artifact directory
    art_file = "C:/Users/av979/.gemini/antigravity/brain/59d0f182-ce1c-4aa2-88f1-13c7a9855303/dashboard.html"
    with open(art_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved to artifact: {art_file}")

if __name__ == "__main__":
    build()
