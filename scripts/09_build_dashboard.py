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
            <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-amber-400/20 text-amber-300 border border-amber-400/40">SupeRR Selector S2</span>
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
          <span class="font-bold text-white">199,208 Balls (843 Matches)</span>
        </div>
        <div class="bg-pink-950/60 border border-pink-700/60 px-3 py-1.5 rounded-lg flex items-center gap-2">
          <span class="text-pink-300">High Pressure:</span>
          <span class="font-bold text-pink-200">47,446 Balls (PI &ge; 0.494)</span>
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
      <button onclick="switchTab('tab-sim')" id="btn-tab-sim" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>⚡</span> Delivery Pressure Simulator
      </button>
      <button onclick="switchTab('tab-methodology')" id="btn-tab-methodology" class="tab-btn px-4 py-2 rounded-lg transition-all duration-150 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-blue-900/40">
        <span>🔬</span> Mathematical Engine & Audit
      </button>
    </div>
  </nav>

  <!-- MAIN VIEWPORT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">

    <!-- ============================================================== -->
    <!-- TAB 1: SQUAD BUILDER & MATCHDAY SIMULATOR (TEST BENCH)         -->
    <!-- ============================================================== -->
    <div id="tab-xi" class="tab-content space-y-6">
      
      <!-- Top Control & Validation Bar -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Quota Validator -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl relative overflow-hidden">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider font-mono">BCCI Quota Validator</span>
            <span class="px-2 py-0.5 text-[10px] font-bold rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40" id="quota-status-pill">100% Rule Compliant</span>
          </div>
          <h3 class="text-base font-bold text-white mb-2">Live Matchday Playing XI Quota</h3>
          <div class="space-y-2.5 font-mono text-xs">
            <div>
              <div class="flex justify-between mb-1">
                <span class="text-slate-300">Indian Core Players:</span>
                <span class="text-emerald-400 font-bold" id="quota-ind-count">7 / 7 (Min 7 Required)</span>
              </div>
              <div class="w-full h-2 bg-blue-950 rounded-full overflow-hidden">
                <div class="h-full bg-emerald-500 rounded-full w-full"></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between mb-1">
                <span class="text-slate-300">Overseas Quota Slots:</span>
                <span class="text-amber-300 font-bold" id="quota-os-count">4 / 4 (Max 4 Permitted)</span>
              </div>
              <div class="w-full h-2 bg-blue-950 rounded-full overflow-hidden">
                <div class="h-full bg-amber-400 rounded-full w-full"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Tactical Combination Switcher (Interactive) -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block mb-1 font-mono">Tactical Blueprint Switcher</span>
          <h3 class="text-base font-bold text-white mb-2.5">Select Strategic Combination</h3>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <button onclick="setCombination('comboA')" id="btn-comboA" class="p-3 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-bold text-left transition shadow-sm shadow-pink-500/20">
              <div class="font-extrabold text-pink-300 text-[11px] flex items-center gap-1.5">
                <span>🛡️</span> Option A: Tactical Anchor
              </div>
              <div class="text-[10px] text-slate-300 mt-1 leading-tight">Shai Hope (#3) + Mohit Sharma Closer + Archer Express</div>
            </button>
            <button onclick="setCombination('comboB')" id="btn-comboB" class="p-3 rounded-xl border border-blue-800 bg-blue-900/30 text-slate-300 font-semibold text-left transition hover:border-blue-600">
              <div class="font-extrabold text-blue-300 text-[11px] flex items-center gap-1.5">
                <span>⚡</span> Option B: Dual Express Pace
              </div>
              <div class="text-[10px] text-slate-400 mt-1 leading-tight">Atharwa Taide (#3) + Archer & Shamar Joseph (Dual 150+ km/h!)</div>
            </button>
          </div>
        </div>

        <!-- Cricket-Authentic Impact Player Simulator -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-1.5">
              <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider font-mono">Impact Player Engine</span>
              <span class="text-[10px] font-mono bg-blue-900/60 px-2 py-0.5 rounded text-blue-200">Rule: Ind for Ind</span>
            </div>
            <h3 class="text-base font-bold text-white mb-1">Match Scenario & Phase</h3>
            <p class="text-[11px] text-slate-300 mb-2 leading-snug" id="impact-desc">Plan A: Bowling 1st (5 Frontline Bowlers start; Dubey rests on bench as Chase Impact Sub).</p>
          </div>
          <div class="flex gap-2 text-xs font-mono">
            <button onclick="setMatchScenario('bowl_first')" id="btn-scen-bowl" class="flex-1 py-2 rounded-lg font-bold bg-[#ea1b86] text-white transition">Plan A: Bowling 1st</button>
            <button onclick="setMatchScenario('bat_first')" id="btn-scen-bat" class="flex-1 py-2 rounded-lg font-bold bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition">Plan B: Batting 1st</button>
          </div>
        </div>
      </div>

      <!-- Lineup Interactive Board -->
      <div class="bg-[#001744]/90 border border-blue-900/70 rounded-2xl p-6 shadow-2xl">
        <div class="flex flex-wrap items-center justify-between gap-3 pb-4 mb-5 border-b border-blue-900/60">
          <div>
            <div class="flex items-center gap-2">
              <h3 class="text-lg font-bold text-white" id="lineup-title">Starting XI: Bowling First (5 Frontline Bowlers)</h3>
              <span class="text-xs px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30 font-mono" id="sub-state-badge">Pre-Impact Sub (Bowling Phase)</span>
            </div>
            <p class="text-xs text-slate-400 mt-1" id="lineup-subtitle">Includes <b>Vaibhav Sooryavanshi</b> at #2 alongside 5 frontline bowlers delivering 20 full overs.</p>
          </div>

          <!-- Impact Sub Action Button -->
          <div class="flex items-center gap-3">
            <button onclick="toggleImpactSubExecution()" id="btn-execute-sub" class="px-4 py-2 rounded-xl text-xs font-bold font-mono bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-500 hover:to-purple-500 text-white shadow-lg shadow-pink-600/30 flex items-center gap-2 transition">
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
              <b class="text-white font-mono">Key Takeaway:</b> Shubham Dubey accelerates from 148.6 to <b class="text-pink-400">173.7 HP SR</b> (+25.1 uplift). Shai Hope anchors at 157.0 HP SR with a 59.7 HP Avg.
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
              <b class="text-white font-mono">Clutch Elite:</b> Top-right quadrant isolates players with high HP SR (&gt;150) and low dot ball rates (&lt;32%), confirming Dubey and Wellalage as ice-cool finishers.
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
              <b class="text-white font-mono">Role Symmetry:</b> Dubey dominates Boundary% (25.3%), Hope dominates Average (59.7), and Taide balances fearless aggression with 85.0 HP Avg.
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
              <b class="text-white font-mono">Key Takeaway:</b> Mohit Sharma restricts death batters to <b class="text-emerald-400">8.38 HP Econ</b> across 151 balls (26 wickets). Sean Abbott chokes scoring to 7.91 HP Econ.
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
              <b class="text-white font-mono">Surgical Discipline:</b> Mohit Sharma leads in Wickets (26), Abbott in Dot% (38.1%), and Brijesh Sharma provides unmatched uncapped economy control (7.19).
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
            <option value="indian">Indian Core Only (5 Players)</option>
            <option value="overseas">Overseas Targets Only (5 Players)</option>
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
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">#7 Lower Order Finisher</span>
          <h4 class="text-sm font-bold text-white mt-1">Shubham Dubey (RR Retained Core)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Vidarbha power hitter with unmatched death leverage: <b class="text-pink-300 font-bold">173.7 HP SR across 99 balls</b> with a 25.3% boundary frequency. Solves RR's tail collapse at #7.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-pink-400 uppercase tracking-wider font-mono">Under-22 Prodigy Pick</span>
          <h4 class="text-sm font-bold text-white mt-1">Dunith Wellalage (Age 21, SLA)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">The only overseas player under 22 admitted under strict auction age filters. Delivers <b class="text-white">164.6 HP SR</b> and SLA bowling control, providing dual-threat all-rounder flexibility.</p>
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
            <option value="indian">Indian Core Only (4 Players)</option>
            <option value="overseas">Overseas Targets Only (6 Players)</option>
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
                <th class="py-3 px-4 text-right">HP Wickets</th>
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
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">Death Knuckleball Closer</span>
          <h4 class="text-sm font-bold text-white mt-1">Mohit Sharma (Rank 1 Pick)</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Fixes RR's 10.76 death pace bleed. Delivers an elite <b class="text-white">8.38 HP Econ across 151 balls with 26 wickets</b>. As an Indian player, saves an overseas slot for Hope or Joseph.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">150+ km/h Strike Weapon</span>
          <h4 class="text-sm font-bold text-white mt-1">Shamar Joseph & Jofra Archer</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Consistently breaches 150 km/h with brutal bounce and toe-crushing yorkers. Option B combines both to unleash unprecedented dual express pace in the death overs.</p>
        </div>
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800/80 rounded-2xl p-5 shadow-xl">
          <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider font-mono">Frontline Specialist Spin</span>
          <h4 class="text-sm font-bold text-white mt-1">Ravi Bishnoi & Brijesh Sharma</h4>
          <p class="text-xs text-slate-300 mt-2 leading-relaxed">Uncapped prodigy Brijesh Sharma delivers <b class="text-white">7.19 HP Econ</b> across 86 balls. Pairs with Ravi Bishnoi and Jadeja to build a fortress of spin through middle and death overs.</p>
        </div>
      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 5: DELIVERY PRESSURE SIMULATOR (JUDGES TEST BENCH)         -->
    <!-- ============================================================== -->
    <div id="tab-sim" class="tab-content hidden space-y-6">
      
      <div class="bg-[#001744] border border-blue-900/60 p-6 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div>
          <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Judges Interactive Test Bench</span>
          <h2 class="text-lg font-bold text-white">Live Match Scenario Pressure Calculator</h2>
          <p class="text-xs text-slate-300 mt-0.5">Test any match scenario by adjusting the 5 leverage variables. Watch the continuous mathematical engine recalculate delivery-level Pressure Index (PI &isin; [0, 1]):</p>
        </div>
        <div class="text-xs font-mono text-pink-400 bg-pink-500/10 border border-pink-500/30 px-3 py-1.5 rounded-lg">
          PI = w1&middot;Lreq + w2&middot;Wadj + w3&middot;Dexp + w4&middot;Tstage + w5&middot;Starget
        </div>
      </div>

      <!-- Simulator Controls & Output -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

        <!-- Controls Column (Sliders) -->
        <div class="lg:col-span-2 bg-[#001744]/90 border border-blue-900/70 rounded-2xl p-6 shadow-xl space-y-5">
          
          <!-- Slider 1: Required Run Rate -->
          <div>
            <div class="flex justify-between items-center mb-1.5 text-xs font-mono">
              <span class="text-slate-200 font-bold">1. Required Run Rate (RRR):</span>
              <span class="text-pink-400 font-bold text-sm" id="val-rrr">10.5 RPO</span>
            </div>
            <input type="range" id="slider-rrr" min="4.0" max="18.0" step="0.5" value="10.5" oninput="calculatePI()" class="w-full accent-pink-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-0.5">
              <span>4.0 (Cruise)</span>
              <span>8.0 (Par)</span>
              <span>12.0 (Steep)</span>
              <span>18.0 (Extreme)</span>
            </div>
          </div>

          <!-- Slider 2: Wickets Fallen -->
          <div>
            <div class="flex justify-between items-center mb-1.5 text-xs font-mono">
              <span class="text-slate-200 font-bold">2. Wickets Fallen:</span>
              <span class="text-pink-400 font-bold text-sm" id="val-wickets">4 Wickets</span>
            </div>
            <input type="range" id="slider-wickets" min="0" max="9" step="1" value="4" oninput="calculatePI()" class="w-full accent-pink-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-0.5">
              <span>0 (Top Order Intact)</span>
              <span>4 (Middle Squeeze)</span>
              <span>7 (Tail Exposed)</span>
              <span>9 (Last Wicket)</span>
            </div>
          </div>

          <!-- Slider 3: Balls Remaining -->
          <div>
            <div class="flex justify-between items-center mb-1.5 text-xs font-mono">
              <span class="text-slate-200 font-bold">3. Balls Remaining:</span>
              <span class="text-pink-400 font-bold text-sm" id="val-balls">24 Balls (Over 16.0)</span>
            </div>
            <input type="range" id="slider-balls" min="1" max="120" step="1" value="24" oninput="calculatePI()" class="w-full accent-pink-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-0.5">
              <span>1 (Final Ball)</span>
              <span>24 (Death Overs)</span>
              <span>60 (Middle Overs)</span>
              <span>120 (Match Start)</span>
            </div>
          </div>

          <!-- Slider 4: Target Score -->
          <div>
            <div class="flex justify-between items-center mb-1.5 text-xs font-mono">
              <span class="text-slate-200 font-bold">4. Match Target Score:</span>
              <span class="text-pink-400 font-bold text-sm" id="val-target">195 Runs</span>
            </div>
            <input type="range" id="slider-target" min="120" max="250" step="5" value="195" oninput="calculatePI()" class="w-full accent-pink-500 cursor-pointer">
            <div class="flex justify-between text-[10px] text-slate-400 font-mono mt-0.5">
              <span>120 (Low Chase)</span>
              <span>175 (Par Score)</span>
              <span>210 (Massive)</span>
              <span>250 (Historic)</span>
            </div>
          </div>

          <!-- Switch 5: Tournament Stage -->
          <div>
            <div class="flex justify-between items-center mb-1.5 text-xs font-mono">
              <span class="text-slate-200 font-bold">5. Tournament Context / Stage:</span>
              <span class="text-pink-400 font-bold text-sm" id="val-stage">Playoff / Final (+0.15)</span>
            </div>
            <div class="grid grid-cols-2 gap-3">
              <button onclick="setSimStage('league')" id="btn-stage-league" class="py-2.5 rounded-xl border border-blue-800 bg-blue-950 text-slate-300 font-mono text-xs font-bold transition hover:border-blue-600">
                League Stage Match
              </button>
              <button onclick="setSimStage('playoff')" id="btn-stage-playoff" class="py-2.5 rounded-xl border border-pink-500 bg-pink-500/20 text-white font-mono text-xs font-bold transition shadow-sm shadow-pink-500/20">
                Playoff / Final / Eliminator
              </button>
            </div>
          </div>

        </div>

        <!-- Output Gauge Column -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#000d29] border border-blue-800 rounded-2xl p-6 shadow-2xl flex flex-col justify-between">
          <div>
            <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block mb-2 font-mono">Engine Real-Time Output</span>
            <h3 class="text-base font-bold text-white mb-4">Calculated Delivery Pressure</h3>

            <!-- Meter / Number -->
            <div class="p-6 rounded-2xl bg-slate-950/80 border border-blue-900/80 text-center relative overflow-hidden shadow-inner">
              <div class="text-[11px] font-mono text-slate-400 uppercase tracking-widest mb-1">Pressure Index (PI)</div>
              <div class="text-5xl font-black font-mono tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-pink-400 via-rose-300 to-amber-300" id="gauge-pi-val">0.642</div>
              <div class="mt-3 inline-block px-3 py-1 rounded-full text-xs font-bold font-mono uppercase tracking-wider" id="gauge-tier-pill">
                High Pressure Delivery
              </div>
            </div>

            <!-- Breakdown Bars -->
            <div class="mt-5 space-y-2.5 text-xs font-mono">
              <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                  <span>Required Rate Leverage (35%):</span>
                  <span class="text-pink-400 font-bold" id="bar-val-rrr">0.245</span>
                </div>
                <div class="w-full h-1.5 bg-blue-950 rounded-full overflow-hidden">
                  <div class="h-full bg-pink-500 rounded-full" id="bar-fill-rrr" style="width: 70%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                  <span>Wicket Strain Factor (25%):</span>
                  <span class="text-pink-400 font-bold" id="bar-val-wickets">0.111</span>
                </div>
                <div class="w-full h-1.5 bg-blue-950 rounded-full overflow-hidden">
                  <div class="h-full bg-purple-500 rounded-full" id="bar-fill-wickets" style="width: 44%"></div>
                </div>
              </div>

              <div>
                <div class="flex justify-between text-[11px] text-slate-300 mb-1">
                  <span>Death Exponential Leverage (20%):</span>
                  <span class="text-pink-400 font-bold" id="bar-val-balls">0.148</span>
                </div>
                <div class="w-full h-1.5 bg-blue-950 rounded-full overflow-hidden">
                  <div class="h-full bg-rose-500 rounded-full" id="bar-fill-balls" style="width: 74%"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Tactical Recommendation Card -->
          <div class="mt-5 p-3.5 rounded-xl bg-pink-950/40 border border-pink-500/30 text-xs">
            <span class="text-[10px] font-mono text-pink-300 font-bold uppercase tracking-wider block mb-1">Tactical Recommendation</span>
            <div class="text-slate-200 leading-snug" id="sim-recommendation">
              Extreme Death Leverage: Deploy <b class="text-white">Mohit Sharma</b> (knuckleball slower ball) or <b class="text-white">Jofra Archer</b> (150+ yorker). For chase: Requires <b class="text-pink-300 font-bold">Shubham Dubey</b> (173.7 HP SR).
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ============================================================== -->
    <!-- TAB 6: MATHEMATICAL ENGINE & CONSTRAINTS AUDIT                 -->
    <!-- ============================================================== -->
    <div id="tab-methodology" class="tab-content hidden space-y-6">
      
      <div class="bg-[#001744] border border-blue-900/60 p-6 rounded-2xl shadow-xl">
        <span class="text-xs font-bold text-[#ea1b86] uppercase tracking-wider block font-mono">Methodological Governance</span>
        <h2 class="text-lg font-bold text-white mb-2">Mathematical Formulation & Algorithmic Architecture</h2>
        <p class="text-xs text-slate-300 leading-relaxed">
          The continuous Pressure Index (PI) maps delivery-level leverage to [0, 1] across 199,208 deliveries. It replaces crude match-level filters with instantaneous, context-aware physics.
        </p>
      </div>

      <!-- Formulas Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Batter Formula -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800 rounded-2xl p-5 shadow-xl space-y-3 font-mono text-xs">
          <span class="text-pink-400 font-bold text-sm block">1. Pressure Batter Score (PBS)</span>
          <div class="p-3 bg-slate-950 rounded-xl border border-blue-900 text-slate-200 overflow-x-auto">
            PBS = [0.45&middot;(SR_hp / 140) + 0.35&middot;(Avg_hp / 30) + 0.20&middot;(Bdry%_hp / 0.18)] &times; Shrinkage_bat &times; Consistency_match
          </div>
          <ul class="text-[11px] text-slate-300 space-y-1 font-sans">
            <li>&bull; <b class="text-white font-mono">0.45 SR Weight:</b> Prioritizes rapid boundary clearing under scoreboard squeeze.</li>
            <li>&bull; <b class="text-white font-mono">0.35 Avg Weight:</b> Rewards wicket preservation during tight chases.</li>
            <li>&bull; <b class="text-white font-mono">0.20 Boundary Weight:</b> Specifically penalizes dot balls in death overs.</li>
          </ul>
        </div>

        <!-- Bowler Formula -->
        <div class="bg-gradient-to-br from-[#001c58] to-[#001033] border border-blue-800 rounded-2xl p-5 shadow-xl space-y-3 font-mono text-xs">
          <span class="text-emerald-400 font-bold text-sm block">2. Pressure Bowler Score (PBoS)</span>
          <div class="p-3 bg-slate-950 rounded-xl border border-blue-900 text-slate-200 overflow-x-auto">
            PBoS = [0.45&middot;(8.5 / Econ_hp) + 0.35&middot;(18 / SR_hp) + 0.20&middot;(Dot%_hp / 0.35)] &times; Shrinkage_bowl &times; Consistency_match
          </div>
          <ul class="text-[11px] text-slate-300 space-y-1 font-sans">
            <li>&bull; <b class="text-white font-mono">0.45 Econ Inversion:</b> Directly rewards sub-8.5 economy rates under extreme squeeze.</li>
            <li>&bull; <b class="text-white font-mono">0.35 Strike Rate Weight:</b> Rewards crucial breakthrough wicket-taking in death overs.</li>
            <li>&bull; <b class="text-white font-mono">0.20 Dot Ball Weight:</b> Captures pressure-building maiden/choke capabilities.</li>
          </ul>
        </div>

      </div>

      <!-- Shrinkage and Filters Audit -->
      <div class="bg-[#001744]/90 border border-blue-900/70 rounded-2xl p-6 shadow-xl space-y-4">
        <h3 class="text-sm font-bold uppercase tracking-wider text-white font-mono">Statistical Rigor & Auction Constraint Audits</h3>
        
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs font-mono">
          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-[#ea1b86] font-bold block">1. Overseas Age Filter</span>
            <p class="text-slate-300 text-[11px]">Strict exclusion of uncapped overseas players aged &ge;22. Only elite prodigies (Wellalage, 21) admitted.</p>
            <p class="text-slate-400 text-[10px]">Purged: Yasir Ali, Balbirnie, Rasooli, Humphreys.</p>
          </div>

          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-emerald-400 font-bold block">2. Proven IPL Caps</span>
            <p class="text-slate-300 text-[11px]">All veteran overseas targets possess verified IPL caps (Hope, Roy, Williamson, Wade, Abbott, Joseph).</p>
            <p class="text-slate-400 text-[10px]">Guarantees immediate auction readiness.</p>
          </div>

          <div class="bg-blue-950/60 border border-blue-900 p-4 rounded-xl space-y-2">
            <span class="text-amber-400 font-bold block">3. Empirical Bayesian Shrinkage</span>
            <p class="text-slate-300 text-[11px]">Multiplier = N_hp / (N_hp + K), with K_bat=40, K_bowl=50</p>
            <p class="text-slate-400 text-[10px]">Prevents small sample size anomalies from distorting player rankings.</p>
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
    // DATA STORE
    const battersData = [
      { rank: 1, name: "Shubham Dubey", id: 25139, tier: "Indian Core", status: "Indian Uncapped", role: "#6/#7 Power Finisher (25.3% Bdry)", baseSr: 148.6, hpSr: 173.7, hpAvg: 34.4, score: 1.7370 },
      { rank: 2, name: "Shai Hope", id: 4369, tier: "Overseas (DC)", status: "Proven IPL Anchor", role: "Master #3 Anchor (Post-Samson)", baseSr: 141.3, hpSr: 157.0, hpAvg: 59.7, score: 1.5702 },
      { rank: 3, name: "Atharwa Taide", id: 6466, tier: "Indian Core", status: "Indian Uncapped", role: "Indian #3 Anchor / Fearless Opener", baseSr: 138.3, hpSr: 149.1, hpAvg: 85.0, score: 1.4912 },
      { rank: 4, name: "Dunith Wellalage", id: 7052, tier: "Overseas (SL)", status: "Young Prodigy (<22)", role: "Fixes #7 Tail Choke (SLA All-Rounder)", baseSr: 113.4, hpSr: 164.6, hpAvg: 39.5, score: 1.9551 },
      { rank: 5, name: "Jason Roy", id: 1187, tier: "Overseas (KKR)", status: "Proven IPL Star", role: "Fearless Powerplay Enforcer Cover", baseSr: 122.4, hpSr: 173.3, hpAvg: 26.0, score: 1.0236 },
      { rank: 6, name: "Gulbadin Naib", id: 2214, tier: "Overseas (DC)", status: "Proven IPL Star", role: "Power Boundary Finisher", baseSr: 121.6, hpSr: 158.2, hpAvg: 43.5, score: 1.2090 },
      { rank: 7, name: "Lalit Yadav", id: 6671, tier: "Indian Core", status: "Indian Uncapped", role: "Indian #7 All-Round Spine & Off-Break", baseSr: 104.9, hpSr: 128.4, hpAvg: 18.7, score: 0.8384 },
      { rank: 8, name: "Kane Williamson", id: 1568, tier: "Overseas (SRH)", status: "Proven IPL Legend", role: "Classical #3 Anchor & Master Tactician", baseSr: 108.2, hpSr: 123.7, hpAvg: 47.0, score: 0.7850 },
      { rank: 9, name: "Suyash Prabhudessai", id: 8085, tier: "Indian Core", status: "Indian Uncapped", role: "Clutch Domestic 360° Finisher", baseSr: 111.5, hpSr: 122.9, hpAvg: 28.7, score: 0.5602 },
      { rank: 10, name: "Matthew Wade", id: 796, tier: "Overseas (GT)", status: "Proven IPL Closer", role: "Clutch Wicketkeeper Finisher", baseSr: 128.6, hpSr: 125.0, hpAvg: 21.0, score: 0.5401 }
    ];

    const bowlersData = [
      { rank: 1, name: "Mohit Sharma", id: 2878, tier: "Indian Core", status: "Proven IPL Closer", role: "Fixes Death Pace Bleed (26 HP Wkts)", baseEcon: 8.95, hpEcon: 8.38, hpWkts: 26, score: 2.1485 },
      { rank: 2, name: "Sean Abbott", id: 1389, tier: "Overseas (SRH)", status: "Proven IPL Pacer", role: "Death Overs Restrictor & Boundary Hitter", baseEcon: 8.98, hpEcon: 7.91, hpWkts: 15, score: 1.9472 },
      { rank: 3, name: "Brijesh Sharma", id: 67036, tier: "Indian Core", status: "Indian Uncapped", role: "Uncapped Mystery Spin (7.19 HP Econ)", baseEcon: 7.64, hpEcon: 7.19, hpWkts: 9, score: 1.6373 },
      { rank: 4, name: "Michael Bracewell", id: 6512, tier: "Overseas (RCB)", status: "Proven IPL All-Rounder", role: "Off-Spin Choke & Clutch Lower Batter", baseEcon: 7.39, hpEcon: 7.50, hpWkts: 14, score: 1.3410 },
      { rank: 5, name: "Shamar Joseph", id: 47050, tier: "Overseas (LSG)", status: "Proven IPL Express", role: "150+ km/h Raw Express Pace Weapon", baseEcon: 8.65, hpEcon: 7.42, hpWkts: 12, score: 1.2580 },
      { rank: 6, name: "Sushant Mishra", id: 7269, tier: "Indian Core", status: "Indian Uncapped (GT)", role: "Left-Arm Fast-Medium Knuckleballer", baseEcon: 8.79, hpEcon: 8.05, hpWkts: 11, score: 0.9854 },
      { rank: 7, name: "Mohammad Nabi", id: 1107, tier: "Overseas (MI)", status: "Proven IPL Veteran", role: "Powerplay / Middle Spin Controller", baseEcon: 8.48, hpEcon: 7.04, hpWkts: 9, score: 0.7249 },
      { rank: 8, name: "Tabraiz Shamsi", id: 4237, tier: "Overseas (RR)", status: "Proven IPL Spinner", role: "Attacking Wrist Spinner", baseEcon: 9.64, hpEcon: 8.40, hpWkts: 8, score: 0.5678 },
      { rank: 9, name: "Kumar Kartikeya", id: 7574, tier: "Indian Core", status: "Indian Uncapped (RR)", role: "Left-Arm Mystery Spin", baseEcon: 8.52, hpEcon: 9.72, hpWkts: 5, score: 0.4850 },
      { rank: 10, name: "Riley Meredith", id: 5940, tier: "Overseas (MI)", status: "Proven IPL Express", role: "Hit-the-Deck Express Pacer (10 Wkts)", baseEcon: 9.41, hpEcon: 8.45, hpWkts: 10, score: 0.5073 }
    ];

    // ==========================================================
    // CRICKET-ACCURATE SQUAD STATES & TACTICAL BLUEPRINTS
    // ==========================================================
    let currentScenario = 'bowl_first'; // 'bowl_first' or 'bat_first'
    let isSubExecuted = false;
    let currentCombo = 'comboA'; // 'comboA' (Tactical Anchor) or 'comboB' (Dual Express Pace)

    // ----------------------------------------------------------
    // BLUEPRINT A: TACTICAL ANCHOR (Shai Hope #3 + Mohit Knuckleballer + Archer Express)
    // ----------------------------------------------------------
    const bowlFirstPreSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target (DC)", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Ravi Bishnoi / Brijesh Sharma", type: "IND", role: "Frontline Specialist Leg-Spinner (Bowler 1: 4 Overs)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 2: 4 Overs SLA)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 3: 4 Overs)", highlight: "Starting Bowler 3", isSub: false },
      { pos: 10, name: "Mohit Sharma", type: "IND", role: "Death Knuckleball Closer (Bowler 4: 4 Overs: 8.38 HP Econ)", highlight: "Rank 1 Closer", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace Strike (Bowler 5: 4 Overs)", highlight: "Starting Bowler 5", isSub: false }
    ];

    const bowlFirstPostSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target (DC)", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey (IMPACT SUB IN)", type: "IND", role: "Death Boundary Finisher (173.7 HP SR — Replaces Bishnoi for Chase)", highlight: "🔥 IMPACT PLAYER ACTIVATED", isSub: true },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (LHB / SLA)", highlight: "Retained Core", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Dynamic All-Rounder (164.6 HP SR, Age 21)", highlight: "Rank 4 Pick", isSub: false },
      { pos: 10, name: "Mohit Sharma", type: "IND", role: "Death Knuckleball Closer (4 Overs Completed: 8.38 HP Econ)", highlight: "4 Overs Bowled", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace Strike (4 Overs Completed)", highlight: "4 Overs Bowled", isSub: false }
    ];

    const batFirstPreSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target (DC)", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Captain", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey", type: "IND", role: "Designated Death Power Finisher (173.7 HP SR across 99 balls!)", highlight: "Starting Batter #7", isSub: false },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 2: 4 Overs)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 10, name: "Mohit Sharma", type: "IND", role: "Death Knuckleball Closer (Bowler 3: 4 Overs)", highlight: "Starting Bowler 3", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace Strike (Bowler 4: 4 Overs)", highlight: "Starting Bowler 4", isSub: false }
    ];

    const batFirstPostSub_A = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Agile Outfield Fielding)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Shai Hope", type: "OS", role: "Master #3 Tactical Anchor (59.7 HP Avg, 157.0 HP SR)", highlight: "Auction Target (DC)", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Ravi Bishnoi / Brijesh Sharma (IMPACT BOWLER IN)", type: "IND", role: "Specialist Frontline Spinner (Bowler 5: 4 Overs — Replaces Dubey)", highlight: "🛡️ 5TH BOWLER ACTIVATED", isSub: true },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Frontline Bowler 1", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 2: 4 Overs)", highlight: "Frontline Bowler 2", isSub: false },
      { pos: 10, name: "Mohit Sharma", type: "IND", role: "Death Knuckleball Closer (Bowler 3: 4 Overs)", highlight: "Frontline Bowler 3", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Pace Strike (Bowler 4: 4 Overs)", highlight: "Frontline Bowler 4", isSub: false }
    ];

    // ----------------------------------------------------------
    // BLUEPRINT B: DUAL EXPRESS PACE (Atharwa Taide #3 IND Anchor + Archer & Shamar Joseph Dual 150+ km/h!)
    // ----------------------------------------------------------
    const bowlFirstPreSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Ravi Bishnoi / Brijesh Sharma", type: "IND", role: "Frontline Specialist Leg-Spinner (Bowler 1: 4 Overs)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 2: 4 Overs SLA)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 3: 4 Overs)", highlight: "Starting Bowler 3", isSub: false },
      { pos: 10, name: "Shamar Joseph", type: "OS", role: "150+ km/h Raw Express Pace Missile (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 5: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false }
    ];

    const bowlFirstPostSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey (IMPACT SUB IN)", type: "IND", role: "Death Boundary Finisher (173.7 HP SR — Replaces Bishnoi for Chase)", highlight: "🔥 IMPACT PLAYER ACTIVATED", isSub: true },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (LHB / SLA)", highlight: "Retained Core", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Dynamic All-Rounder (164.6 HP SR, Age 21)", highlight: "Rank 4 Pick", isSub: false },
      { pos: 10, name: "Shamar Joseph", type: "OS", role: "150+ km/h Raw Express Missile (4 Overs Completed)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (4 Overs Completed)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false }
    ];

    const batFirstPreSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Age 15/16 Phenom)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Captain", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Shubham Dubey", type: "IND", role: "Designated Death Power Finisher (173.7 HP SR across 99 balls!)", highlight: "Starting Batter #7", isSub: false },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Starting Bowler 1", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 2: 4 Overs)", highlight: "Starting Bowler 2", isSub: false },
      { pos: 10, name: "Shamar Joseph", type: "OS", role: "150+ km/h Raw Express Pace Missile (Bowler 3: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false }
    ];

    const batFirstPostSub_B = [
      { pos: 1, name: "Yashasvi Jaiswal", type: "IND", role: "Explosive Powerplay Opener (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 2, name: "Vaibhav Sooryavanshi", type: "IND", role: "Key Prodigy Sensation (Agile Outfield Fielding)", highlight: "Key Player of the Season", isSub: false },
      { pos: 3, name: "Atharwa Taide", type: "IND", role: "Clutch #3 Indian Anchor (85.0 HP Avg, 149.1 HP SR)", highlight: "Indian Anchor Gem", isSub: false },
      { pos: 4, name: "Riyan Parag (c)", type: "IND", role: "Middle-Overs Enforcer & Spin Option", highlight: "Captain & Core", isSub: false },
      { pos: 5, name: "Dhruv Jurel (wk)", type: "IND", role: "Designated Clutch Pressure Finisher", highlight: "Retained Core", isSub: false },
      { pos: 6, name: "Shimron Hetmyer", type: "OS", role: "Elite Death Overs Destroyer (LHB)", highlight: "Retained Core", isSub: false },
      { pos: 7, name: "Ravi Bishnoi / Brijesh Sharma (IMPACT BOWLER IN)", type: "IND", role: "Specialist Frontline Spinner (Bowler 5: 4 Overs — Replaces Dubey)", highlight: "🛡️ 5TH BOWLER ACTIVATED", isSub: true },
      { pos: 8, name: "Ravindra Jadeja", type: "IND", role: "World-Class All-Rounder (Bowler 1: 4 Overs SLA)", highlight: "Frontline Bowler 1", isSub: false },
      { pos: 9, name: "Dunith Wellalage", type: "OS", role: "Under-22 SLA All-Rounder (Bowler 2: 4 Overs)", highlight: "Frontline Bowler 2", isSub: false },
      { pos: 10, name: "Shamar Joseph", type: "OS", role: "150+ km/h Raw Express Pace Missile (Bowler 3: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false },
      { pos: 11, name: "Jofra Archer", type: "OS", role: "150+ km/h Express Spearhead (Bowler 4: 4 Overs)", highlight: "⚡ DUAL 150+ EXPRESS", isSub: false }
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
        subtitleEl.innerHTML = "<b>Tactical Anchor Blueprint:</b> Shai Hope anchors at #3 (59.7 HP Avg), Mohit Sharma executes knuckleball death overs (8.38 Econ), with Jofra Archer express strike.";
      } else {
        subtitleEl.innerHTML = "<b>Dual Express Pace Blueprint:</b> Atharwa Taide anchors at #3 (85.0 HP Avg), unleashing <b>Dual 150+ km/h pacers (Archer + Shamar Joseph in tandem)</b>!";
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
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">RR fields 5 frontline specialist bowlers delivering 20 complete overs. <b class="text-pink-300">Shubham Dubey</b> rests in the dugout.</div>
                </div>
              </div>
              <div class="bg-pink-950/50 border border-pink-700/60 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-pink-300 font-bold uppercase tracking-wider">Tactical Dugout Bench (Impact Reserve)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Shubham Dubey (Vidarbha / RR)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/40 font-mono animate-pulse">CHASE SUB READY</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">173.7 HP SR across 99 balls | 25.3% Boundary Rate. Ready to swap in at innings break!</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">7 IND + 4 OS (Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        } else {
          titleEl.innerText = "Innings 2 Lineup: Chasing Target (Shubham Dubey Activated at #7)";
          subBadgeEl.innerText = "Post-Impact Sub (Chase Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-pink-500/20 text-pink-300 border border-pink-500/30 font-mono animate-pulse";
          executeBtn.innerText = "Reset to Pre-Sub Starting XI (Bishnoi IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-pink-950/70 border border-pink-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🔥</span>
                <div>
                  <div class="text-xs font-bold text-pink-300 uppercase tracking-wider font-mono">2nd Innings — Run Chase (Firepower Activated)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Tactical substitution executed: Bowler replaced by <b class="text-white">Shubham Dubey (173.7 HP SR)</b> at #7. Batting depth stacked to #8 to ice high-pressure chases!</div>
                </div>
              </div>
              <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-slate-400 font-bold uppercase tracking-wider">Tactical Dugout Bench (Subbed Out)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Ravi Bishnoi / Brijesh Sharma</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-700/60 text-slate-300 border border-slate-600 font-mono">4 OVERS COMPLETE</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">Completed 4 overs of leg-spin in 1st Innings (7.19 HP Econ). Exits for chase batting firepower.</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">7 IND + 4 OS (Legal)</span>
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
          executeBtn.innerText = "Execute Defense Impact Sub (Bring Bishnoi IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-pink-950/70 border border-pink-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🏏</span>
                <div>
                  <div class="text-xs font-bold text-pink-300 uppercase tracking-wider font-mono">1st Innings — Batting Phase (Setting Target)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Shubham Dubey starts at #7 to provide maximum death overs boundary firepower. <b class="text-blue-300">Ravi Bishnoi / Brijesh Sharma</b> rests in the dugout.</div>
                </div>
              </div>
              <div class="bg-blue-950/50 border border-blue-700/60 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-blue-300 font-bold uppercase tracking-wider">Tactical Dugout Bench (Impact Reserve)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Ravi Bishnoi / Brijesh Sharma</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/40 font-mono animate-pulse">DEFENSE SUB READY</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">7.19 HP Econ | 24.3 HP Dot%. Ready to enter for 2nd innings to activate 5 frontline specialist bowlers!</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">7 IND + 4 OS (Legal)</span>
                  <span class="text-[9px] text-slate-400 font-mono mt-1">Rule: Ind for Ind</span>
                </div>
              </div>
            </div>
          `;
        } else {
          titleEl.innerText = currentCombo === 'comboA' ? "Innings 2 Lineup: Defending Target (5 Bowlers Active - Mohit Closer)" : "Innings 2 Lineup: Defending Target (5 Bowlers Active - Dual 150+ km/h Express)";
          subBadgeEl.innerText = "Post-Impact Sub (Defense Phase)";
          subBadgeEl.className = "text-xs px-2.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 font-mono animate-pulse";
          executeBtn.innerText = "Reset to Pre-Sub Starting XI (Dubey IN)";
          banner.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 w-full">
              <div class="bg-emerald-950/70 border border-emerald-700/80 rounded-xl p-4 flex items-start gap-3.5">
                <span class="text-2xl mt-0.5">🛡️</span>
                <div>
                  <div class="text-xs font-bold text-emerald-300 uppercase tracking-wider font-mono">2nd Innings — Defending Target (5 Bowlers Active)</div>
                  <div class="text-xs text-slate-200 mt-1 leading-relaxed">Batter replaced by <b class="text-white">Ravi Bishnoi / Brijesh Sharma</b> (7.19 HP Econ). Gives RR 5 full frontline specialist bowlers delivering 4 overs each = 20 overs!</div>
                </div>
              </div>
              <div class="bg-slate-900/80 border border-slate-700 rounded-xl p-4 flex items-start justify-between gap-3">
                <div>
                  <div class="text-[10px] font-mono text-slate-400 font-bold uppercase tracking-wider">Tactical Dugout Bench (Subbed Out)</div>
                  <div class="text-sm font-bold text-white mt-0.5 flex items-center gap-2">
                    <span>Shubham Dubey (Vidarbha / RR)</span>
                    <span class="text-[10px] px-2 py-0.5 rounded-full bg-slate-700/60 text-slate-300 border border-slate-600 font-mono">BATTING COMPLETE</span>
                  </div>
                  <div class="text-[11px] text-slate-300 mt-1">Completed death boundary hitting duty in 1st Innings (173.7 HP SR). Exits for bowling defense.</div>
                </div>
                <div class="text-right flex flex-col items-end shrink-0">
                  <span class="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/30">7 IND + 4 OS (Legal)</span>
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
            <span class="text-[9px] ${p.isSub ? (currentScenario === 'bowl_first' ? 'text-pink-300 font-extrabold animate-pulse' : 'text-emerald-300 font-extrabold animate-pulse') : (p.highlight.includes('DUAL') ? 'text-cyan-300 font-bold' : 'text-pink-400')} mt-1 font-semibold">${p.highlight}</span>
          </div>
        </div>
      `).join('');
    }

    function setMatchScenario(scenario) {
      currentScenario = scenario;
      isSubExecuted = false;
      document.getElementById('btn-scen-bowl').className = scenario === 'bowl_first' ? 'flex-1 py-2 rounded-lg font-bold bg-[#ea1b86] text-white transition' : 'flex-1 py-2 rounded-lg font-bold bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition';
      document.getElementById('btn-scen-bat').className = scenario === 'bat_first' ? 'flex-1 py-2 rounded-lg font-bold bg-[#ea1b86] text-white transition' : 'flex-1 py-2 rounded-lg font-bold bg-blue-950 text-slate-300 border border-blue-800 hover:text-white transition';
      
      const impactDesc = document.getElementById('impact-desc');
      if (scenario === 'bowl_first') {
        impactDesc.innerHTML = "Plan A: Bowling 1st (5 Frontline Bowlers start; Dubey rests on bench as Chase Impact Sub).";
      } else {
        impactDesc.innerHTML = "Plan B: Batting 1st (Dubey starts at #7 for batting depth; Bishnoi rests on bench for defense).";
      }
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
        rec.innerHTML = "High Pressure Leverage: Deploy <b class='text-white'>Mohit Sharma</b> (knuckleball slower ball) or <b class='text-white'>Jofra Archer</b> (150+ yorker). For chase: Requires <b class='text-pink-300 font-bold'>Shubham Dubey</b> (173.7 HP SR across 99 balls).";
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
