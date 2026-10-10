---
triggers:
  - "user asks where to buy a pullback"
  - "user is FOMO buying into a premium pump"
  - "user asks about equilibrium or 50% Fib"
  - "user asks why a level like daily 50% / mid-range matters"
use_when:
  - "defining discount vs premium after an impulse leg"
  - "planning adds after a bullish MSS or before a relief leg"
  - "filtering FOMO: do not buy premium if the plan is discount entries"
fails_when:
  - "Fib is drawn on the wrong leg (not bottom-to-top of the relevant impulse)"
  - "user buys 50% with no LTF confirmation in a downtrend"
  - "user treats 50% as magic support that cannot break"
related:
  - "market-structure-shift.md"
  - "four-point-structure.md"
  - "timeframe-hierarchy.md"
  - "anti-hopium.md"
---

# 50% Retrace / Equilibrium

## When to Use
- After a defined impulse (low→high or high→low) you need a mechanical mid for discount/premium
- You feel FOMO on a pump and need a rule that keeps you from buying premium
- You are waiting for daily/HTF "equilibrium" before the next leg
- You want a simple Fib: only 0 / 0.5 / 1

## Fails When
- The range is not defined (no clear swing low and swing high for the leg you care about)
- You enter at 50% against HTF structure with no LTF MSS confirmation
- You assume touch of 50% guarantees reversal; it is a magnet and a plan level, not a promise
- Cycle-wide "50% drawdowns" history is confused with range equilibrium (related frame, different job)

## Core Concept

Markets always retrace 50%. Market makers, institutions, smart money (whatever label) drive price back toward the mid of a defined range. Discount is where they want to buy; premium is where they want to sell. Same logic as shoes: buy cheap, sell expensive.

Operationally: pull Fibonacci from the bottom of the move to the top (or reverse for shorts). Keep only 0, 0.5, and 1. The middle line is the 50% retrace. Below mid after a bullish impulse is discount; above is premium. He often calls the HTF mid **equilibrium** (example language: daily equilibrium on TOTAL).

You do not need a stack of Fib ratios. This is the only Fib he needs for the model. When price is pumping and you feel FOMO, the rule is simple: you do not buy in premium if your plan is discount.

Touching 50% is not the full trade. Confirmation still lives on the lower timeframe: typically a market structure shift (e.g. higher high on 15m) **in the discount zone** while the higher-timeframe trend thesis is still valid.

## How to Apply

1. **Define the impulse.** Mark the swing low and swing high of the leg you are trading (breakout leg, relief leg, or range extremes he is calling).
2. **Pull Fib 0 / 0.5 / 1 only.** Save a template if needed. Mid line = 50% = equilibrium for that range.
3. **Label discount and premium.** Long bias: wait for price into/below 50% (discount). Short bias: wait for premium after a bearish impulse (mirror).
4. **Set the alert at mid.** When it tags, drop to confirmation TF (often 15m when HTF is 1h/4h/daily).
5. **Require LTF confirmation in the zone.** Example long: in discount, wait for 15m higher high / MSS. Prefer confirmation in discount, not after price has already left discount.
6. **Place stops from structure.** Scalp: under the 15m shift low. Swing/add plan: under the major HTF low if you are building a bull-market add book. Partials if LTF MSS prints against you after a target touch.
7. **If equilibrium never tags.** Treat missed HTF 50% as information (concern / manipulation risk), not ignore it. Plan B may be different adds or partials.

## Examples

**Situation:** After a liquidation flush and a strong bounce, retail buys the breakout while the full impulse has not returned to 50%.

**Application:** Do not buy premium. Pull Fib bottom→top of the relevant leg. Wait for mid. On first tag, drop to 15m; only long if MSS prints in discount. If wick vs close: close below a prior low confirms strength of that level; wick alone can be a liquidity hunt.

**Illustrative result:** You skip the FOMO long and take the mid-range confirmation that matches the drafted path.

**Situation:** Daily update language: "we need to come back to 50%… equilibrium has been achieved, we can have another leg up."

**Application:** Treat HTF mid as the completion of the retrace job. After equilibrium, look for continuation structure rather than inventing a deeper mandatory dump for its own sake.

**Illustrative result:** Equilibrium becomes a regime label: retrace job done, now trade the next structure.

**Situation:** X plan: if LTF MSS against position after a high tag, take ~25% profits; if no tag of resistance, wait for 50% retrace to add.

**Application:** 50% is both an add magnet and a mental framework for not round-tripping winners without a plan.

## Anti-Patterns (tactical)

**Don't:** Buy the face-melting pump in premium because "it only goes up."

**Why:** Premium is where inventory wants to offload. Discount is where the model wants risk for longs.

**Don't:** Stack 0.236 / 0.382 / 0.618 noise as if the model depends on them.

**Why:** The operational model is mid-range equilibrium. Extra Fibs create fake precision.

**Don't:** Market-buy the first touch of 50% with no LTF shift.

**Why:** Mid can fail. Confirmation in discount is what turns a magnet into a trade.

**Don't:** Confuse historical "BTC dropped 50% five times" cycle stats with this range Fib.

**Why:** Cycle drawdown stats feed anti-hopium and context. Range 50% is a trade location tool. Keep the jobs separate.
