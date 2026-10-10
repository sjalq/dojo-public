---
triggers:
  - "user asks when to enter a trade"
  - "user asks if now is a good time to buy"
  - "user wants to know Kyle's entry signals"
  - "user asks about confirmation"
  - "user is impatient and wants to enter early"
  - "user asks whether to chase a pump"
  - "user asks about re-entry after selling"
use_when:
  - "User is about to enter a trade without a stated trigger or invalidation level"
  - "User is asking whether a current price is a good entry"
  - "User wants to understand what Kyle waits for before buying"
  - "User is FOMO-ing into a move that is already extended"
fails_when:
  - "User has already entered and is asking what to do now — that is a position management question, not an entry question"
  - "User is asking about a long-term DCA strategy — the DCA plan bypasses trigger discipline by design"
  - "User wants a target level to buy at — Kyle gives trigger signals, not targets; the trigger fires at the level"
related:
  - "risk-management.md"
  - "range-trading.md"
---

# Entry Discipline

## When to Use
- User is deciding whether to enter a trade right now
- User has a setup in mind but has not stated a trigger or invalidation
- User is asking if they missed the move or should chase
- User wants to understand why Kyle sometimes waits weeks or months before entering

## Fails When
- User has a fully defined setup with a trigger and invalidation — at that point, execute or don't; this framework does not add anything
- User is asking about a specific asset Kyle would not trade (most altcoins on a long-term basis)
- User wants certainty about outcome — triggers improve probability, they do not guarantee results

## Core Concept

Kyle's entry rule is a single sentence that appears in every phase of his trading: **"No trigger, no trade."**

A trigger is a specific observable market event that confirms a setup is live. It is not a price level you like. It is not a feeling. It is not the fact that the asset has dropped a lot. It is a concrete, pre-stated condition — a candle close, a structure reclaim, an EMA cross — that must fire before he commits capital. Without the trigger, he waits. Indefinitely if necessary.

The rule is paired with a hard invalidation: a level or condition that, if reached, proves the thesis wrong. He states the invalidation BEFORE the entry, not after. This is what separates a planned trade from a hope.

## The Trigger Must Be Pre-Stated

**Never/Always: Always state the trigger before entering — Why:** If you define the trigger after the fact you will find one every time. Post-hoc rationalization is not a trigger. The trigger's function is to keep you out of the trade until the market proves the setup is live, not to justify an entry you already want to make.

In P3 (May 2023) Kyle had sold all his Bitcoin at $28,500 and was sitting in cash. Rather than re-entering as the price drifted sideways for months, he stated his exact re-entry trigger: "I would need to see price start to take out around those $30,000 levels" with EMAs crossing back up. Then he said: "I'd rather be patient even if it meant I bought higher." (WdhCPgT_iwA) He sat in cash from May to October — five months — waiting for that trigger.

The trigger fired around the October 2023 breakout. He did not re-enter before that. The trade was more expensive when he re-entered. He was fine with that because the confirmation signal was worth the extra price.

## What a Valid Trigger Looks Like

Kyle's triggers come from a short list of structural confirmations. He does not use vague conditions ("market looks strong"). He uses specific ones:

**Price structure reclaims:**
- Reclaim of the 21 EMA on the weekly (macro bull regime confirmation): "Needs multiple candle closes above."
- Reclaim of the 9/18 EMA cluster ("pink line") on the daily: "price must reclaim to shift momentum."
- Reclaim of a key horizontal after a sweep: e.g., in P7 (Jun 2026): "There is no trigger, no trigger on the trade. Do not take the trade over here because there's no reclaim." (2QeEnge1RJI)

**Pattern completion:**
- In P2 (Dec 2022) the entry trigger was the "Wick × Wick × Wick" pattern on the 4H chart at $16,600 — three consecutive wicks at the same support level signalling absorption. That was the trigger. Not "$16,600 looks cheap."
- In P3 (Feb 2023) the trigger was an ascending triangle breakout: "As long as $23,500 holds I'm okay" — the level was the invalidation; the breakout of the triangle was the trigger.

**Momentum signals:**
- MACD cross of the zero line on the weekly (bear market duration signal).
- TD Sequential 9-count buy/sell signal: "seven, eight, nine, local top" or "nine buy" for longs.
- RSI reclaim of the tracked pivot level on the daily.

**Volume gating:**
- In P7 (2026 decline) declining daily exchange volume was an explicit no-entry condition: "The rallies won't be sustainable without that daily exchange volume, which is still declining." He would not enter a long until volume confirmed the move.

## Waiting Is the Job

Kyle's patience is not passive. It is an active decision to preserve capital and optionality. He described it across multiple phases:

- P1: "rather wait for an established uptrend where the market is going to be poised in a much safer position" (5A0fEFf4hwQ)
- P1: "pretty much just sitting on my hands. I'll wait for the FOMC and see what happens from there. If you end up losing a little bit of opportunity it's not the end of the world. It's better than losing all your money." (_oJuL26W1Gg)
- P3: "I would wait. I would wait, wait, wait." Explicit endorsement of doing nothing as the dominant activity.
- P5: "all you have to do is you need to be patient right — wait for a shift in the market, wait for a break of structure." (kqdBnZAtQiw)

**Never/Always: Never enter just because you have been waiting — Why:** Impatience is not a trigger. The longer you have been in cash does not increase the probability that a setup is valid right now. Exception: After a very extended sideways period where Bollinger Bands have contracted to historic extremes (P5, Jul 2024: "absolute tightest BB reading ever seen for Bitcoin"), the probability of a big move is high — but the direction is still unknown. The position is still gated by the trigger, not by how long you have waited.

## Do Not Chase Pumps

**Never/Always: Never chase a pump in a bear market — Why:** In bear markets pumps are relief rallies. They are traps. The correct trade is to short the pump after a couple of days once a lower high forms, not to buy into the move. Kyle stated in P1: "don't chase the pumps — short the pumps after a couple of days." In P3 he labelled the entire $19k-$28k move a "bear market relief rally" and participated only with his DCA grid, not with a new tactical long.

Exception: In a confirmed bull regime (21W EMA well established above price), short-term chasing of a breakout with a tight stop is acceptable — specifically when the breakout is the trigger itself (e.g. "$30k breakout" as the 2023 re-entry signal). Even then, he stated he would buy at a higher price on confirmation rather than anticipate.

## The Multi-Condition Bottom Checklist

Kyle has never called a bottom on price action alone. He uses a simultaneous three-condition gate for entries at potential cycle lows:

1. High-volume capitulation candle (measured against the 7-day exchange volume MA)
2. Sustained negative aggregate funding rates (not a single negative print — "held negative for quite some time")
3. Altcoins taking out all-time lows / momentum divergence (later replaced by: "bull moon" signal + Market Cipher B green dot)

All three must fire. In P1 (Nov 2022) with BTC at $16k he said: "it's not capitulation yet. The price has gone down damn far but it's still not capitulation because it's very low volume, no negative funding rates." (fJOEz4EFcfc) He was cash for months more.

**Never/Always: Never call a bottom on price alone — Why:** The fact that price has dropped a lot tells you nothing about whether it will drop more. The three criteria together identify a structural exhaustion event. Price alone is just sentiment. Exception: When the 1.618 fib extension, long-term trend line, and broadening wedge fib all converge at a level (as in P7's 28-38k target zone), the technical confluence is strong enough to plan a scaled entry in advance — but the actual trigger is still required to fire before capital is deployed.

## Aggressive vs Conservative Entry Options

Kyle often gives his audience two entry frameworks for the same setup:

**Aggressive**: Enter at the level itself with a hard stop below. Higher risk, better average price. Suitable when the level is extremely high-confluence (e.g. 21 EMA + 200 MA + golden pocket all at the same price).

**Conservative**: Wait for the higher low to form after a bounce from the level. Enter on the confirmation of structure, not the level itself. Higher price, lower risk, better probability. "Wait for price to push back above — wait for the higher low — that is your next best zone with greater confluence so you're not catching a falling knife." (voNC4i09gW4, P5 Aug 2024)

Kyle himself tends to take the conservative entry for spot and the aggressive entry for very small, tightly-stopped leverage scalps.

## The 21-Week EMA as Macro Gating

Every tactical trigger operates within a macro regime defined by the 21-week EMA. Kyle will not establish new spot longs in a confirmed bear regime (21W EMA sloping down and price below it). He will not add to shorts in a confirmed bull regime (21W EMA sloping up and price above it).

In Feb 2025 he exited to 100% cash in a single daily close when the 21W EMA was lost: "I'm out. Just to be clear. I'm fully in cash." (RV5Rwzdrbpc) He did not wait for more confirmation. The macro gate had closed. All tactical triggers inside a bear regime are for short-term counter-trend trades with tight stops — not for re-establishing a core directional position.

**Never/Always: Always check the 21W EMA before assigning a directional bias — Why:** A great entry signal in the wrong macro regime is a loser. A breakout trigger in a bear market is just a lower high. The EMA regime determines whether you are trading with the trend or against it, and Kyle only trades with the macro trend for spot positions.
