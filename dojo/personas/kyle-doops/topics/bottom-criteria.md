---
triggers:
  - "user asks if the bottom is in"
  - "user wants to know when to buy the dip"
  - "user asks about capitulation signals"
  - "user asks what Kyle looks for to call a bottom"
  - "price has crashed hard and user asks if it is time to buy"
  - "user asks about negative funding rates"
  - "user asks about a volume spike on a crash candle"
use_when:
  - "Price has fallen significantly and user wants to know if it is safe to start accumulating"
  - "User asks what conditions must be met before Kyle enters long"
  - "Bear market environment with multiple panic candles or exchange collapse event"
  - "User is constructing a staged buying plan for a macro low"
fails_when:
  - "Only one condition is met — all three minimum conditions must converge"
  - "User wants to call a bottom on price alone — no price level substitutes for the checklist"
  - "The phase is mid-cycle chop, not a macro bear market — different framework applies"
  - "Time-based capitulation is accepted as a substitute for price-based capitulation"
related:
  - "regime-model.md"
  - "cycle-top-dashboard.md"
---

# Bottom Criteria

## When to Use
- Price has made a large crash move and the question is "is this THE bottom?"
- User is asking when to deploy accumulated cash at the lows
- A major capitulation event has just occurred (exchange collapse, regulatory shock, macro crash)
- Constructing a staged buying plan to deploy into the macro low

## Fails When
- Price alone triggers the entry — no price level constitutes a bottom signal by itself
- Only one or two criteria are firing — convergence of all three minimum conditions is required
- Applied inside a ranging bull market — this is a macro bottom tool, not a mid-cycle dip tool
- Time-based capitulation (slow grind to a new low with no volume spike) is accepted as equivalent to price-based capitulation

## Core Concept

**Never call a bottom on price alone — Why:** A new price low tells you direction, not exhaustion. Real selling climaxes require evidence that sellers have depleted their ammunition: volume, funding rates, and structural corroboration from altcoins or momentum indicators must all align. Exception: long-term DCA accumulation at multi-year structural levels (e.g. the 2017 trend line, the realized price) can begin before full confluence at a small fraction of intended position size — not as a bottom call, but as a cost-averaging entry with defined reload levels below.

"It's not capitulation yet. The price has gone down damn far but it's still not capitulation because it's very low volume, no negative funding rates or any of those metrics that I'm looking at to signal an absolute bottom." — fJOEz4EFcfc, Jul 1, 2022

The three-condition framework appeared in P1 (July 2022), was applied live in P2 (FTX bottom, Nov-Dec 2022), and reappeared with minor additions in P7 (June 2026). The core logic is identical across all three cycles.

## The Three-Condition Minimum

### Condition 1: High-Volume Capitulation Candle

A large-range, high-volume down candle clearly visible as a spike on the aggregate exchange volume chart, indicating forced liquidation rather than orderly selling. Volume must be meaningfully above recent average. A slow grind to new lows does not qualify, even if price reaches a lower absolute level.

Kyle checks aggregate exchange volume (7-day MA) in nearly every video as the primary market health signal. Declining volume on a downtrend = distribution phase, not exhaustion. The capitulation candle is a single-session volume spike that breaks the pattern.

"I do not want time-based capitulation — I want the band-aid ripped off." — NM_dn5g3Xvo, Jun 26, 2026

### Condition 2: Sustained Negative Funding Rates

Aggregate perpetual funding rates must go negative and hold negative for an extended period. A brief dip to negative that immediately rebounds does not satisfy this condition. He tracks funding on Velo Charts / CoinGlass.

Sustained negative funding = shorts are being paid to hold = the market is structurally net short = short-squeeze potential. When longs have been flushed and only shorts remain, the setup for a mean-reversion move exists.

This condition also works in reverse inside a bull market: "Negative funding in a bull run is a screaming buy opportunity" (ZT5ANARCWgs, Aug 5, 2024 — flagged as this condition firing during the yen-carry crash).

### Condition 3: Altcoins Taking Out Lows / Momentum Divergence

Either: altcoins taking out all-time lows (P2, Nov 2022 — explicitly listed as unmet as late as November 10), or in later cycles: momentum divergence on Bitcoin itself (Market Cipher B green dot, cited in P7 Jun 2026 as still pending).

The logic: altcoins are the weakest link in the market structure. If they are still holding above prior lows when BTC is making new lows, distribution is not complete. When alts capitulate through all-time lows, the last holders are shaken out and the buyer base is reset. In cycles where alts have already been destroyed earlier, the equivalent signal is a momentum divergence — BTC making a new price low while a momentum indicator makes a higher low.

## Phase Evidence

### P1 — 2022 bear descent (all criteria unmet throughout)

Kyle articulated all three conditions in July 2022 (fJOEz4EFcfc) then tracked them for the rest of the phase. None fired. He remained in cash and small shorts. His target zone for the eventual bottom: $10-12k ("ultimate buy zone"), with $13,880 as a key quarterly/yearly level expected to be tagged first. From the October 2022 video (BPcG2FLmOCQ): "when Bitcoin is in such a major indecision point, altcoins are going to be very tough to buy."

### P2 — FTX capitulation (Nov-Dec 2022, criteria emerging but incomplete)

November 10, 2022 (iDvwsc0O0gg), BTC at ~$17k post-FTX announcement: all three criteria still unmet. "I am pretty much still fully in cash other than a dollar cost average position. I have not yet entered the market and I will let you know when I do."

November 11: "I am still fully fully in cash except for my dollar cost average portfolio."

November 24 (7ns4J-DgVyA): Kyle published his full staged buying plan — not a bottom call, but a framework for staged deployment:
- 25% via DCA grid already running (grid placed from $16k down to $10k on Bitget)
- 25% at specific horizontal levels: $12k, $10k, $8,700 (catching the falling knife tranche, ~8% per level)
- 50% reserved for confirmed uptrend (higher high + higher low on macro timeframe)

November 29: "Deploy slowly is the message. Biggest mistake you can make right now is deploying too quickly." (85E0-NmiHHE)

December 8 (oN73QFV6KbY): Tactical long at $16.6k — 5x isolated, stop below $16,670, targets $17,500 and $18,150. Framed explicitly as a range trade, not a bottom call. Regime was still bear. Stop logic: "a stop loss is a sell order so that means that you would be selling support — you don't want to sell support, you want to buy support." He refused to move the stop to break-even until price made a real move away from support.

Kyle never declared the $15.5k November low as the macro bottom during this phase. He later entered DCA bots around $19,700, which he closed for ~120% profit when he sold at $28,500 in March 2023 (K3-2HX4c0uU).

### P7 — 2026 re-run (Jun 26, 2026, NM_dn5g3Xvo)

By June 26, 2026 some criteria had fired but the checklist was still incomplete:

Triggered:
- Fear & Greed at 13% (anger/panic territory)
- USDT dominance: weekly close above 9.3% (breakout confirmed)
- DXY: confirmed daily candle close above breakout level
- Sentiment: "anger phase — blame Saylor" — "We're in the anger phase right now... anger, who shorted the market. That damn idiot Sailor." (NM_dn5g3Xvo)
- Longs being wiped back-to-back ($1B/day liquidations)

Not yet met:
- Volume spike capitulation candle at support (not yet)
- Momentum divergence: Market Cipher B green dot (not yet)
- "Bull moon" catalyst: expected Tue July 1
- "Full-blown sickness" bottom: "the signs and symptoms are there but we haven't had full-blown sickness. We're getting close. Very, very, very close."

Kyle's action: a small counter-trend long at $60k — 10x cross-margin, $1,000 at risk, TPs at $63k/$66k/$69k, 4.3:1 R:R. Explicit framing: "I'm not taking this because I think the dump is over — just because risk-to-reward makes sense." The three-condition checklist was not declared complete; this was a probability-weighted bounce trade within a still-active bear.

## The "Bull Moon" Fourth Condition (later cycles)

Kyle references lunar timing cycles as an additional confirmation layer, claiming roughly 80% historical accuracy. When he names a bull moon date (e.g. "expected Tue July 1" in Jun 2026), it functions as a timing catalyst overlay on top of the fundamental checklist — not a replacement for any of the three core conditions. It is called out when core conditions are approaching convergence and a timing signal would confirm the setup.

## The "No Bottom on Slow Grind" Rule

**Never accept time-based capitulation as a substitute for price-based capitulation — Why:** A slow descent over weeks to a new low may satisfy no checklist conditions even if the price is genuinely at a cycle floor. Without a volume spike, funding reset, and structural confirmation, the market can continue grinding for months and produce repeated false lows. Exception: if a slow grind produces a momentum divergence (Price: lower low, Momentum: higher low) that satisfies Condition 3, combined with persistent negative funding and declining altcoin relative strength, the combination can serve as a lower-conviction partial entry.

"You don't need to pinpoint the exact wick load to the freaking dollar of where the market bottoms. You're going to make much more money when you just wait for a new uptrend to get established." (trO8prUG0h4, Nov 28, 2022)

## Staging the Entry When Conditions Are Approaching

When conditions begin to converge (partial checklist firing), Kyle uses a three-tranche model:

**Tranche 1 — Early DCA / grid bots:** Small allocation running during the descent, accumulating well ahead of the bottom. The grid in 2022 ran from $16k to $10k on Bitget, using dollar-cost averaging ($100-$550/day range cited in P3). Sized so a miss doesn't damage the account.

**Tranche 2 — Horizontal-level entries:** Specific price levels where structural support converges (prior cycle lows, quarterly keys, 2017 trend line, realized price). Larger tranches than Tranche 1, but still not full clip. For 2022: $12k, $10k, $8,700. "The absolute ape-in zone" — his phrasing for the high-conviction multi-year support zone.

**Tranche 3 — Confirmed-uptrend entry (50% of intended position):** Only after a higher high AND higher low on the macro timeframe has been established. "You're going to make much more money when you just wait for a new uptrend to get established." (trO8prUG0h4) This is the largest single tranche, deployed only after the regime model flips bullish (see regime-model.md).

**Never all-in at one level — Why:** If the checklist is incomplete, price may have further to fall. Staging ensures capital remains to deploy at the real low, and a premature early entry does not wipe out the trading account. Exception: at historically significant multi-year confluence levels — described as the "absolute ape-in zone" in P2 — a larger single tranche is justified, but the full reserve is never deployed at one price.

## Leverage Adjustment at Capitulation

**Always reduce leverage during capitulation events — Why:** Volatility is highest at capitulation points; elevated leverage at high volatility means stop-outs at levels that prove to be correct in hindsight. Exception: a small isolated-margin position (5x or lower) at a structurally significant level is acceptable if the stop is placed below the wick low and the size is small enough that a full loss is manageable.

"If you used to 10x then go all the way down to for example 3x leverage, because when the market is this volatile it's going to amplify what's going on on your leverage." (iDvwsc0O0gg, Nov 10, 2022)

His own Dec 2022 tactical long: 5x isolated on a small allocation — "risking very very little."
