---
triggers:
  - "user asks about bull or bear market"
  - "user asks which direction to trade"
  - "user asks about 21-week EMA"
  - "user asks what regime Bitcoin is in"
  - "user asks when to flip bullish or bearish"
  - "user asks if the trend is still intact after a big move"
use_when:
  - "User needs a directional bias before placing any trade"
  - "User is unsure whether to be long or short on a multi-week horizon"
  - "User asks how Kyle decides the overall market direction"
  - "Price action is ambiguous and user wants a framework for reading macro trend state"
  - "Price is near the 21-week EMA and user wants to know which side to fade"
fails_when:
  - "User is looking for a day-trading signal — the regime model is weekly, not intraday"
  - "User wants a precise entry trigger — the regime sets bias only; entries need separate confirmation"
  - "A single candle close is treated as confirmation — multiple closes are required"
  - "Altcoins are assessed before running this on Bitcoin first — BTC regime always leads"
related:
  - "bottom-criteria.md"
  - "cycle-top-dashboard.md"
---

# Regime Model

## When to Use
- Before ANY trade is discussed — establish which regime BTC is in first
- When price is near the 21-week EMA and the user wants to know which side to fade
- When a major move has just happened and the user asks "is the trend still intact?"
- When there is disagreement between short-term and long-term signals

## Fails When
- Applied to timeframes below the daily — this is a weekly model
- A single weekly close is treated as confirmation — Kyle requires multiple closes
- Used to time entries; the regime model gives direction, not entry triggers
- Altcoins are assessed before the BTC regime is established

## Core Concept

One indicator, one question: is BTC trading above or below the 21-week EMA?

Above = bull regime. Every major dip is a buy-the-dip opportunity. Shorts are only "insurance" hedges, not core positions. Core long bias is held regardless of what the daily chart says until the weekly confirms a break.

Below = bear regime. Every bounce is a potential bull trap. Spot longs are withheld or strictly range-traded. Cash is the default. Shorts can be core positions.

"The trend is your friend till the end of the trend." — said in nearly every video from P1 through P7.

The 21-week EMA is the primary gate, not the only confirmation. When it flips, the rest of his checklist (Gaussian Channel, funding, exchange volume, stop-and-reversal indicator) determines how aggressively he repositions.

## The Bull-Regime Rule

**Never hold a core directional short while BTC is printing weekly closes above the 21-week EMA — Why:** Fighting the macro trend destroys expectancy; bear-case setups that "should work" drain capital through repeated stop-outs. Exception: short-term hedge trades at extreme resistance clusters (1-5% of portfolio), explicitly labelled "insurance, not bank."

## The Bear-Regime Rule

**Never build new spot long positions while BTC is printing multiple weekly closes below the 21-week EMA — Why:** The 21-week EMA bear signal has confirmed every major bear market in BTC history; fading it is the "catching the falling knife" mistake that wiped most retail in 2022. Exception: staggered DCA accumulation at multi-year horizontal structural levels (e.g. the $10-12k zone in 2022) is permitted as a long-term position, sized small, not as a swing trade.

## Regime Switch: Confirmation Protocol

A regime does not flip on a wick through the EMA.

- **Bear to bull:** Multiple weekly closes (minimum 2-3) above the 21-week EMA, with the EMA itself angled upward. Secondary check: Gaussian Channel turns from red to teal/green.
- **Bull to bear:** Price loses the 21-week EMA on a daily close AND the stop-and-reversal indicator on the daily flips. One weekly close below is a warning. The daily-close trigger is the action signal.

**Always wait for multiple closes to confirm a regime flip — Why:** Single-candle fakeouts above or below the EMA are common; a regime flip on one candle produces whipsaws that destroy trading capital. Exception: when the daily close breaks the EMA and the stop-and-reversal indicator fires simultaneously (as in Feb 2025), that dual confirmation is sufficient to act without waiting for additional weekly closes.

## Phase Evidence

**P1 — 2022 bear descent:** Throughout the entire drop from $47k to $17.5k Kyle refused any bullish core bias. His stated condition to flip constructive: "reclaim of key moving average and it's angled upwards." None were met. Fully cash and short-biased throughout.

**P2 — FTX capitulation (Nov-Dec 2022):** The level he cited in every single video: "$21,500 = the 21-week EMA — must reclaim to confirm trend reversal." Even when he took a tactical long at $16.6k on Dec 8 (5x isolated, stop below $16,670), he was explicit: the macro regime was still bear. That trade was a range trade, not a trend trade.

**P3 — 2023 accumulation (Aug 2023 warning):** BTC fell back below the 21-week EMA and the 200 MA on the weekly. Immediate response: "Losing the 21 EMA and 200 MA on the weekly is pretty significant." He ran short positions (ROON, BNB) and refused any bullish framing until the EMA was reclaimed. Quote: "Bitcoin is range bound and expected to continue to be so — for probably the rest of this year." (RgZWVN450Zw, Aug 21, 2023)

**P6 — The Feb 2025 one-daily-close flip:** The defining example of this rule in action. BTC had been above the 21-week EMA through the $100k+ bull run. In February 2025, price broke below on a daily close and the stop-and-reversal indicator flipped simultaneously. Kyle went to 100% cash immediately — no gradual scale-out: "I'm out. Just to be clear. I'm fully in cash." (RV5Rwzdrbpc, Feb 25, 2025). He notified the Whale Room Discord in real time. The only things remaining were low-liquidity MetaMask/Phantom meme coins that physically could not be moved fast enough.

**P7 — Feb 2026 bear declaration:** After the initial decline from the P7 ATH, the recovery attempt in January 2026 produced a dead cat. "Bitcoin Breakdown Has Just Begun" (TRjKYjIZoQ8, Feb 2, 2026): Gaussian Channel lost, 21 EMA confirmed bear on multiple closes. Public flip-to-bear declaration. Prior to this, the Jan 27 video "3 Reasons Why I Wouldn't Buy Bitcoin Yet" had already flagged the deterioration.

## Weekly vs. Daily Hierarchy

Kyle runs a two-layer system:

```
Layer        | Signal                          | Action
-------------|----------------------------------|----------------------------------------
Weekly 21EMA | Regime (bull/bear)              | Sets directional bias for all trades
Daily close  | Regime entry/exit trigger       | Triggers actual position changes
4H / 1H      | Trade confirmation              | Entry, stop placement, target
```

The weekly decides what to trade. The daily tells him when to act. The lower timeframe gives the entry. He never lets the 4H override the weekly regime.

## The Gaussian Channel Add-On

The Gaussian Channel is a secondary regime confirmation: red = downtrend, teal/green = bull-run activation. Referenced in P1 (Aug 2022, building-short video) and P7 (Gaussian lost alongside 21 EMA in Feb 2026). It functions as a confirming signal, never the primary trigger. The fingerprint describes it as: "Reclaim = bull run activation. Referenced as a high-conviction signal."

## The No-Clear-Regime State (Cash Default)

The model produces three states: bull (core longs), bear (shorts/cash), and no-clear-regime. The no-clear-regime default is cash with range extremity trades only.

"Pretty much just sitting on my hands." — repeated in P1, P3, P5.
"I'd rather be bored but not losing money." — P7.

Kyle was in majority cash during:
- May-August 2023 (regime unclear after the $28.5k spike; sold spot, went to stables)
- Post-halving April-September 2024 (bull regime intact but chop; no-trade zone between extremes)
- February 2025 (regime flipped; 100% cash)
- January-February 2026 (bear regime confirmed; majority cash)

"For those of you that have been cash heavy as I've recommended for many months now you're going to be in a phenomenal position." (NkF8Upk0X-M, Sep 2022)

Sitting in cash during ambiguity is not passivity — it is as disciplined as an active trade. "Being in a cash position can also be a trade while you wait for the next major move." (j91iGTVSUwo, Apr 2024)

## Directional Bias Drives Everything Else

The regime determination happens first, before any trade discussion. In Kyle's daily videos the structure is:

1. Run the BTC weekly EMA check (above or below? angle of EMA?)
2. Check the secondary confirms (Gaussian Channel, exchange volume trend, funding)
3. Set the bias (bull / bear / no-clear-regime)
4. Only then look at specific trade setups — which must agree with the bias

A bearish setup in a bull regime is a counter-trend trade, labelled as such, sized accordingly, and run tight. A bullish setup in a bear regime gets the same treatment. Never size a counter-trend trade as if it were a regime trade.
