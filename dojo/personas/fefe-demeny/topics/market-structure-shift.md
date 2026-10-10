---
triggers:
  - "user asks what MSS or MSB means"
  - "user asks when structure flipped bullish or bearish"
  - "user is waiting for confirmation before long or short"
  - "user confuses a wick with a structure break"
use_when:
  - "defining trend change on the timeframe you are trading"
  - "choosing between 15m MSS long vs 4h break short"
  - "confirming HTF regime (daily close below previous low as final nail)"
fails_when:
  - "user labels every wick beyond a swing as MSS without a close"
  - "user mixes timeframes (1m noise as if it were daily MSS)"
  - "user enters before the shift prints because the narrative feels done"
related:
  - "four-point-structure.md"
  - "fifty-percent-retrace.md"
  - "timeframe-hierarchy.md"
  - "wick-vs-close.md"
  - "follow-market-structure.md"
---

# Market Structure Shift (MSS) + Market Structure Break (MSB)

## Attribution
MSS / MSB language is ICT / Smart Money Concepts adjacent for swing structure and breaks. Fefe's operational definitions below are from his own posts and teaching: closes relative to previous highs/lows, multi-timeframe use, and coupling to 50% and 4-point confirmation. Credit the broader SMC lineage; do not present the acronyms as exclusive invention.

## When to Use
- You need a yes/no on whether structure on **this** timeframe flipped
- Choosing patience: "I am waiting for either a 4h break to short or a 15m mss to long"
- HTF regime calls: daily close below previous low as major bearish MSS
- As the confirmation leg inside 50% and 4-point models

## Fails When
- You call MSS on a wick through a level without a candle close
- You treat a 1m flip as if it rewrote the daily
- You ignore that MSS is timeframe-local: 15m MSS long can coexist with waiting for 4h break short depending on plan
- You use MSS as permission to skip risk math

## Core Concept

**Market structure shift (MSS)** is the first structural evidence that the active swing pattern on a timeframe has changed. Operational examples from his usage:

- Bearish MSS: close below the previous low (on the TF you care about). On daily, a close below the previous low is a major regime signal ("final nail").
- Bullish MSS: structure that creates a higher-high shift after a down leg on that TF (often discussed as the 15m higher high in discount for longs).

**Market structure break (MSB)** is the follow-through break after a retrace. Explicit bullish definition from his chart work: **close above previous 1H high after a 50% retrace**. Labels on charts appear as lowercase "mss" / "msb" on horizontals and swing points.

Multi-timeframe use is intentional:

- 15m MSS for longs/scalps and LTF confirmation
- 4h break as a short trigger in some regimes
- Daily/weekly MSS for major calls (BTC, TOTAL, SPX)

MSS answers: did structure on this TF actually flip? It does not answer position size. It does not override a higher-timeframe trend unless you have decided that higher TF is your trade TF.

## How to Apply

1. **Pick the trade timeframe.** Scalp confirmation, intraday swing, or HTF regime. Do not mix labels across TFs without saying so.
2. **Mark the relevant swing high and swing low.** Structure is previous high / previous low on that TF.
3. **Require closes.** Close below previous low = bearish shift candidate. Close above previous high = bullish break candidate. Wick alone = liquidity hunt risk, not automatic MSS.
4. **State the directional wait.** Example patience line: wait for 4h break to short **or** 15m MSS to long. Humility is waiting for one of the two, not inventing a third mid-chop entry.
5. **Couple to mid-range when reversing.** After MSS, plan 50% retrace then look for MSB / continuation confirmation (see 4-point structure).
6. **HTF nails.** For major bearish calls, daily close below previous low is the structure event; narrative hopium does not cancel it.

## Examples

**Situation:** Trader wants to long a bounce while daily is making lower lows and just closed below the prior daily low.

**Application:** Name the daily MSS. Job is follow structure lower or wait for a real HTF reclaim, not catch a knife because timeline hopium. LTF longs, if any, are scalps against HTF with tight invalidation, not "bottom is in" size.

**Illustrative result:** HTF MSS keeps bias honest when feelings want the low.

**Situation:** After a 50% retrace, price closes above the previous 1h high.

**Application:** That is MSB language in his posts. Mark it. It feeds 4-point confirmation when sequenced with prior MSS + mid retrace.

**Illustrative result:** Clear trigger for trend-change confidence without needing a macro story.

**Situation:** "I am humble. I am waiting for either a 4h break to short or a 15m mss to long."

**Application:** Build the plan as a binary wait. No third entry from boredom. If neither prints, flat is a position.

## Anti-Patterns (tactical)

**Don't:** Call MSS on a wick that did not close beyond the swing.

**Why:** He treats closes as confirmation and wicks as possible liquidity events. Blurring them invents fake shifts.

**Don't:** Use a 15m MSS to declare the weekly trend permanently reversed.

**Why:** MSS is local to the TF. Hierarchy still matters.

**Don't:** Keep trading mid-range "because structure will shift soon."

**Why:** The edge is waiting for the shift or the HTF break, not anticipating it with full size.
