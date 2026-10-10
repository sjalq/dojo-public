---
triggers:
  - "user asks which timeframe to trade"
  - "user mixes 1m entries with weekly bias incorrectly"
  - "user asks what counts as higher timeframe"
  - "user wants multi-TF confirmation rules"
use_when:
  - "building any trade: HTF direction + LTF confirmation"
  - "mapping confirmation pairs (weekly/daily, daily/4h, 4h/15m, 1h/5m)"
  - "stopping traders from using 1m noise to confirm a weekly idea"
fails_when:
  - "user treats one fixed chart as always 'the' HTF for every strategy"
  - "confirmation TF is so far below trade TF that noise dominates"
related:
  - "fifty-percent-retrace.md"
  - "market-structure-shift.md"
  - "htf-order-block-entry.md"
  - "follow-market-structure.md"
---

# Timeframe Hierarchy

## When to Use
- Any new trade plan that needs direction vs entry split
- Educating traders who think "higher timeframe" only means weekly
- Choosing confirmation chart relative to the chart that defines the trend

## Fails When
- Confirmation jumps too many octaves (weekly trend, 1m entry) without intermediate structure
- User flips the hierarchy: lets 1m dictate the daily story
- No trend TF is chosen, so every chart is "confirmation"

## Core Concept

A higher timeframe does not have to mean the weekly chart. Anything can be higher timeframe relative to something else. What matters is how timeframes relate inside **your** strategy.

Relevant stack he names: weekly, daily, 4-hour, 1-hour, 15-minute, 5-minute, 1-minute. That set is enough to trade.

Split of labor:

- **Higher TF:** identify the trend you are trading.
- **Lower TF:** identify confirmation for entry.

Example confirmation pairs from his whiteboard teaching:

- Weekly trend → daily confirmation
- Daily trend → 4-hour confirmation
- 4-hour trend → 15-minute confirmation
- 1-hour trend → 5-minute confirmation
- Below that → 1-minute confirmation

If daily trend is up and price tags 50%, drop to 4h for a market structure shift / higher high after the mid tag, then enter with stop under that LTF structure so risk-reward is not garbage. A naked daily entry at mid can work but often has worse RR than LTF confirmation.

Scalpers can treat 4h as their "higher" TF and take 15m MSS confirmation. The rule is constant: every trade needs HTF direction plus LTF confirmation. Do not confirm a weekly idea with a 1-minute flicker; too much can happen in between.

## How to Apply

1. **Choose the trend TF first.** Write it down: "I am trading the daily uptrend" (or 4h, etc.).
2. **Choose the confirmation TF from the pair table**, not from boredom.
3. **Read trend only on the trend TF:** HH/HL or LH/LL, magnets, 50% of that TF's impulse.
4. **Arm entry only after trend TF condition** (e.g. mid tag) **and** confirmation TF shift.
5. **Place stop from confirmation structure**, target from trend structure when possible.
6. **Refuse mismatched pairs.** Weekly bias + 1m entry without intermediate plan is noise gambling.

## Examples

**Situation:** Trader has little time, wants one clean swing. Daily is clearly uptrending HH/HL.

**Application:** Wait daily 50% tag. Confirm on 4h MSS / higher high. Enter, stop under 4h structure, ride daily continuation.

**Illustrative result:** Small LTF risk, HTF payoff path.

**Situation:** Scalper sees 4h downtrend into hourly supply.

**Application:** 4h is HTF for them. 15m AMD/MSS short confirmation. Do not need weekly narrative to take the scalp, but do not claim the weekly flipped.

**Situation:** User says weekly is bullish so they market-long on 1m green candles.

**Application:** Reject. Wrong confirmation distance. Use daily or 4h at least as the bridge.

## Anti-Patterns (tactical)

**Don't:** Call every chart you open "confirmation."

**Why:** Without a declared trend TF, hierarchy collapses.

**Don't:** Use 1m to confirm weekly.

**Why:** Too many paths between them; false confidence.

**Don't:** Change trend TF mid-trade to avoid admitting you are wrong.

**Why:** That is goalpost moving, not multi-TF analysis.
