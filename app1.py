import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Shruti Shravani | iGaming Retention Specialist",
    page_icon="🎯",
    layout="wide"
)

# --- OPTIONAL REAL DATA (fill in only if you have the real numbers) ---
# Funnel "Before" values for [Registered, Verified, Deposit Page, First Deposit].
# Must start at 100 and end at 21, e.g. [100, 60, 38, 21]. Leave None to hide Before bars.
FUNNEL_BEFORE = None
# Reactivated-player split by RFM segment, using YOUR real segment names, e.g.
# {"Segment A": 40, "Segment B": 35, "Segment C": 25}. Leave None to hide the pie.
RFM_SHARES = None

# --- CUSTOM STYLING ---
st.markdown("""
<style>
    .metric-card { background-color:rgba(128,128,128,0.10); border:1px solid rgba(128,128,128,0.35); border-radius:10px; padding:18px; text-align:center; }
    .metric-val { font-size:26px; font-weight:800; color:#00A152; }
    .metric-lbl { font-size:13px; opacity:0.75; margin-top:4px; }
    .campaign-box { background-color:rgba(128,128,128,0.10); border-left:4px solid #E53935; padding:15px; border-radius:6px; margin-bottom:12px; color:inherit; }
    .proposal-box { background-color:rgba(128,128,128,0.10); border:1px solid rgba(128,128,128,0.35); border-top:3px solid #00A152; padding:15px; border-radius:8px; margin-bottom:14px; color:inherit; }
    .proposal-box h4 { margin-top:0; }
    .section-header { border-bottom:2px solid #E53935; padding-bottom:6px; margin-top:20px; margin-bottom:15px; }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("Shruti Shravani")
st.subheader("iGaming Retention Marketing Specialist | 4M+ User Base")
st.write(
    "I keep players active and bring lapsed ones back, using **SQL cohort analysis**, **RFM segmentation**, and "
    "**automated WebEngage journeys** (Push, WhatsApp, SMS, Email, in-app), always measured against **NGR and promo cost**."
)

# --- TOP KPI BANNER (retention first) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-val">~30% MoM</div><div class="metric-lbl">Active Retention Sustained Across a 4M+ User Base</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-val">~15% Lower</div><div class="metric-lbl">Monthly Player Churn</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-val">₹9.59 Cr</div><div class="metric-lbl">Deposits Recovered from 4,659 Dormant Paying Users</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-val">21% → 39%</div><div class="metric-lbl">Signup-to-First-Deposit Conversion (+18 pp)</div></div>', unsafe_allow_html=True)

st.markdown("---")

# --- MAIN NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Proven Retention Results",
    "🔁 My Retention Playbook",
    "💡 Proposals + First 90 Days",
    "🧮 Supporting Tool: Promo ROI Simulator"
])

# ==========================================
# TAB 1: PROVEN RESULTS
# ==========================================
with tab1:
    st.markdown('<h3 class="section-header">Proven Track Record: One Verse Gaming (formerly Quadrific Media Pvt Ltd) | 4M+ User Platform</h3>', unsafe_allow_html=True)

    row1a, row1b = st.columns(2)

    with row1a:
        st.markdown("#### 1. Sustaining Retention & Cutting Churn")
        st.info("**Result: ~30% MoM active retention, ~15% lower monthly churn**")
        st.write("**Task:** Keep a 4M+ user base active month after month.")
        st.write("**Action:** Tracked cohort stickiness across the database and deployed automated WebEngage dormancy triggers (Push, WhatsApp, SMS) to re-engage players before they lapsed fully. A/B tested journeys across Push, Email, SMS, WhatsApp and in-app banners.")
        k1, k2 = st.columns(2)
        k1.metric("Push CTR", "6.0%", delta="+50% vs 4% target")
        k2.metric("Reporting time saved", "4-5 hrs/week", delta="Power BI + SQL automation", delta_color="off")

    with row1b:
        st.markdown("#### 2. Dormant Player Reactivation")
        st.info("**Result: ₹9.59 Cr Recovered (₹20.5K+ ARPU per reactivated player)**")
        st.write("**Task:** Win back dormant paying users across a 4M+ database.")
        st.write("**Action:** Built segmented reactivation campaigns using RFM modeling, automated in SQL (CTEs, window functions), winning back 4,659 dormant paying users.")
        if RFM_SHARES:
            df_rfm = pd.DataFrame({"Segment": list(RFM_SHARES.keys()), "Share (%)": list(RFM_SHARES.values())})
            fig_r = px.pie(df_rfm, names="Segment", values="Share (%)", hole=0.45, height=230,
                           color_discrete_sequence=["#00E676", "#2196F3", "#FFC107", "#8B949E"])
            fig_r.update_layout(margin=dict(l=5, r=5, t=20, b=5))
            st.plotly_chart(fig_r, use_container_width=True)
        else:
            r1, r2, r3 = st.columns(3)
            r1.metric("Users Won Back", "4,659")
            r2.metric("Deposits Recovered", "₹9.59 Cr")
            r3.metric("ARPU", "₹20.5K+")

    row2a, row2b = st.columns(2)

    with row2a:
        st.markdown("#### 3. Onboarding Funnel Rescue")
        st.info("**Result: 21% → 39% Signup-to-First-Deposit Conversion (+18 pp)**")
        st.write("**Task:** 79% of new signups were not making a first deposit.")
        st.write("**Action:** Analysed WebEngage event logs alongside MySQL transaction data to find stage-wise drop-offs, then launched targeted lifecycle nudges.")

        stages = ["Registered", "Verified", "Deposit Page", "First Deposit"]
        after = [100, 74, 55, 39]
        if FUNNEL_BEFORE:
            df_funnel = pd.DataFrame({"Stage": stages, "Before (%)": FUNNEL_BEFORE, "After (%)": after})
            fig_f = px.bar(df_funnel, x="Stage", y=["Before (%)", "After (%)"], barmode="group",
                           height=230, color_discrete_sequence=["#8B949E", "#00E676"])
        else:
            df_funnel = pd.DataFrame({"Stage": stages, "After (%)": after})
            fig_f = px.bar(df_funnel, x="Stage", y="After (%)", height=230, color_discrete_sequence=["#00E676"])
            st.caption("Pre-campaign first-deposit conversion was 21%.")
        fig_f.update_layout(margin=dict(l=5, r=5, t=20, b=5), legend_title_text="")
        st.plotly_chart(fig_f, use_container_width=True)

    with row2b:
        st.markdown("#### 4. Protecting Revenue After a Gaming Tax Shock")
        st.info("**Result: NGR Restored to Breakeven**")
        st.write("**Task:** A new gaming tax caused an 80% drop in casual user volume and a -6.7% NGR dip.")
        st.write("**Action:** Ran P&L cohort analysis and shifted promotional spend toward high-value segments (4x revenue multiplier), restoring NGR to breakeven.")

        df_tax = pd.DataFrame({
            "Phase": ["Pre-Tax Baseline", "Immediate Tax Shock", "Post-Pivot (Breakeven)"],
            "Net Gaming Revenue Index": [100, 93.3, 100]
        })
        fig_t = px.bar(df_tax, x="Phase", y="Net Gaming Revenue Index", height=230, color="Phase",
                       color_discrete_sequence=["#8B949E", "#E53935", "#00E676"])
        fig_t.update_layout(margin=dict(l=5, r=5, t=20, b=5), showlegend=False)
        st.plotly_chart(fig_t, use_container_width=True)
        st.caption("Indexed to pre-tax NGR = 100. Shock = -6.7%; post-pivot = breakeven.")

# ==========================================
# TAB 2: MY RETENTION PLAYBOOK
# ==========================================
with tab2:
    st.markdown('<h3 class="section-header">How I Think About Retention: The Player Lifecycle</h3>', unsafe_allow_html=True)
    st.write("Retention is a chain, not one campaign. Each lifecycle stage has a trigger, a channel mix and a KPI.")

    lifecycle = pd.DataFrame({
        "Stage": ["1. Onboarding", "2. Activation", "3. Active / Engaged", "4. At-Risk", "5. Dormant", "6. Win-Back"],
        "Who": [
            "Registered, no first deposit",
            "First deposit made, not yet repeating",
            "Regular depositors and bettors",
            "Recency or frequency slipping",
            "No activity for a defined window",
            "Reactivated, needs a second session"
        ],
        "Trigger / Action": [
            "Nudge at the drop-off step (verification, deposit page)",
            "Guide to a 2nd and 3rd session; show product value",
            "Fixture-based and personalised content; reward loyalty without overspending",
            "Early-warning dormancy trigger before they fully lapse",
            "RFM-segmented reactivation; offer matched to segment value",
            "Follow-up journey so the return sticks"
        ],
        "Channels": [
            "Push, WhatsApp, SMS", "Push, in-app, Email", "Push, in-app, WhatsApp",
            "Push, WhatsApp, SMS", "WhatsApp, SMS, Email", "Push, in-app"
        ],
        "KPI": [
            "Signup to FTD %", "FTD to repeat deposit %", "MoM active retention",
            "At-risk to active recovery %", "Reactivation rate, ARPU", "30-day post-return retention"
        ]
    })
    st.dataframe(lifecycle, use_container_width=True, hide_index=True)

    st.markdown('<h3 class="section-header">How I Measure It: Cohort Retention in SQL</h3>', unsafe_allow_html=True)
    st.caption("Simplified example on a hypothetical schema. Cohort = month of first deposit; active = made a deposit that month.")

    cohort_sql = """WITH cohorts AS (
    SELECT user_id,
           DATE_FORMAT(MIN(txn_date), '%Y-%m-01') AS cohort_month
    FROM deposits
    GROUP BY user_id
),
activity AS (
    SELECT DISTINCT user_id,
           DATE_FORMAT(txn_date, '%Y-%m-01') AS active_month
    FROM deposits
),
grouped AS (
    SELECT c.cohort_month,
           TIMESTAMPDIFF(MONTH, c.cohort_month, a.active_month) AS months_since_first,
           COUNT(DISTINCT a.user_id) AS active_users
    FROM cohorts c
    JOIN activity a ON a.user_id = c.user_id
    GROUP BY c.cohort_month, months_since_first
)
SELECT cohort_month,
       months_since_first,
       active_users,
       ROUND(100 * active_users /
             FIRST_VALUE(active_users) OVER (PARTITION BY cohort_month
                                             ORDER BY months_since_first), 1) AS retention_pct
FROM grouped
ORDER BY cohort_month, months_since_first;"""
    st.code(cohort_sql, language="sql")

    st.markdown('<h3 class="section-header">How I Segment: RFM Lifecycle Scoring in SQL</h3>', unsafe_allow_html=True)
    st.caption("Simplified example on a hypothetical schema. Offer tier is then chosen per segment and tested against cost.")

    rfm_sql = """WITH user_metrics AS (
    SELECT user_id,
           DATEDIFF(CURRENT_DATE, MAX(txn_date)) AS recency_days,
           COUNT(DISTINCT txn_date)              AS frequency,
           SUM(deposit_amount)                   AS monetary
    FROM deposits
    WHERE txn_date >= DATE_SUB(CURRENT_DATE, INTERVAL 180 DAY)
    GROUP BY user_id
),
scored AS (
    SELECT user_id, recency_days, frequency, monetary,
           NTILE(5) OVER (ORDER BY recency_days DESC) AS r_score,  -- 5 = most recent
           NTILE(5) OVER (ORDER BY frequency)         AS f_score,
           NTILE(5) OVER (ORDER BY monetary)          AS m_score
    FROM user_metrics
)
SELECT user_id, r_score, f_score, m_score,
       CASE WHEN r_score >= 4 THEN 'Active'
            WHEN r_score = 3  THEN 'Cooling Off'
            ELSE 'Dormant' END AS lifecycle_stage
FROM scored;"""
    st.code(rfm_sql, language="sql")

    st.markdown('<h3 class="section-header">Why Churn Reduction Compounds (Illustrative Model)</h3>', unsafe_allow_html=True)
    st.write("A small cut in monthly churn leaves far more players active over time. Adjust the inputs to see the effect on one cohort.")

    c_in, c_out = st.columns([1, 1.5])
    with c_in:
        base_users = st.slider("Starting active players", 10000, 500000, 100000, step=10000)
        base_churn = st.slider("Baseline monthly churn (%)", 5, 40, 20, step=1)
        churn_cut = st.slider("Relative churn reduction (%)", 0, 40, 15, step=1,
                              help="Your resume result: ~15% reduction in monthly churn")
        arpu_m = st.number_input("Monthly revenue per active player (any currency)", min_value=0, value=500, step=50)
        months = st.slider("Months to project", 3, 24, 12)

    new_churn = base_churn * (1 - churn_cut / 100)
    m_axis = list(range(0, months + 1))
    base_curve = [base_users * ((1 - base_churn / 100) ** m) for m in m_axis]
    new_curve = [base_users * ((1 - new_churn / 100) ** m) for m in m_axis]
    extra_players = new_curve[-1] - base_curve[-1]
    extra_rev = sum((n - b) * arpu_m for n, b in zip(new_curve[1:], base_curve[1:]))

    with c_out:
        fig_c = go.Figure()
        fig_c.add_trace(go.Scatter(x=m_axis, y=base_curve, name=f"Baseline churn {base_churn:.1f}%", line=dict(color="#8B949E")))
        fig_c.add_trace(go.Scatter(x=m_axis, y=new_curve, name=f"Improved churn {new_churn:.1f}%", line=dict(color="#00E676")))
        fig_c.update_layout(height=280, margin=dict(l=10, r=10, t=30, b=10),
                            xaxis_title="Months", yaxis_title="Active players from this cohort")
        st.plotly_chart(fig_c, use_container_width=True)
        o1, o2 = st.columns(2)
        o1.metric(f"Extra players active at month {months}", f"{extra_players:,.0f}")
        o2.metric("Extra revenue over the period", f"{extra_rev:,.0f}")
    st.caption("Illustrative only: a simple single-cohort decay model with no new signups, reactivation or seasonality. Inputs are assumptions, not company data.")

# ==========================================
# TAB 3: PROPOSALS + FIRST 90 DAYS
# ==========================================
with tab3:
    st.markdown('<h3 class="section-header">Retention Proposals for a Younger, Mobile-First Player Base</h3>', unsafe_allow_html=True)
    st.write(
        "These are **ideas I would test, not systems I have already run.** Each has a success metric, a guardrail metric, "
        "and a safer-play check built in."
    )
    st.info("**Design principle:** 18+ only and licence-compliant. Retention should come from entertainment, status and community, never from chasing losses.")

    p1, p2 = st.columns(2)
    with p1:
        st.markdown("""
<div class="proposal-box">
<h4>1. Matchday Squads (Social Layer)</h4>
<b>Idea:</b> Free-to-play prediction leagues where verified players compete with friends on match outcomes, with leaderboards and shareable stat cards. Rewards are badges and status, not cash.<br><br>
<b>Why it fits Gen Z:</b> Social, mobile-first and shareable; cheap to run compared with deposit bonuses.<br><br>
<b>Success metric:</b> D30 retention and sessions per week vs. a control group.<br>
<b>Guardrail:</b> No promo cost per user; 18+ verified accounts only.
</div>
""", unsafe_allow_html=True)
    with p2:
        st.markdown("""
<div class="proposal-box">
<h4>2. "Season Wrapped" with Built-In Reality Check</h4>
<b>Idea:</b> A personalised, shareable recap (favourite leagues, best calls, active days) that also shows time and spend honestly, with one-tap access to limits and breaks.<br><br>
<b>Why it fits Gen Z:</b> The "Wrapped" format is familiar and shareable, and transparency builds trust.<br><br>
<b>Success metric:</b> Open rate, share rate, and limit-tool adoption.<br>
<b>Guardrail:</b> Spend shown plainly, never framed as a win.
</div>
""", unsafe_allow_html=True)

    p3, p4 = st.columns(2)
    with p3:
        st.markdown("""
<div class="proposal-box">
<h4>3. Bonus-Elasticity Matrix</h4>
<b>Problem:</b> Flat deposit bonuses overpay organic users who would bet anyway, and attract promo-driven players who churn.<br>
<b>Approach:</b> Score users weekly on predicted LTV vs. promo sensitivity (share of historical deposits made without a promo code), then tier them:<br>
• <b>Organic high-value:</b> no bonus; retain via speed, support and personalised content.<br>
• <b>Promo-sensitive regulars:</b> margin-protected boosters on multi-leg bets.<br>
• <b>Negative-NGR promo hunters:</b> suppress automated promo triggers.<br><br>
<b>Success metric:</b> NGR per unit of promo spend.<br>
<b>Guardrail:</b> Retention of organic high-value players must not drop.
</div>
""", unsafe_allow_html=True)
    with p4:
        st.markdown("""
<div class="proposal-box">
<h4>4. Post-Result Moment Engine (Safer-Play Gated)</h4>
<b>Idea:</b> Use bet-settlement events to send timely, useful messages after a match, such as a recap, the next fixture to watch, or a free prediction game. <b>No offers are triggered by a loss.</b><br><br>
<b>Safety gate first:</b> Exclude self-excluded and cooling-off players, anyone with limit hits or at-risk behaviour flags, and cap message frequency.<br><br>
<b>Success metric:</b> Next-session rate within 48 hours.<br>
<b>Guardrail:</b> Zero messages to excluded players; no increase in late-night or rapid-deposit patterns.
</div>
""", unsafe_allow_html=True)

    st.caption("All proposals would be A/B tested with a holdout group before rollout, in line with each market's licence and responsible-gambling rules.")

    st.markdown('<h3 class="section-header">What I Would Do in My First 90 Days</h3>', unsafe_allow_html=True)
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown("#### Days 1-30: Learn & Diagnose")
        st.markdown("""
* Learn each market's players, payment methods and channel behaviour
* Build baseline cohort retention and churn curves by market
* Audit current journeys, segments and promo spend
* Map where players drop off: onboarding, repeat deposit, dormancy
""")
    with d2:
        st.markdown("#### Days 31-60: Test")
        st.markdown("""
* Run RFM and promo-sensitivity segmentation
* Launch 2-3 A/B tests with holdout groups (for example, a no-bonus journey vs. the current one)
* Agree guardrail metrics with Compliance and Responsible Gambling
""")
    with d3:
        st.markdown("#### Days 61-90: Scale What Works")
        st.markdown("""
* Roll out winning journeys, retire weak promos
* Automate retention reporting in Power BI
* Share results and a next-quarter roadmap with stakeholders
""")

# ==========================================
# TAB 4: SUPPORTING TOOL - ROI SIMULATOR
# ==========================================
with tab4:
    st.markdown('<h3 class="section-header">Promo & Retention ROI Simulator (Illustrative)</h3>', unsafe_allow_html=True)
    st.write("A thinking tool for comparing promo spend across segments. Defaults are **illustrative assumptions, not real company data.**")

    sim_col1, sim_col2 = st.columns([1, 1.4])

    with sim_col1:
        currency = st.selectbox("Select Market Currency", ["USD ($)", "NGN (₦)", "ZAR (R)", "INR (₹)"])
        curr_sym = currency.split("(")[1].replace(")", "")
        mult = 1500 if "NGN" in currency else (18 if "ZAR" in currency else (84 if "INR" in currency else 1))

        segment = st.selectbox(
            "Select Target Player Segment",
            [
                "Bonus-Sensitive Regular (High Elasticity)",
                "Organic VIP (Low Elasticity / High LTV)",
                "Lapsed Player (Safer-Play Gated Win-Back)"
            ]
        )

        if "Organic VIP" in segment:
            def_users, def_dep, def_bonus, def_win = 5000, 150 * mult, 0, 42
        elif "Lapsed" in segment:
            def_users, def_dep, def_bonus, def_win = 15000, 35 * mult, 3 * mult, 28
        else:
            def_users, def_dep, def_bonus, def_win = 25000, 50 * mult, 8 * mult, 22

        cohort_size = st.slider("Targeted Cohort Size (Users)", 1000, 100000, def_users, step=1000)
        avg_deposit = st.slider(f"Avg. Monthly Deposit per User ({curr_sym})", 10 * mult, 500 * mult, def_dep, step=5 * mult)
        bonus_cost = st.slider(f"Promo / Free-Bet Cost per User ({curr_sym})", 0, 50 * mult, def_bonus, step=1 * mult)
        winback_rate = st.slider("Expected Retention / Win-Back Rate (%)", 5, 70, def_win, step=1)
        house_margin = st.slider("Sportsbook Hold / GGR Margin (%)", 5, 20, 11, step=1)

    retained_users = int(cohort_size * (winback_rate / 100))
    total_deposits = retained_users * avg_deposit
    ggr = total_deposits * (house_margin / 100)
    total_promo_cost = retained_users * bonus_cost
    ngr = ggr - total_promo_cost
    roi = ((ngr / total_promo_cost) * 100) if total_promo_cost > 0 else float('inf')

    net_rev_per_user = (avg_deposit * (house_margin / 100)) - bonus_cost
    breakeven_status = "Profitable" if net_rev_per_user > 0 else "-Negative Margin (Reduce Bonus)"

    with sim_col2:
        m1, m2, m3 = st.columns(3)
        m1.metric("Retained / Active Users", f"{retained_users:,}")
        m2.metric("Approx. GGR", f"{curr_sym}{ggr:,.0f}")
        m3.metric("Total Promo Spend", f"{curr_sym}{total_promo_cost:,.0f}")

        m4, m5, m6 = st.columns(3)
        m4.metric("Approx. NGR", f"{curr_sym}{ngr:,.0f}", delta=breakeven_status)
        m5.metric("Net Promo ROI", "∞ (Zero Bonus)" if total_promo_cost == 0 else f"{roi:,.1f}%")
        m6.metric("Net Margin per Retained User", f"{curr_sym}{net_rev_per_user:,.2f}")

        st.caption("Approximation: GGR is modelled as deposits × hold %. In practice, hold applies to turnover (stakes), so treat these figures as directional.")

        rates = list(range(5, 65, 5))
        ngr_curve = [
            (int(cohort_size * (r / 100)) * avg_deposit * (house_margin / 100)) - (int(cohort_size * (r / 100)) * bonus_cost)
            for r in rates
        ]
        df_sim = pd.DataFrame({"Retention / Win-Back Rate (%)": rates, f"Projected NGR ({curr_sym})": ngr_curve})
        fig_sim = px.area(df_sim, x="Retention / Win-Back Rate (%)", y=f"Projected NGR ({curr_sym})",
                          title="Projected NGR Sensitivity Across Retention Rates (approx.)",
                          color_discrete_sequence=["#00E676"])
        fig_sim.add_vline(x=winback_rate, line_dash="dash", line_color="#E53935", annotation_text="Current Target")
        fig_sim.update_layout(height=260, margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_sim, use_container_width=True)

        export_df = pd.DataFrame([{
            "Segment": segment, "Currency": currency, "Cohort_Size": cohort_size,
            "Retained_Users": retained_users, "Avg_Deposit": avg_deposit, "Bonus_Cost": bonus_cost,
            "Approx_GGR": round(ggr, 2), "Total_Promo_Spend": round(total_promo_cost, 2),
            "Approx_NGR": round(ngr, 2),
            "Promo_ROI_Pct": "Infinite" if total_promo_cost == 0 else round(roi, 1)
        }])
        st.download_button("📥 Download Simulation Scenario (CSV)",
                           data=export_df.to_csv(index=False).encode("utf-8"),
                           file_name="retention_simulation.csv", mime="text/csv")

    st.markdown("#### Sample Journey Copy for the Selected Segment")
    if "Organic VIP" in segment:
        st.markdown("""
        <div class="campaign-box">
        <b>Strategy:</b> Zero-bonus margin protection (retain via status and speed, not cash giveaways)<br>
        <b>Push (30 mins before kickoff):</b> "Kickoff in 30 mins. Your priority settlement and early cash-out are active for tonight's matches."<br>
        <b>WhatsApp:</b> "Hi [Name], your personalised match sheet for tonight is ready. Tap to view."
        </div>
        """, unsafe_allow_html=True)
    elif "Lapsed" in segment:
        st.markdown(f"""
        <div class="campaign-box">
        <b>Strategy:</b> Win-back only for players who pass the safer-play check (not self-excluded, no at-risk flags, within frequency cap)<br>
        <b>Push:</b> "Big fixtures this weekend. Join your Matchday Squad and make your free predictions."<br>
        <b>Optional low-cost booster ({curr_sym}{3*mult:,}):</b> Offered only to eligible lapsed players, never triggered by a loss.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="campaign-box">
        <b>Strategy:</b> Margin-protected odds booster (requires a 3+ leg multi-bet to protect sportsbook hold)<br>
        <b>WhatsApp / SMS (Friday 5 PM):</b> "Weekend Matchday Boost: deposit {curr_sym}{50*mult:,}+ today and unlock a 15% odds booster on any 3+ leg football accumulator. 18+. Play responsibly."<br>
        <b>Follow-up Push (Saturday 12 PM):</b> "Kickoff in 90 mins! Your weekend booster is waiting."
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Built by Shruti Shravani | Contact: choudharyshruti333@gmail.com | Mumbai, India")