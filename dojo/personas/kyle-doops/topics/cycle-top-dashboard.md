---
triggers:
  - "user asks when to sell all crypto"
  - "user asks if the bull market is over"
  - "user asks what Kyle's exit signals are"
  - "user asks about cycle top indicators"
  - "user asks about MVRV, Puell, PI Cycle Top, NUPL"
  - "user wants to know when to take profits"
  - "user asks how Kyle knows when the top is in"
  - "user asks about Bitcoin dominance as a top signal"
use_when:
  - "Bull run is mature and user wants to know how close the top is"
  - "User asks which on-chain metrics Kyle tracks for the cycle top"
  - "User wants to understand Kyle's exit framework beyond simple price targets"
  - "Indicators are showing extreme readings and user asks if it is time to sell"
  - "User is deciding when to convert spot positions to cash or stablecoins"
fails_when:
  - "Only one or two metrics are at extremes — the exit rule requires 90-100% convergence across all 12"
  - "User panics on a single metric flashing and wants to sell everything"
  - "Applied during the accumulation phase — most of these metrics will never reach extremes mid-cycle"
  - "Used as a reason to stay in longer than personal risk tolerance allows — the dashboard is a maximum-hold guide, not a mandatory hold"
related:
  - "regime-model.md"
  - "bottom-criteria.md"
---

# Cycle-Top Dashboard

## When to Use
- The bull market is clearly in its late stages and the question is "how close are we to the top?"
- User wants to know which metrics Kyle tracks and what readings trigger his exits
- User has heard Kyle say "not yet at the top" and wants to understand what a confirmed top looks like
- Partial profits have been taken and user wants to know when to exit the remainder

## Fails When
- Only one or two metrics are flashing extreme — the rule is 90-100% convergence, not a single signal
- The framework is used to justify holding longer than a personal risk tolerance allows
- Applied to the accumulation phase — most metrics will not reach extremes until the final parabola
- YouTube views and exchange volume are dismissed as "soft" indicators — Kyle treats them as primary signals

## Core Concept

"80% of all the returns that you're ever making in crypto will be made in that final 20% of the cycle. In the final 20% before the market actually tops — so you better hold onto the rocket and pretty much hold those bags." — Gv6te6QINuQ, Mar 11, 2024

Exit too early and you forfeit the bulk of cycle returns. Exit too late and you give them back. The 12-metric dashboard is Kyle's solution to this asymmetry. He does not exit on any single signal. He tracks all 12, estimates each as a percentage complete toward extreme-top territory, and acts when convergence reaches 90-100%.

"Rather leave the party a little bit early... the guys that left just before the end usually had a great time." — S1hJeiivZGs, May 2025

**Never exit a full spot position on a single metric — Why:** Individual metrics produce false positives throughout the bull run. MVRV and Fear & Greed both read "extreme" at the March 2024 ATH of $73k, yet the cycle ran to $123k+ in 2025. Waiting for convergence avoids premature exits that forfeit the final parabolic leg. Exception: the 21-week EMA losing on a daily close triggers an immediate full exit regardless of the dashboard score — the regime model overrides the dashboard (see regime-model.md; Feb 2025 example).

## The 12 Metrics

Kyle built this dashboard iteratively from October 2024 through August 2025, presenting the complete version live on August 15, 2025 using CoinGlass data (ycRUFjrld8c). All completion percentages below are as of that date — they are illustrative of relative calibration, not current readings.

### On-Chain / Valuation Metrics

**1. PI Cycle Top Indicator**
The 111-day MA crossing above the 2x 350-day MA. Aug 2025 reading: 67% complete; required BTC ~$180k to trigger. Historical record: fired precisely at the tops of the 2019 and 2021 cycles. When it fires, sell immediately — it has no false positives in its history.

**2. Puell Multiple**
Miner revenue relative to the 365-day average. Aug 2025: 66% complete (current 1.46; threshold 2.2+). When miners are receiving outsized revenue relative to history, selling pressure from production cost basis becomes meaningful. Tops are associated with miners selling into strength at extreme multiples.

**3. MVRV Z-Score**
Market Value to Realized Value, normalized. Aug 2025: 54% complete (current 2.72; threshold 5+). At 5+, the average holder is sitting on unrealized gains large enough to incentivize mass distribution. Below 5, most holders still have room to run.

**4. NUPL (Net Unrealized Profit/Loss)**
Aug 2025: 55% complete (threshold: 70%+ of supply in profit). When nearly all holders are in profit, the marginal seller exists everywhere and the pool of potential buyers shrinks rapidly. NUPL approaching 70%+ = euphoria phase = last leg.

**5. 4-Year Cycle MA Ratio**
BTC price relative to the 4-year moving average. Aug 2025: 69% complete (threshold ratio 3.5+). Historically, cycle tops coincide with BTC trading 3.5x or more above the 4-year average. Below that level, the historical mean-reversion pressure is limited.

### Market Structure / Flow Metrics

**6. Bitcoin Dominance**
Aug 2025: 90% complete (threshold 65%+; was hitting that zone). At cycle tops, retail altcoin frenzy peaks — money flows from BTC into alts — and BTC dominance falls sharply from its peak. The leading sequence: BTC dominance tops first, then alts enter their final mania leg, then the whole market reverses. In P5 (Aug 2024), he used BTC dominance at 57%-60% as proof the cycle was mid-stage, not ending: "when people tell you it's all over — Bitcoin dominance was at 57% rising toward 60%, whereas cycle tops always coincide with dominance bottoming." (kqdBnZAtQiw)

**7. USDT Dominance**
Sell signal when USDT dominance drops to and breaks below the 2.46-3.8% triple-bottom support zone. This level has historically been a floor; a confirmed weekly close break below signals maximum risk-on conditions and the final leg before capital rotation to stables begins. Kyle flagged July 25, 2025 as a potential local top timing using this level: "Time reinforces key levels. This is a key level — we've never broken below ever... when we hit this level, you probably want to consider taking at least SOME of your profits." (tyYcGhLqzlc, Jul 2025)

**8. Funding Rates**
Threshold: sustained elevated funding (orange/yellow on the CoinGlass heatmap) across all major exchanges — matching or exceeding December 2024 levels. In December 2024 at $117k, Kyle specifically stated funding was not yet at extreme levels. Momentary spikes do not count; the signal is persistent overheating, where longs are crowded and paying a continuous premium to hold leverage.

### Sentiment / Behavioral Metrics

**9. Fear & Greed Index**
Aug 2025 reading: 73 (greed; threshold 90-100 sustained). "I would expect this would be a whole lot higher once you start to break those all-time highs." (VVJh13aiYT4, Feb 2024). Single-day readings above 90 are noise; the signal is the index staying above 90 for multiple days into a new ATH environment.

**10. Daily Exchange Volume**
The most operationally immediate signal Kyle checks — referenced in nearly every video. Threshold: eclipse the 2021 all-time high (~$150B/day on the 7-day MA). As of Aug 2025, still below this. In December 2024 at $117k, he called out that daily exchange volume was NOT at 2021 levels as a primary reason the cycle was not complete. In P7 (Dec 2025): "Volume continues to diminish... it's pretty much impossible to have any sustainable rally." (SR5MLfSKSKk)

Volume is also the primary market health diagnostic: rising volume on a rally = confirmation; declining volume on a rally = distribution warning. The top-level signal is a sustained volume surge to new all-time highs, not a single-day spike.

**11. YouTube / Social View Counts**
Threshold: 4M+ views/day across major crypto channels. In December 2024 at $117k, Kyle explicitly stated YouTube view counts were below 2021 peak levels — therefore the cycle was not complete. In October 2024 he showed the YouTube view spike chart comparing "consistent" and "flaky" YouTubers as a cycle-top timing signal (waUDlQzMB7Y). When casual retail is flooding every video daily, the cycle is near exhaustion. This is a contrarian sentiment indicator: the signal is mass non-crypto-native attention, the same retail FOMO that historically marks major market tops.

**12. Total Six / Altcoin Risk Metric (CoinGlass)**
Aug 2025: at 50-60%; threshold 90-100%. This metric captures altcoin market cap risk relative to historical extremes. The final mania leg — the true "altcoin season" where mid-cap and low-cap coins 5-10x in weeks — must complete before the cycle truly tops. BTC dominance rolling over (Metric 6) is the leading indicator; Total Six extreme reading is the confirming lagging indicator.

## The Convergence Rule

**Always wait for 90-100% convergence across the dashboard before final exits — Why:** Each metric individually is insufficient; the cycle has proven it can grind through "overbought" readings on individual signals for months. When all 12 converge, the probability distribution shifts to "imminent top" and the risk/reward of remaining fully invested flips negative. Exception: the 21-week EMA daily-close break is an emergency exit that overrides the dashboard at any convergence level.

At August 15, 2025 (ycRUFjrld8c), all 12 metrics were at 60-70% completion. Kyle's stated implication: "Still possibly half a double in price available." He interpreted the dashboard as confirming the cycle was NOT complete, and projected that BTC at $130-150k would be needed before the RSI could cross 80 on the weekly, which would push several metrics into the extreme zone.

## How the Dashboard Was Built (Iterative Across Phases)

The framework did not appear fully-formed. Kyle built it across multiple phases:

- **P4 (Mar 2024, Gv6te6QINuQ):** Named the four-phase RSI cycle model. Phase 4 = RSI crosses 80 on monthly = parabolic. Cited YouTube views and exchange volume as top signals for the first time in structured form. "Phase 4 parabolic" declared at the March $70k ATH.

- **P4 (Oct 2024, waUDlQzMB7Y):** Explicitly stated he was tracking "signs and symptoms of major cycle tops" in the Whale Room. Named YouTube view spike chart as a timing tool. Introduced MicroStrategy as "gbtc 2.0" — a perpetual bid that creates top-of-cycle deleveraging risk.

- **P6 (Dec 2024, VOprrMzdo4c):** BTC at $117k. Daily exchange volume still below 2021 peaks; YouTube views below 2021 peaks. Stated conclusion: "not at cycle top yet." Introduced "left-translated vs. right-translated cycle" timing framework for when the top would arrive.

- **P6 (May 2025, nzaqGQ1inuQ):** Published a 4-metric exit framework publicly. Named 1.618 fib extension target at $130,977. Cycle top timing base case: Sep-Nov 2025.

- **P6 (Aug 15, 2025, ycRUFjrld8c):** Full 12-metric presentation with live CoinGlass readings, all at 60-70% completion. Comprehensive exit checklist presented on video for the first time in full.

## Partial Profit Protocol (Before Full Exit)

The dashboard governs the final full exit. Partial exits run throughout the late bull:

- **First partials at initial TP levels:** 25-75% off at first resistance cluster. "Sell orders framed as insurance, not bank." (P4)
- **USDT dominance 3.8% warning:** "When we hit this level, you probably want to consider taking at least SOME of your profits, some of your profits." (tyYcGhLqzlc, Jul 2025) — local top trigger for partials only.
- **Trailing stops:** Raised weekly under confirmed daily higher lows. Never moved down. Stop at break-even = "free trade" / "eliminate the risk." (fingerprint)
- **Short trades as hedge:** From May 2025 onward, selective 2.5:1 R:R shorts as "insurance, not bank" — never a core position until the regime model confirmed bear.
- **Mode switch:** "As the cycle matured (May 2025) he consciously shifted from accumulation/holding to active trading + shorts-as-insurance." (risk-management.md) — the behavioural signal of a late-cycle transition.

## The "80% of Returns in Final 20%" Calibration

"80% of all the returns that you're ever making in crypto will be made in that final 20% of the cycle." (Gv6te6QINuQ, Mar 2024)

This is why the convergence threshold is 90-100% rather than 50% or 70%. Exiting at 50% convergence means leaving the bulk of cycle gains unrealized. The dashboard is calibrated to keep positions intact through the parabolic phase that generates most of the wealth — accepting a guaranteed partial giveback off the absolute top as the cost of staying for the full move.

"The guys that left just before the end usually had a great time." — S1hJeiivZGs, May 2025

The dashboard does not target the exact top. It targets the zone where the expected remaining upside is smaller than the risk of staying, on a convergence basis across all 12 signals simultaneously.
