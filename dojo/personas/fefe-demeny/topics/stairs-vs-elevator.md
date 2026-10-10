---
triggers:
  - "user asks whether a slow grind is buyable"
  - "user describes elevator up stairs down or elevator down stairs up"
  - "user is long a choppy recovery after a dump"
  - "user asks what stairs vs elevator means on a chart"
use_when:
  - "reading path shape of a move (impulse vs grind) on any liquid chart"
  - "deciding whether to fade a pullback or wait for the next impulse"
  - "annotating freehand path language on TOTAL, BTC, or alts"
fails_when:
  - "used alone without HTF context, MSS, or order-block confirmation"
  - "user forces elevator labels on range chop with no clear impulse"
  - "user treats 'always a buy' as size-up without risk and structure"
related:
  - "amd-pattern.md"
  - "follow-market-structure.md"
  - "liquidity-retail-traps.md"
  - "market-structure-shift.md"
---

# Stairs vs Elevator

## When to Use
- You need a one-glance read on whether price is impulsive or grinding
- After a fast move, you are deciding whether the slow counter-move is a buy or a trap
- Teaching freehand chart language (black squiggles on TradingView) for impulse vs chop
- Coupling path shape to AMD accumulation (stairs into a magnet) before distribution

## Fails When
- There is no clear elevator leg, only sideways noise, and you invent stairs
- You buy stairs up after elevator down because "it always comes back" without a structure shift
- You ignore higher-timeframe direction and trade stairs language against the HTF trend
- You use the slogan as a substitute for stop placement, RR, and confirmation

## Core Concept

You always want to be on the elevator, not the stairs.

The elevator is the fast impulsive leg: a near-vertical path, few candles, real displacement. The stairs are the slow multi-wave grind: choppy higher lows or lower highs that look constructive while they build stop liquidity under a trendline or into a supply/demand zone.

Two named variants:

1. **Elevator up, stairs down** is always a buy frame. After a fast push higher, price crawls lower. That slow stairs pullback is bullish path language: the impulse was the real move; the grind is the gift. "Market is coming down slowly. That is very very bullish."
2. **Elevator down, stairs up** means you never take the stairs. After a dump, the slow multi-wave recovery is not the trade. Smart money can be walking retail longs up the stairs into an order block while building trendline liquidity underneath. You wait for the next elevator (impulse) in the direction that structure supports, often the next distribution down.

This is freehand chart language, not an indicator. Draw multi-wave squiggles for stairs and a single vertical path for elevator. It pairs with AMD: elevator down then stairs up into an HTF order block is classic accumulation path shape before manipulation and distribution.

## How to Apply

1. **Mark the last clear impulse.** Is the dominant displacement up or down? That leg is the elevator candidate.
2. **Read the counter-move.** Multi-wave grind = stairs. Fast continuation or reversal displacement = elevator.
3. **Apply the rule set:**
   - Elevator up + stairs down → treat as pullback-in-uptrend path language (bias long, still wait for your confirmation model).
   - Elevator down + stairs up → do not buy the stairs; expect trap risk into magnets above.
4. **Couple to a magnet.** Stairs into an hourly (or higher) order block, 50% equilibrium, or trendline liquidity is higher-quality path language than stairs in the middle of nowhere.
5. **Still require confirmation.** Stairs language sets bias. Entry still wants LTF rejection, MSS, or your scale-and-trail rules. "Always a buy" is path bias, not a market order.

## Examples

**Situation:** TOTAL prints a vertical spike, then sells slowly for hours under a labeled POI while a dashed support holds.

**Application:** Label elevator up, stairs down. Bias long on the slow grind. Plan adds toward structure, not chase the elevator after it already ran. Watch the invalidation level (e.g. a broken key support that ends the bullish path).

**Illustrative result:** Path language keeps you from shorting a healthy stairs pullback just because "it's red."

**Situation:** BTC dumps hard, then chops in multi-wave higher lows toward a supply box while a freehand stairs path is drawn into that box.

**Application:** Elevator down, stairs up. You never want to be on those stairs. Wait for rejection from the supply / HTF order block and the next elevator down, or wait for a real bullish MSS if structure actually flips.

**Illustrative result:** You avoid long scalp pain in the recovery grind that exists to park retail stops under the trendline.

**Situation:** Live AMD teaching: price elevator-downs, then stairs-ups under an hourly order block forming an uptrending trendline.

**Application:** Read stairs as accumulation path, not "buy the bounce." Wait for manipulation into the OB and distribution rejection on LTF.

**Illustrative result:** Stairs language and AMD become the same movie: path shape first, trap second, impulse third.

## Anti-Patterns (tactical)

**Don't:** Buy stairs up after elevator down because the chart "looks recovered."

**Why:** That path is how retail gets walked into liquidity and order blocks. The stairs are the setup against them, not the entry.

**Don't:** Short stairs down after elevator up just because price is lower than the high.

**Why:** Slow stairs after an impulse up is the bullish path variant. Shorting it is fighting the path language.

**Don't:** Draw elevator/stairs on every wiggle without an impulse and a counter-path.

**Why:** Without a clear elevator leg, "stairs" is just noise labeling and becomes superstition.

**Don't:** Size full risk on path language alone.

**Why:** Path language is bias. Confirmation, stop location, and RR still decide whether the trade exists.
