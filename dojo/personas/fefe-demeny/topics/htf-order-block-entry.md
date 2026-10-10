---
triggers:
  - "user asks how to enter at supply or demand"
  - "user asks what an order block is"
  - "user is shorting every touch of a level without confirmation"
  - "user confuses a random candle with a strong level"
use_when:
  - "mapping HTF magnets (hourly+ order blocks / supply-demand) before LTF entries"
  - "building AMD or continuation entries at a real zone"
  - "filtering weak levels that lack consecutive-candle strength"
fails_when:
  - "every candle is labeled an order block"
  - "user enters the zone with no LTF rejection"
  - "user ignores that strong levels can still sweep and reverse"
related:
  - "amd-pattern.md"
  - "timeframe-hierarchy.md"
  - "scale-and-trail.md"
  - "liquidity-retail-traps.md"
---

# HTF Order Block Entry

## Attribution
Order block / supply-demand magnet vocabulary is ICT / Smart Money Concepts adjacent. Fefe's operational process is his: mark the last opposing candle before impulsive displacement, prefer multi-candle strong levels, drop to LTF for rejection/AMD confirmation, stop beyond the HTF box. Credit the lineage; present the entry process as his packaging.

## When to Use
- You need the magnet before any LTF AMD or MSS entry
- Defining supply/demand that actually produced displacement
- Planning scalp shorts/longs into a level with stop beyond the HTF box

## Fails When
- Levels are drawn on every pause without impulsive follow-through
- Entries fire on first touch with no rejection close
- Stop is inside the noise of the box instead of beyond structure

## Core Concept

Higher-timeframe order blocks (and supply/demand zones) are the magnets. An order block, in his operational language, is basically the last bearish or bullish candle in market structure before an impulsive move. Strong levels also show as zones with real acceptance: he looks for at least three consecutive candles to form a strong level on the timeframe that matters (e.g. hourly).

Process:

1. Mark the HTF magnet (1h / 4h / daily).
2. Expect price to return there as liquidity and inventory rebalance.
3. Drop to LTF (often 15m) for entry confirmation: rejection, MSS, AMD distribution.
4. Place risk beyond the HTF structure (e.g. stop above the hourly block for a short).

Traders screw this up by shorting or longing every approach: "here and here and here" into the zone with no confirmation. Confirmation is the job of the LTF. The HTF only tells you where the fight should be.

## How to Apply

1. **Find displacement.** Where did price leave in a hurry? The last opposing candle before that move is the OB candidate.
2. **Validate strength.** Prefer zones with multiple consecutive candles / clear rejection history, not a single random wick.
3. **Box the zone on HTF.** Keep it visible when you drop timeframes.
4. **Wait for price into the box.** No anticipatory full-size entries far from the magnet unless that is a different model.
5. **Confirm on LTF.** Rejection close, MSS, or full AMD. First touch without reaction is not a mandate.
6. **Risk beyond the structure.** Stop on the far side of the HTF block; target via structure trail, next OB, or measured move, not vibes.

## Examples

**Situation:** Hourly chart shows three consecutive candles and a last bullish candle before an impulsive dump; later price climbs back into that box.

**Application:** Mark the hourly supply. On 15m wait for rejection/AMD. Short with stop above the box. Trail with LTF structure.

**Illustrative result:** Entry quality comes from magnet + confirmation, not from predicting the first touch.

**Situation:** Daily order block above as the next magnet after a local 4h reclaim.

**Application:** If LTF structure flips bullish, plan the trade toward the daily OB / equilibrium rather than calling the ultimate bottom. The OB is the target magnet, not proof the bear market ended.

## Anti-Patterns (tactical)

**Don't:** Label every candle an order block.

**Why:** Only candles that precede real impulsive displacement earn the magnet role.

**Don't:** Full-size the first tag with no LTF close against the approach.

**Why:** Zones get swept. Confirmation is the filter.

**Don't:** Put the stop in the middle of the box.

**Why:** Noise inside the zone will stop you before the idea is invalidated.
