---
triggers:
  - "user asks how to size into a setup"
  - "user missed the first rejection and chases"
  - "user asks when to add or move stop"
  - "user goes all-in on first AMD wick"
use_when:
  - "managing AMD or HTF level entries with partial size"
  - "trailing winners with LTF market structure"
  - "building a larger trade without needing perfect first tick timing"
fails_when:
  - "adds happen on hope without a second rejection"
  - "stop is widened after a loss of thesis"
  - "user pyramids into premium against structure"
related:
  - "amd-pattern.md"
  - "htf-order-block-entry.md"
  - "risk-and-expectancy.md"
  - "market-structure-shift.md"
---

# Scale and Trail

## When to Use
- First rejection at a magnet looks real but impulsive continuation could leave without you
- You want to add on retrace to the initiation order block after distribution starts
- Trailing a winner by structure rather than round-number vibes

## Fails When
- Half-size becomes full-size fear when the first entry is red
- Adds ignore total risk (multiple adds still respect account risk units)
- Trail stop is moved farther away to "give room" after structure already broke

## Core Concept

Usual management in the AMD teaching:

1. On first clean rejection from the HTF magnet / distribution start, take **about 50% of intended position size**. Reason: if the session is impulsive (e.g. New York open), the move can leave immediately and you do not want to miss a perfect setup entirely.
2. Wait for **retrace into the initiation order block** of that move (e.g. 15m OB of the distribution leg).
3. On **second rejection**, deploy the rest (or add), and begin trailing.
4. As new LTF order blocks print and reject, you can add or tighten stop below/above the latest structure. Building a bigger trade can mean a wider stop in price if you add, which can reduce R multiple if stopped while green; that tradeoff is explicit.
5. Exit when structure reverse-signals (example short exit: clear higher high / W formation against the position). Closing is fine even if more was available. Repeat both directions.

This is patience plus aggression: patience for the second touch, aggression when confirmation repeats.

## How to Apply

1. **Pre-define full size and risk unit.** Half of intended size on first trigger must still equal a known fraction of risk.
2. **First trigger = rejection proof**, not a random touch.
3. **Hard wait for retrace** to initiation OB unless the written plan allows runners only.
4. **Second trigger = add.** Move stop to structure that keeps total risk sane; prefer stop that locks progress when already in profit.
5. **Trail only with structure events** (new OB rejection, MSS in trade direction), not with P&L comfort.
6. **Flatten on reverse structure.** Do not negotiate with the W / higher high against a short.

## Examples

**Situation:** 15m AMD distribution off hourly supply. First close below prints.

**Application:** Enter half short. Wait hours/days if needed for retrace to the 15m initiation OB. Second rejection: add, stop above that OB, trail as successive stairs-down distribution legs print.

**Illustrative result:** You participate in the first impulse and still have dry powder for the clean retest.

**Situation:** Short working, then a clear W and higher high prints; he posts reversal coming and closes.

**Application:** Close. Do not hold for ego. Start the process again for longs or next short at HTF magnet.

## Anti-Patterns (tactical)

**Don't:** All-in on the first wick.

**Why:** Fake-outs exist even on "perfect" AMD. Half-size is the humility tax.

**Don't:** Add when price is running already extended with no retrace.

**Why:** That is chase, not scale.

**Don't:** Widen stops after the thesis fails so the add "can work."

**Why:** That converts a process trade into hopium.
