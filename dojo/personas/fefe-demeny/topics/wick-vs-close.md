---
triggers:
  - "user treats a wick beyond a low/high as structure break"
  - "user asks what confirms a level is strong"
  - "user is confused by liquidity hunts vs real breaks"
  - "user wants entry rules around swing points"
use_when:
  - "validating MSS/MSB candidates"
  - "judging whether a level has 'massive strength'"
  - "filtering fake breaks during news or stop runs"
fails_when:
  - "user waits for perfect closes and misses that some models use acceptance over multiple candles"
  - "user ignores HTF context and only counts LTF closes"
related:
  - "market-structure-shift.md"
  - "liquidity-retail-traps.md"
  - "four-point-structure.md"
  - "fifty-percent-retrace.md"
---

# Wick vs Close Confirmation

## When to Use
- A swing was pierced and you need to know if structure actually changed
- Teaching why a level is "valid" or has "massive strength"
- Separating liquidity hunts from MSS/MSB

## Fails When
- Applied robotically on illiquid alts where wicks are meaningless noise
- User demands closes on every TF simultaneously and never acts
- Close is cherry-picked on a tiny TF to invent an HTF event

## Core Concept

For a market structure shift to count, you need to see a **close** beyond the previous swing, not merely a wick. If price only wicks below the previous low, that can be a liquidity hunt and "doesn't matter" as a structure confirmation. If you get a candle **close** below that low, the level has a massive amount of strength as a structural event: the break is real on that timeframe.

Same logic upward for breaks above highs: MSB language is about **closes** above previous highs after the right retrace context, not spikes that fail.

This pairs with liquidity traps: manipulation can wick through a level to run stops and reverse. Distribution confirmation wants the close back / close against, not the emotional high of the wick.

## How to Apply

1. **Mark the swing.** Previous low or high on the TF you claim.
2. **On pierce, wait for the candle to finish.** No early label mid-candle if your plan is close-based.
3. **Wick only → liquidity hunt bias.** Do not promote it to MSS yet.
4. **Close beyond → structure event.** Update MSS/MSB labels and plans.
5. **Grade level strength.** Closes through a level that then holds as support/resistance on retest upgrade the level's importance for later magnets.
6. **Align TF.** A 15m close is a 15m event. Promote to daily only on daily close.

## Examples

**Situation:** 15m in discount needs a bullish MSS. Price wicks above a prior high but closes back below.

**Application:** Not the shift yet. Keep waiting for a real close above that creates the higher high structure he wants in discount.

**Illustrative result:** You avoid a fake long that was only a stop run.

**Situation:** Daily candle closes below previous daily low.

**Application:** HTF MSS / "final nail" language. Regime read updates. Hopium does not overrule the close.

**Situation:** Hourly wick above supply, 15m closes back under the block.

**Application:** Sweep + rejection. Short management model, stop beyond wick extreme per risk.

## Anti-Patterns (tactical)

**Don't:** Screenshot a wick and declare structure shifted.

**Why:** The model explicitly separates wick (hunt) from close (confirm).

**Don't:** Ignore a clean close because the narrative is bullish.

**Why:** Closes are the facts. Narrative is hopium risk.

**Don't:** Use a 1m close to announce a weekly MSS.

**Why:** Confirmation is local to the timeframe of the close.
