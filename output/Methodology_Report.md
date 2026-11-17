# SupeRR Selector Season 2: Round 1 Methodology Report
## Identifying Pressure-Resilient Cricketers for Rajasthan Royals (IPL 2027)
### Quota-Aware Tactical Optimization & Roster Architecture Following Official Retentions (Featuring Mohd. Shami)

---

### Executive Summary

In T20 franchise cricket, championships are won in the margins of extreme leverage. Following the official release of **Rajasthan Royals' Retained Squad for TATA IPL 2027 (19 Players)**, the franchise enters the upcoming IPL 2027 Auction from a position of unprecedented bowling strength, headlined by the sensational acquisition of premier Indian strike pacer **Mohd. Shami** alongside speed merchant **Jofra Archer** and death-overs maestro **Sandeep Sharma**.

With 19 players locked in (14 Indian, 5 Overseas), RR holds **6 open auction slots** (with up to **3 overseas positions** available under the BCCI 8-overseas squad ceiling). Crucially, **IPL matchday regulations permit at most 4 overseas players in any Playing XI**, mandating that at least **7 players must be Indian**.

Our empirical analysis on the official 199,208 ball-by-ball dataset (843 matches across IPL, BBL, PSL, CPL, SA20, and T20Is) reveals:
1. **The Bowling Transformation**: The presence of **Mohd. Shami** (Purple Cap pedigree, world-class seam presentation, powerplay swing and death reverse-yorkers) paired with **Jofra Archer** (150+ km/h express pace) and **Sandeep Sharma** (wide knuckleballs and slower balls) completely neutralizes RR’s historical death-overs bleed.
2. **The #1 Tactical Void — The #3 Anchor (Post-Sanju Samson Void)**: With explosive prodigies **Yashasvi Jaiswal** and **Vaibhav Sooryavanshi** opening the innings, RR possesses unmatched early boundary potential but faces high volatility. With Sanju Samson departing, RR’s singular tactical imperative at the auction is securing a proven, ice-cool **#3 Anchor**:
   - **Option A (Overseas Master Anchor)**: **Shai Hope** (157.0 HP Strike Rate, 59.7 HP Average under high pressure) — proven in IPL and international chases.
   - **Option B (Indian Uncapped Anchor)**: **Atharwa Taide** (149.1 HP Strike Rate, 85.0 HP Average under high pressure) — frees up an overseas slot for dual express pace or all-round hitting.
3. **Auction Depth & Squad Insurance**: With **Shubham Dubey**, **Brijesh Sharma**, and **Sushant Mishra** confirmed on RR's retained roster, the auction targets pivot cleanly toward tactical depth: **Mohit Sharma** (veteran Indian death pace backup), **Sean Abbott** (hard-length pace all-rounder batting at #8), **Michael Bracewell** (off-spin choke vs LHB), and **Shamar Joseph** (150+ km/h backup for Archer).

---

### 1. Rajasthan Royals Official Retained Squad (TATA IPL 2027)

The official retention graphic confirms **19 players retained by Rajasthan Royals**:

```
+----------------------------------------------------------------------------------------------------+
|                         RAJASTHAN ROYALS RETAINED SQUAD (TATA IPL 2027)                            |
+----------------------+---------------------------+-------------------------------------------------+
| Category             | Players Retained          | Tactical Role & Asset Class                     |
+----------------------+---------------------------+-------------------------------------------------+
| Indian Top-Order     | Yashasvi Jaiswal          | LHB Aggressive Powerplay Opener                 |
|                      | Vaibhav Sooryavanshi      | LHB Young Prodigy & Boundary Enforcer           |
|                      | Aman Rao Perala           | RHB Domestic Top-Order Talent                   |
+----------------------+---------------------------+-------------------------------------------------+
| Middle-Order /       | Riyan Parag               | RHB Captain & Middle-Overs Spin Enforcer        |
| Finishers            | Dhruv Jurel               | RHB Designated Clutch Finisher & Wicketkeeper   |
|                      | Shubham Dubey             | LHB Death-Overs Boundary Finisher (Retained!)   |
|                      | Yash Raj Punja            | RHB Domestic Power Talent                       |
|                      | Donovan Ferreira ✈        | RHB Explosive Overseas Finisher & Spin          |
|                      | Lhuan-dre Pretorius ✈     | LHB Dynamic Top-Order Wicketkeeper              |
+----------------------+---------------------------+-------------------------------------------------+
| All-Rounders         | Ravindra Jadeja           | LHB + SLA World-Class All-Round Spine           |
|                      | Dasun Shanaka ✈           | RHB + RAM Seam-Bowling All-Rounder              |
+----------------------+---------------------------+-------------------------------------------------+
| Pace Attack          | Mohd. Shami               | Premier Indian Strike Pacer (Purple Cap Winner) |
|                      | Jofra Archer ✈            | 150+ km/h Express Strike Pace                   |
|                      | Sandeep Sharma            | Death Knuckleball & Slower Yorker Specialist    |
|                      | Nandre Burger ✈           | 145+ km/h Left-Arm Express Pacer                |
|                      | Sushant Mishra            | Left-Arm Seam Domestic Depth                    |
+----------------------+---------------------------+-------------------------------------------------+
| Spin Attack          | Ravi Bishnoi              | Elite Leg-Spin & Googly Specialist              |
|                      | Manimaran Siddharth (T)*  | Left-Arm Orthodox Spinner (Player Trade)        |
|                      | Brijesh Sharma            | Right-Arm Off-Break Domestic Spinner            |
+----------------------+---------------------------+-------------------------------------------------+
```
*Note: Squad capacity allows 25 players maximum (6 open auction slots). Retained overseas count is 5 (Archer, Burger, Ferreira, Pretorius, Shanaka), leaving 3 overseas slots open for the auction.*

---

### 2. Squad Diagnostic Audit: Strategic Impact of Mohd. Shami

Prior to Shami's acquisition, RR struggled with death-over leakage (averaging 10.82 RPO in Phase 3) whenever Sandeep Sharma was unavailable. Mohd. Shami’s arrival fundamentally transforms RR’s bowling metrics:

```
+----------------------------------------------------------------------------------------------------+
|                                 SQUAD GAP & TACTICAL REALIGNMENT                                    |
+-----------------------------+------------------------------------+---------------------------------+
| Phase / Department          | Squad Status Post-Retentions       | Auction Strategic Directives    |
+-----------------------------+------------------------------------+---------------------------------+
| Phase 1: Powerplay (Overs 1-6) | Shami + Archer + Sandeep form an   | Low urgency; target swing depth |
|                             | impenetrable seam attack.          | (FazalHaq Farooqi / Abbott).    |
+-----------------------------+------------------------------------+---------------------------------+
| Phase 2: Middle (Overs 7-15)| Ravi Bishnoi + Ravindra Jadeja +   | Target off-spin all-rounder     |
|                             | M. Siddharth + Riyan Parag.        | (Michael Bracewell / Nabi).     |
+-----------------------------+------------------------------------+---------------------------------+
| Phase 3: Death (Overs 16-20)| Shami (yorkers) + Archer (150k) +  | Add veteran depth (Mohit Sharma)|
|                             | Sandeep (knuckleballs). ELITE!     | to manage workload & injury risk|
+-----------------------------+------------------------------------+---------------------------------+
| Batting Top-Order (#1 - #3) | Jaiswal & Sooryavanshi are violent | **TOP AUCTION PRIORITY #1**:    |
|                             | openers; #3 anchor is EMPTY!       | Buy **Shai Hope** or **Taide**! |
+-----------------------------+------------------------------------+---------------------------------+
| Lower-Order Hitting (#6-#8) | Jurel + Jadeja + Shubham Dubey     | Add all-round hitting depth     |
|                             | provide solid Indian spine.        | (Sean Abbott / Dunith Wellalage)|
+-----------------------------+------------------------------------+---------------------------------+
```

---

### 3. Continuous Pressure Index ($\text{PI}$) Formulation

To evaluate auction targets objectively under match leverage, we formulated a continuous, delivery-level **Pressure Index ($\text{PI} \in [0, 1]$)** calculated ball-by-ball across 199,208 deliveries:

$$\text{PI} = 0.15 \cdot F_{\text{phase}} + 0.20 \cdot F_{\text{wickets}} + 0.25 \cdot F_{\text{runrate}} + 0.15 \cdot F_{\text{stage}} + 0.25 \cdot F_{\text{closeness}}$$

Where:
1. **Match Phase ($F_{\text{phase}}$)**: Powerplay (overs 1–6) = $0.20$, Middle overs (7–15) = $0.50$, Death overs (16–20) = $1.00$.
2. **Wickets Exhaustion ($F_{\text{wickets}}$)**: $F_{\text{wickets}} = \frac{W_{\text{lost}}}{9} \in [0, 1]$.
3. **Run Rate Urgency ($F_{\text{runrate}}$)**:
   - *Chasing (Innings 2)*: $F_{\text{runrate}} = \text{clip}\left(\frac{\text{RRR} - 6.0}{14.0 - 6.0}, 0, 1\right)$
   - *Setting Target (Innings 1)*: $F_{\text{runrate}} = \text{clip}\left(\frac{\text{CRR} - 6.0}{12.0 - 6.0}, 0, 1\right)$
4. **Tournament Stakes ($F_{\text{stage}}$)**: Knockouts, playoffs, and finals = $1.00$; league stage = $0.40$.
5. **Score Closeness ($F_{\text{closeness}}$)**: In Innings 2, distance between runs required and balls remaining; in Innings 1, projected score deviation from venue par ($170$).

**Distribution Thresholds**:
- **Low Pressure**: $\text{PI} < 0.322$ (40.0% of deliveries)
- **Medium Pressure**: $0.322 \le \text{PI} < 0.494$ (36.2% of deliveries)
- **High Pressure (HP)**: $\text{PI} \ge 0.494$ (Top 23.8% highest leverage; 47,446 deliveries)

---

### 4. Performance Scoring, Shrinkage & Consistency Calibration

#### 4.1 Dimensional Uplift Metrics
We compare performance under High Pressure ($\text{PI} \ge 0.494$) against overall career baselines:
- **Batters (Pressure Batting Score)**:
  $$\text{PBS} = 0.30 \cdot z(\Delta\text{SR}) + 0.20 \cdot z(\Delta\text{Avg}) + 0.20 \cdot z(\Delta\text{Bdry}\%) + 0.15 \cdot z(\Delta\text{Dot}\%) + 0.15 \cdot z(\Delta\text{Impact})$$
- **Bowlers (Pressure Bowling Score)**:
  $$\text{PBoS} = 0.30 \cdot z(\Delta\text{Econ}) + 0.25 \cdot z(\Delta\text{SR}) + 0.20 \cdot z(\Delta\text{Dot}\%) + 0.15 \cdot z(\Delta\text{Bdry}\%) + 0.10 \cdot z(\Delta\text{Extras}\%)$$

#### 4.2 Empirical Bayesian Shrinkage
To prevent small-sample noise, raw uplifts are regressed toward population means:
$$\text{Factor}_{\text{Bayes}} = \frac{N_{\text{hp}}}{N_{\text{hp}} + K}$$
Where $K_{\text{bat}} = 40$ balls faced and $K_{\text{bowl}} = 50$ balls bowled.

#### 4.3 Match Consistency Multiplier
To reward clutch dependability over erratic performance:
$$\text{Multiplier}_{\text{consistency}} = 0.75 + \frac{0.25}{1 + \text{CV}_{\text{match}}}$$

---

### 5. Deliverable 1: Top 10 Auction Target Batters (Excluding RR Retentions)

All 10 targets are strictly eligible for the IPL 2027 auction, eliminating retained players (such as Shubham Dubey) and non-viable candidates:

| Rank | Player Name | Player ID | Quota / Status | Strategic RR Role | Base SR | HP SR | Base Avg | HP Avg | PBS Final |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **Shai Hope** | `4369` | **Overseas** (IPL: DC) | **Master #3 Anchor (Post-Samson Void)**: 157.0 HP SR, extraordinary 59.7 HP Avg. | 141.3 | **157.0** | 33.5 | **59.7** | **1.5702** |
| **2** | **Atharwa Taide** | `6466` | **Indian Core** (PBKS) | **Indian #3 Anchor / Fearless Opener**: 149.1 HP SR, 85.0 HP Avg! Saves an overseas slot. | 138.3 | **149.1** | 28.9 | **85.0** | **1.4912** |
| **3** | **Dunith Wellalage** | `7052` | **Overseas** (SL / <22) | **All-Round Prodigy**: 164.6 HP SR, 39.5 HP Avg; SLA bowler & lower-order hitter. | 113.4 | **164.6** | 17.9 | 39.5 | **1.9551** |
| **4** | **Jason Roy** | `1187` | **Overseas** (IPL: KKR) | **Powerplay Boundary Enforcer Cover**: 173.3 HP SR; violent strokeplay vs pace. | 122.4 | **173.3** | 25.8 | 26.0 | **1.0236** |
| **5** | **Gulbadin Naib** | `2214` | **Overseas** (IPL: DC) | **Power Finisher & Seam All-Rounder**: 158.2 HP SR, 43.5 HP Avg in death overs. | 121.6 | **158.2** | 21.6 | 43.5 | **1.2090** |
| **6** | **Lalit Yadav** | `6671` | **Indian Core** (DC) | **Indian #7 Spine & Off-Break**: 128.4 HP SR; provides tactical spin/bat balance. | 104.9 | **128.4** | 18.2 | 18.7 | **0.8384** |
| **7** | **Vijay Shankar** | `2877` | **Indian Core** (GT) | **Experienced Middle-Order Pace All-Rounder**: 151.0 HP SR, 29.0 HP Avg under pressure. | 128.6 | **151.0** | 26.1 | 29.0 | **0.6113** |
| **8** | **Kane Williamson** | `1568` | **Overseas** (IPL: SRH/GT) | **Classical #3 Anchor & Tactical Mind**: 123.7 HP SR, 47.0 HP Avg; calm chase architect. | 108.2 | **123.7** | 29.5 | 47.0 | **0.7850** |
| **9** | **Suyash Prabhudessai** | `8085` | **Indian Core** (RCB) | **Clutch Domestic 360° Finisher**: 122.9 HP SR, 28.7 HP Avg; domestic finishing cover. | 111.5 | **122.9** | 14.0 | 28.7 | **0.5602** |
| **10** | **Matthew Wade** | `796` | **Overseas** (IPL: GT) | **Left-Handed Clutch Finisher/WK**: 150.9 HP SR, 61.5 HP Avg; proven playoff finisher. | 132.7 | **150.9** | 32.9 | 61.5 | **0.5789** |

---

### 6. Deliverable 2: Top 10 Auction Target Bowlers (Excluding RR Retentions)

All retained RR bowlers (Brijesh Sharma, Sushant Mishra, Sandeep Sharma, Shami) are excluded, focusing purely on high-yield auction targets:

| Rank | Player Name | Player ID | Quota / Status | Strategic Bowling Fit | Base Econ | HP Econ | HP Wkts | PBoS Final |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | **Mohit Sharma** | `2878` | **Indian Core** (GT) | **Death Knuckleball IQ (Workload Cover for Shami/Sandeep)**: 8.38 HP Econ, 26 HP Wkts. | 9.67 | **8.38** | **26** | **0.7179** |
| **2** | **Sean Abbott** | `1389` | **Overseas** (IPL: SRH) | **Hard-Length Pace All-Rounder**: Drops econ to 7.89 (8 HP wkts); bats down to #8. | 9.96 | **7.89** | 8 | **0.8695** |
| **3** | **Michael Bracewell** | `6512` | **Overseas** (IPL: RCB) | **Off-Spin Choker (vs LHB)**: Drops econ to 6.39 HP Econ with 10 HP wkts. | 8.08 | **6.39** | 10 | **0.7750** |
| **4** | **Shamar Joseph** | `47050` | **Overseas** (IPL: LSG) | **150+ km/h Express Pace Backup**: Direct reinforcement for Jofra Archer (8.84 HP Econ). | 10.31 | **8.84** | 12 | **0.5973** |
| **5** | **Mohammad Nabi** | `1107` | **Overseas** (IPL: SRH/MI) | **Powerplay/Middle Spin Controller**: 7.04 HP Econ across 186 pressure balls. | 8.48 | **7.04** | 9 | **0.7249** |
| **6** | **Tabraiz Shamsi** | `4237` | **Overseas** (IPL: RR) | **Attacking Wrist Spinner**: 8.40 HP Econ (8 HP Wkts); wicket-taking backup for Bishnoi. | 9.64 | **8.40** | 8 | **0.5678** |
| **7** | **Riley Meredith** | `5940` | **Overseas** (IPL: MI) | **Hit-the-Deck Express Pacer**: 10 HP Wkts at 8.45 HP Econ; rapid raw pace. | 9.41 | **8.45** | 10 | **0.5073** |
| **8** | **FazalHaq Farooqi** | `7240` | **Overseas** (IPL: SRH) | **Left-Arm Swing & Death Yorker Cover**: 7.74 HP Econ (12 HP Wkts); cover for Nandre Burger. | 8.42 | **7.74** | 12 | **0.3352** |
| **9** | **Matthew Humphreys** | `22471` | **Overseas** (Emerging) | **Slow Left-Arm Orthodox Choke**: 5.00 HP Econ, 10 HP Wkts; exceptional control. | 7.22 | **5.00** | 10 | **0.8855** |
| **10** | **Kumar Kartikeya Singh** | `7574` | **Indian Core** (MI) | **Left-Arm Mystery Spin**: 5 HP Wickets in high-pressure middle overs. | 8.77 | **10.13** | 5 | **0.4850** |

---

### 7. Rajasthan Royals Reconstructed Matchday Playing XI (IPL 2027)

#### 7.1 Option A: Classical Anchor Masterclass (Featuring Mohd. Shami)

```
====================================================================================================
           RAJASTHAN ROYALS MATCHDAY COMBINATION A: ANCHOR BALANCE + SHAMI PACE TRIUMVIRATE
           STRICT COMPLIANCE: 9 INDIAN PLAYERS + ONLY 2 OVERSEAS PLAYERS (HUGE QUOTA CUSHION!)
====================================================================================================
AUTHENTIC BATTING ORDER (1 TO 11):
 1. Yashasvi Jaiswal          [INDIAN 1]   (LHB / Aggressive Powerplay Opener - Retained)
 2. Vaibhav Sooryavanshi      [INDIAN 2]   (LHB / Teenage Phenom & Powerplay Boundary Striker - Retained)
 3. Shai Hope                 [OVERSEAS 1] (RHB / Master #3 Anchor - 157.0 HP SR, 59.7 HP Avg) [AUCTION #1]
 4. Riyan Parag (c)           [INDIAN 3]   (RHB / Captain, Middle-Overs Spin Destroyer - Retained)
 5. Dhruv Jurel (wk)          [INDIAN 4]   (RHB / Designated Clutch Pressure Finisher - Retained)
 6. Ravindra Jadeja           [INDIAN 5]   (LHB + SLA / World-Class All-Rounder & Match Controller - Retained)
 7. Shubham Dubey             [INDIAN 6]   (LHB / Power Finisher - Retained Domestic Core)
 8. Mohd. Shami               [INDIAN 7]   (RHB + RMF / Premier Strike Bowler - Upright Seam & Death Reverse)
 9. Jofra Archer              [OVERSEAS 2] (RHB + RAF / 150+ km/h Express Strike Pace - Retained)
10. Ravi Bishnoi              [INDIAN 8]   (RHB + Leg-Spin / Middle-Overs Wicket-Taking Wizard - Retained)
11. Sandeep Sharma            [INDIAN 9]   (RHB + RMF / Master of Death Knuckleballs & Wide Cutters - Retained)
----------------------------------------------------------------------------------------------------
TACTICAL IMPACT SUBSTITUTIONS (100% Rule Compliant):
 • Bowling 1st: Sandeep Sharma starts in the bowling XI -> Subbed out for Shubham Dubey (or Donovan Ferreira ✈)
                during the 2nd innings run-chase!
 • Batting 1st: Shubham Dubey bats at #7 -> Subbed out for Sandeep Sharma to bowl death overs!
====================================================================================================
```

#### 7.2 Option B: Dual Express Pace Firepower (Indian Anchor + 150+ km/h Double-Thunder)

Deploying **Atharwa Taide** at #3 allows RR to field **TWO Express Overseas Fast Bowlers** simultaneously:
1. **Yashasvi Jaiswal** (LHB, Retained Indian)
2. **Vaibhav Sooryavanshi** (LHB, Retained Indian)
3. **Atharwa Taide** (LHB, Auction Target #2 — 149.1 HP SR, 85.0 HP Avg, PBKS)
4. **Riyan Parag (c)** (RHB, Retained Indian)
5. **Dhruv Jurel (wk)** (RHB, Retained Indian)
6. **Ravindra Jadeja** (LHB + SLA, Retained Indian)
7. **Shubham Dubey** (LHB, Retained Indian)
8. **Mohd. Shami** (RMF, Premier Indian Strike Bowler)
9. **Jofra Archer** ✈ (RAF, 150+ km/h Express Pace — Retained)
10. **Nandre Burger / Shamar Joseph** ✈ (LAF/RAF, 145–150+ km/h Express Pace — Retained/Auction)
11. **Ravi Bishnoi** (Leg-spin, Retained Indian)
*Impact Player*: **Sandeep Sharma** subbed in for Shubham Dubey when defending totals.
*Overseas Count*: Exactly 2 Overseas (Archer ✈ + Burger/Joseph ✈), well within the 4-overseas limit!

---

### 8. Conclusion: The Championship Blueprint

With **Mohd. Shami** joining **Jofra Archer**, **Sandeep Sharma**, **Ravi Bishnoi**, and **Ravindra Jadeja**, Rajasthan Royals possess what is analytically the most formidable and versatile 20-over bowling unit in T20 cricket. By acquiring **Shai Hope** or **Atharwa Taide** at the auction to solve the #3 anchor void, RR completes a flawless, championship-caliber roster ready to dominate TATA IPL 2027.
