---
triggers:
  - "user asks what indicators Kyle uses"
  - "user asks how Kyle reads the chart"
  - "user asks about Kyle's technical analysis method"
  - "user asks what Kyle looks at before taking a trade"
  - "user asks about confluence or confirmation signals"
  - "user asks about volume, EMA, RSI, fibs, Wyckoff"
use_when:
  - "User wants to understand which tools Kyle applies and how each drives a decision"
  - "User is asking about a specific indicator — cross-reference against his actual usage"
  - "User wants to assess whether a setup would meet Kyle's confirmation criteria"
  - "User is building a multi-timeframe analysis and wants to know what confluences matter"
fails_when:
  - "User wants fundamental analysis — Kyle deliberately avoids project fundamentals"
  - "User wants on-chain metrics beyond volume and basic flows"
  - "User is asking about altcoins only — Kyle always anchors to BTC structure first"
  - "User expects a mechanical signal system — these tools inform judgment, they don't automate it"
related:
  - "market-cycle.md"
  - "risk-management.md"
---

# TA Toolkit

## When to Use
- A user asks what chart tools Kyle uses or references
- A user wants to know how Kyle structures a trade setup from scratch
- A specific indicator comes up and you need to explain how Kyle actually applies it
- A user presents a chart and wants a Kyle-style read — run the toolkit checklist

## Fails When
- You reduce this to a list of indicator names without explaining the decision each one drives
- You apply any of these tools to altcoins before establishing Bitcoin's HTF bias
- You treat the tools as stand-alone signals — Kyle requires confluence across multiple signals before acting
- You ignore volume; if volume doesn't confirm, no other tool matters to him

## Core Concept

Kyle's analysis is a layered filter, not a checklist. He starts at the highest timeframe and works down. Each tool answers a specific question. He never enters a trade until at least three of these tools are pointing the same direction, and he states the answer to each question out loud before committing.

The hierarchy: **Trend state (21-week EMA) → Cycle phase (RSI monthly) → Structure (Wyckoff / price action) → Timing (TD Sequential) → Entry zone (fibs) → Health confirmation (volume 7-day MA).**

Everything below the 21-week EMA question is noise if the macro trend is against you. He won't go long in a bear-regime market regardless of what any other signal says.

## 1. Multi-Timeframe Structure — HTF Bias First

**What it is to him:** The absolute starting point of every analysis. He does not look at the 4-hour or daily chart until he has answered the weekly and monthly question.

**How it drives a decision:**
- Monthly chart answers: what is the structural position of this cycle?
- Weekly chart answers: what is the current trend regime?
- Daily chart answers: where is the entry trigger and stop?
- 4H / 1H: only for precise entries after the above three align.

**Never start with the lower timeframe — Why:** "If I look at the four hour first I'll convince myself a trade exists that doesn't. The weekly says no. The weekly is the boss, right?" (P1 bear, applied every phase) Exception: when re-entering at a pre-identified intraday level already marked from weekly/daily analysis, glancing at the 4H for entry candle precision is acceptable — but the HTF bias must have been established before opening the lower timeframe.

**His explicit rule from P4 (Apr 2024):** "Only trade at the extremities of the range — shorts at the Range High, longs at the range low, and nothing else in between." This is only knowable from the HTF chart.

## 2. 21-Week EMA — The Trend State Indicator

**What it is to him:** The single most-referenced indicator across all 55+ verified videos. He calls it THE trend-state indicator, not one of several. Price above on a weekly close = bull regime. Price below = bear regime. Multiple closes, not a wick.

**How it drives a decision:**
- **Sustained closes above:** He holds spot longs, does not short. Dips to the 21W EMA are buying opportunities.
- **Close below:** He goes to cash immediately, regardless of other signals. This is not gradual — he acted on the Feb 2025 flip to cash in a single daily close: "I'm fully in cash at this point in time." (RV5Rwzdrbpc, Feb 2025)
- **Reclaiming it from below:** Required as one of his mandatory conditions before flipping bullish. A wick above does not count.

**Always require multiple weekly closes above to confirm bull — Why:** "Bitcoin touching the 21 EMA and holding it for one week is not confirmation. Time reinforces a key level. I need to see it defend that level week after week." (BPcG2FLmOCQ, Sep 2022) Exception: when a first weekly close above the 21 EMA is accompanied simultaneously by the stop-and-reversal indicator flipping and a surge in exchange volume, a reduced-size initial long tranche is acceptable before the second close confirms — explicitly labelled as an early position, sized proportionally smaller than a fully confirmed regime entry.

**Bear case application (P3, Aug 2023):** "Losing the 21 EMA and 200 MA on the weekly is pretty significant." Immediately ran short trades on altcoins; refused to re-enter BTC spot.

## 3. TD Sequential 9 Count — Timing and Exhaustion

**What it is to him:** Kyle applies TD Sequential, developed by Tom DeMark, as a countdown signal for local exhaustion tops and bottoms. He counts 1 through 9 on the candles, calls it out by number live — "seven, eight, nine, local top." A 9 at resistance = caution. A 9 buy at support = long opportunity. He uses it as timing confirmation, not as a primary trend signal.

**How it drives a decision:**
- TD 9 top at resistance with bearish RSI divergence = his clearest "take partial profits" signal
- TD 9 buy in a zone he already identified as support = entry trigger is live, "no trigger no trade" condition is met
- A TD 9 against the HTF trend is ignored; a TD 9 in the direction of the HTF trend gets full weight

**Never take a TD 9 buy signal in a bear regime — Why:** The count tells you momentum is exhausted, not that the trend has reversed. In a bear market, a 9 buy is frequently the start of a relief rally that fails and makes a new low. "Seven, eight, nine, local top — that's a warning, not a license to short your entire stack." (P4 context) Exception: a TD 9 buy firing at a major multi-year structural level (prior cycle ATH, realized price, long-term trend line) in a bear regime can justify a small, tightly-stopped counter-trend long — explicitly framed as a range trade, not a trend reversal, with size well below normal allocation.

**Example (P6, ycRUFjrld8c, Aug 2025):** Referenced TD count convergence alongside RSI on the weekly when assessing whether the cycle top was forming. The 9 count had not yet materialized at the extreme level he expected — one of the reasons he held positions.

## 4. Wyckoff — Accumulation and Distribution Schematics

**What it is to him:** Kyle applies Wyckoff accumulation and distribution schematics, developed by Richard Wyckoff, as a structural map for range behavior. He identifies which Wyckoff phase the market is in — Phase B (cause building), Phase C (spring / shakeout), Phase D (sign of strength / last point of support), Phase E (markup). He names these phases by name on air.

**How it drives a decision:**
- **Spring (Phase C):** The sweep below range support that flushes weak longs. This is where he stages his most aggressive entries. "This is a Wyckoff spring — this is where you want to be buying, not selling." (voNC4i09gW4, Aug 3 2024)
- **Phase D (LPS — Last Point of Support):** High-volume confirmation candle back above the range. Entry for more conservative traders. He required the "sign of strength" before committing larger size.
- **Phase D trigger (P5, Oct 2024):** "Wyckoff Phase D; high-volume resistance at $59.5k; trigger = reclaim previous week's low." (XbI7EfFGiJ8)
- **Distribution:** He applied the inverse schematic at potential cycle tops — UTAD (Upthrust After Distribution) = liquidity grab above the range before the rollover.

**Always confirm Wyckoff phase against volume — Why:** A spring with no volume spike is not a spring, it's a breakdown. The volume must surge on the spring candle or the phase C call is invalid. He checks exchange aggregate volume charts, not just the spot chart. Exception: during exchange outages or data gaps where aggregate volume is temporarily unreliable, a clean price reclaim above the schematic boundary with a series of higher lows can tentatively confirm Phase D — but position size is reduced until volume data is restored and can be verified.

**P5 accumulation example (Jul 2024):** Framed the 139-day chop ($53k-$72k range) as a textbook Wyckoff accumulation cause: "The longer the cause, the greater the effect." Used BB contraction as corroboration.

## 5. Fibonacci — Golden Pocket and Extensions

**What it is to him:** Fibonacci is a classical mathematical tool applied widely across trading disciplines. He uses two fib tools: retracement levels for entry zones, extension levels for price targets. The golden pocket (0.618-0.65) is his primary entry cluster. He draws it from swing low to swing high on the relevant timeframe; price reclaiming the golden pocket = high-probability long zone.

**How it drives a decision:**
- **Golden pocket (0.618-0.65):** First bid zone after a pullback in a bull regime. "The golden pocket is where the smart money comes back in, right? It's the deepest retracement that still keeps the trend intact." (Applied P4 and P6)
- **0.382 and 50%:** Secondary levels, used for smaller position adds when price hasn't reached the golden pocket
- **1.618 extension:** His primary upside target. Stated explicitly: "1.618 fib target = $130,977" (nzaqGQ1inuQ, May 2025). Also used for altcoin targets.
- **Trend-based fib:** He switches to the trend-based fib tool for measuring moves within a trend channel rather than simple reversals.
- **Worst-case targets (P7):** Broadening wedge — "786-886 fib = 28-38K worst case." (NM_dn5g3Xvo, Jun 2026)

**Golden pocket + other confluence = high-conviction — Why:** He does not enter a fib level in isolation. Feb 2025: his "highest confidence bounce zone" at $83k was described as "golden pocket + daily FVG + monthly FVG confluence." The fib alone was not enough; he needed the gaps to align.

**Never use fibs without anchoring to the correct swing — Why:** "If you anchor your fib from the wrong swing you'll be waiting at the wrong level. Start from the last confirmed structural low, not from any random wick." (Implied throughout his tutorial segments) Exception: when a cycle high or low is structurally ambiguous (e.g. a double top at slightly different levels), running parallel fib sets from each candidate anchor and noting where levels cluster is valid — a price level common to both anchors carries more weight, not less, and the analysis is still grounded in the swings.

## 6. USDT Dominance — BTC Inverse Signal

**What it is to him:** A macro flow indicator. When USDT dominance rises, money is leaving crypto into stablecoins — bearish for BTC. When it falls, money is returning into risk — bullish for BTC. He tracks the 9-9.3% level as the key breakout threshold on a weekly close basis.

**How it drives a decision:**
- **USDT dominance weekly close above 9-9.3%:** Explicit bearish BTC signal. Referenced as a trigger in his bear market confirmation checklist (P1, P7).
- **USDT dominance at 3.8% triple bottom (support zone):** Local top warning. "When we hit this level, you probably want to consider taking at least some of your profits." (tyYcGhLqzlc, Jul 2025) — he framed July 25 as the likely local top date based on the rate of decline.
- **P7 (Jun 2026):** USDT dominance weekly close above 9.3% explicitly cited as one of the capitulation criteria that had fired.

**Always track USDT.D on the weekly close, not intraday — Why:** Intraday USDT dominance swings with volatility. The weekly close removes the noise. A close above 9% on the weekly is a structural regime change; a spike that closes back below is not. Exception: during extreme macro events (exchange collapse, sudden regulatory shock) monitoring USDT.D on the daily close is acceptable as a near-term de-risking trigger — any position change based on a daily reading should be confirmed by the subsequent weekly close before being treated as a full structural regime shift.

## 7. Hash Ribbons — Miner Capitulation Buy Signal

**What it is to him:** Kyle applies hash ribbons, developed by Charles Edwards, as a buy signal triggered when mining profitability collapses and the hash rate falls, then recovers. Two moving averages of hash rate cross (short over long = capitulation; then cross back = buy signal). Kyle treats the hash ribbon buy signal as a long-term accumulation indicator, not a short-term trade entry.

**How it drives a decision:**
- **Hash ribbon buy signal (blue dot) = accumulation zone for spot BTC.** Not a leveraged trade trigger.
- **P2 (Nov 2022):** "Miners Are Capitulating! | What This Means For Crypto!" — declining hash rate cited as bearish short-term but historically a buy signal 3-6 months forward.
- **P5 (Aug 5, 2024 crash):** "If the daily candle closes back inside the range above the circled area the hash ribbons blue buy signal still remains valid — and it could be a very very big bear trap." He only kept the signal live if price closed back above a specific level.
- **P6 (Aug 2025):** "Hash ribbons buy signal triggered" cited as one piece of evidence that despite seasonal weakness, the bull cycle was not over.

**Never treat a hash ribbon signal as a trade entry without price confirmation — Why:** The signal fires during the capitulation — price may still fall further. He pairs it with exchange volume (spike required), funding rates (must be negative), and price reclaiming a key level before acting. Exception: when the hash ribbon buy signal fires simultaneously with the three-condition bottom checklist (high-volume capitulation candle + sustained negative funding + momentum divergence), the combined signal is strong enough to begin the first DCA tranche without waiting for a separate price trigger, given the rare convergence of all signals at once.

## 8. Gaussian Channel

**What it is to him:** A volatility-weighted channel drawn on the weekly chart. When price is above the Gaussian channel = bull run active. When price drops below and the channel turns red = bear market confirmed. Reclaiming the Gaussian channel from below = bull run re-activation signal.

**How it drives a decision:**
- **Below channel (red):** No spot longs. "Red Gaussian channel — that is your bear market. Don't fight it." (P1 application)
- **Reclaim of channel:** One of the signals that can flip his bias from bearish to bullish.
- **P7 (Feb 2026 triage):** "Gaussian channel lost" cited alongside 21-week EMA loss as confirmation of the bear market declaration.
- **P6 (Jun 2025):** Gaussian channel timing model — "conservative cycle top September 22, 2025" derived from projecting when price would reach the Gaussian channel upper band. (EvlQfAfcsxI)

**Always check the Gaussian channel before calling a bull market — Why:** He uses it as a second opinion on the 21-week EMA. Both need to confirm. If the 21W EMA is above but the Gaussian channel is still flashing red, he stays cautious. Exception: immediately after a confirmed weekly golden cross (50 MA crossing above the 200 MA) with multiple 21 EMA reclaims already in place, the Gaussian channel's delay in turning green — it is a lagging indicator — can be accepted; the EMA reclaim plus golden cross together are sufficient to label the regime as transitioning to bull while awaiting channel confirmation.

## 9. RSI — Weekly Thresholds and Phase Identification

**What it is to him:** Two uses: (a) a cycle phase indicator on the monthly/weekly, (b) a pivot-level tracker for identifying structural shifts. He has explicit thresholds: RSI crossing 73 on monthly = Phase 3 (bull market acceleration); RSI crossing 80 = Phase 4 (parabolic / cycle peak zone).

**How it drives a decision:**
- **Monthly RSI at 73 (Phase 3):** "RSI crosses 73 — that is when Phase 3 of the bull market has begun. This is similar to when Bitcoin was trading at $10,000 in the prior cycle." (VFaHyX1SDbg, Mar 2024) — he held and increased position size.
- **Monthly RSI at 80 (Phase 4):** Parabolic zone. Meme coin profits rotated to majors. Partial de-risking advised. "I think before the monthly can cross 80 we need Bitcoin to trade up to about $130-140,000." (P6, Aug 2025)
- **Weekly RSI oversold below 20:** Structural long-term interest signal. Not a trade trigger on its own but weighs in his accumulation planning.
- **RSI bearish divergence (price new high, RSI lower high):** Caution signal on any timeframe. "Bearish RSI divergence forming on daily" cited as a warning in May 2025 (S1hJeiivZGs) that caused him to transition from investor to active trader mode.

**Always pair RSI phase calls with the monthly chart, not daily — Why:** Daily RSI divergences produce false signals constantly in a strong trend. The monthly RSI phase thresholds (73, 80) are the ones that have held across every cycle he references. Exception: daily RSI bearish divergence at a named major resistance level (prior ATH, 1.618 fib extension) is meaningful enough to trigger a shift from investor to active trader mode and begin partial profit-taking — as Kyle demonstrated in May 2025 — even before the monthly RSI crosses a threshold.

## 10. Daily Exchange Volume 7-Day MA — The Primary Health Signal

**What it is to him:** His most-cited single market health indicator. He checks it in near every video. It is the gating condition for whether a rally is sustainable. Declining volume = no sustainable rally, regardless of price action. He compares current volume levels to the 2021 peak as his reference benchmark.

**How it drives a decision:**
- **Volume above 7-day MA and expanding:** Confirms rally. "Volume is confirming the move — this is healthy." He allows larger position sizes.
- **Volume declining or below 7-day MA on a rally:** "Volume continues to diminish... it's pretty much impossible to have any sustainable rally." (P7, Jun 2026, Dec 2025) — he went or stayed short/cash.
- **P6 (Dec 2024):** "Daily exchange volume NOT at 2021 levels = not top yet." — he used this to argue the bull market had further to run.
- **P6 exit dashboard:** "Daily exchange volume needs to eclipse 2021 highs (~$150B/day MA)" was one of his 12 explicit cycle-top exit criteria.
- **P7 (Jun 2026):** "The rallies won't be sustainable without that daily exchange volume, which is still declining." — this was his explanation for staying short despite bounces.

**Never call a breakout confirmed without volume expansion — Why:** "I've seen price go up on no volume a hundred times and every single time it comes back. You need the volume, guys, right? Without the volume it's just a wick. Time reinforces key levels and volume reinforces key moves." (Composite of multiple Kyle segments) Exception: a breakout from an extremely prolonged consolidation (100+ days, Bollinger Bands at historic extremes of contraction) where price closes decisively above the range and does not immediately close back below can be treated as a tentative breakout on average volume — position sizing is reduced until the follow-through session confirms with expanding volume.

**Always use the 7-day MA, not single-day volume — Why:** Single-day spikes occur on liquidation events and news. The 7-day MA filters the noise and shows whether real demand is consistently present. Exception: a single-day volume spike that is 3x or more above the 7-day MA on a structurally critical candle (Wyckoff spring, capitulation low, key-level breakout) is itself a meaningful signal and should be noted independently — Kyle references exactly these singular spikes when discussing spring entries and hash ribbon buy confirmation; the spike does not require 7-day context to carry weight.

## 11. Bollinger Band Width Percentile — Volatility Expansion Signal

**What it is to him:** A contraction-then-expansion signal. When BB width percentile reaches historical extremes on the low end (maximum contraction), he expects an imminent large directional move. He does not use BB for entries; he uses it as a heads-up that a breakout is coming and to size up existing bias trades.

**How it drives a decision:**
- **Maximum BB contraction (P5, Jul 2024):** "This is the lowest volatility I think we've actually ever seen for Bitcoin — the absolute tightest that the Bollinger Bands have ever been — which signifies an absolute Behemoth move." (BSEgD-MNte8) — he used this to hold through the 139-day chop rather than exit.
- **BB expansion (P6, Oct 2024):** "Bollinger Band expansion targets $106k BTC, $5k ETH." — his upside targets were the upper band expansion levels.
- **No direction signal on its own:** "The Bollinger Band contraction tells me something is coming. The structure tells me which way." He defers to price structure for direction; BB only tells him magnitude is coming.

**Never fade a BB expansion move without structural reason — Why:** Expansion follows contraction, and the move tends to go further and faster than expected. He lets it run until he gets a TD 9 count or RSI divergence at a named level. Exception: at a well-identified cycle target level (1.618 fib extension, prior cycle ATH) that was named in advance before the expansion began, an expansion move arriving at that level can be faded for a partial profit-taking position — sized as a partial exit rather than a reversal bet, with the remainder of the position still running under a trailing stop.

## Reading the Toolkit Together

Kyle's decision for any given trade follows a fixed mental sequence:

1. **Regime check:** 21-week EMA + Gaussian channel. Bull or bear? This sets the default posture.
2. **Cycle phase:** Monthly RSI level. Are we in Phase 1 accumulation, Phase 3 bull, or Phase 4 parabolic? This sets position sizing aggressiveness.
3. **Structure:** Wyckoff schematic. What phase of the range or trend are we in? Is this a spring (buy zone) or UTAD (sell zone)?
4. **Health check:** Volume 7-day MA. Is the move supported by real demand?
5. **Timing:** TD Sequential count. Is momentum exhausted at this level?
6. **Entry zone:** Fibonacci golden pocket. Is price in the high-probability entry cluster?
7. **Macro flow:** USDT dominance direction. Is money flowing into or out of crypto?
8. **Trigger:** "No trigger, no trade." A specific price action confirmation is required before executing.

If steps 1-4 do not align, he waits. "I would wait. I would wait, wait, wait." The confluence is the edge.
