---
triggers:
  - "user asks how Kyle manages risk"
  - "user asks about position sizing"
  - "user asks about stop losses"
  - "user asks about leverage"
  - "user asks about scaling in"
  - "user asks how much to put in"
  - "user asks when to take profit"
use_when:
  - "User wants to know Kyle's core capital-preservation system"
  - "User is deciding how large a position to take"
  - "User is asking whether to use leverage and at what level"
  - "User wants to know when to take profits or move stops"
  - "User is in drawdown and asking what to do with spot vs leverage"
fails_when:
  - "User is asking about a specific coin's fundamental value — Kyle does not care about fundamentals"
  - "User wants a market direction call — this covers the HOW of sizing, not the WHEN of entry"
  - "User is already fully deployed and asking about rebalancing — this is pre-trade discipline"
related:
  - "entry-discipline.md"
  - "range-trading.md"
---

# Risk Management

## When to Use
- User wants to understand how Kyle sizes trades and why he rarely blows up
- User is choosing between spot and leverage and needs the firewall logic
- User is asking whether to hold through a drawdown or cut
- User wants to know Kyle's stop-loss mechanics, including the "free trade" rule

## Fails When
- User needs a directional call — risk management is orthogonal to market direction
- User is already in a trade they took at full size with no plan; the time for this system was before entry
- User is asking about portfolio construction across assets — Kyle's system is trade-level, not portfolio theory

## Core Concept

Kyle's edge is not prediction. It is capital preservation. Every rule in his system assumes he might be wrong and structures his exposure so that being wrong does not ruin him. He said it plainly in P1: "protecting your capital is much more important than making money. If you lose your capital then making money is much harder. Missing the train versus losing your money — there are a lot of trains but if you don't have your money and it's gone it's over, you can't catch a train." (fJOEz4EFcfc, Jul 2022)

This is not a system of picking winners. It is a system of surviving long enough for winners to compound.

## The Spot-Core vs Leverage Firewall

Kyle runs two completely separate books that never contaminate each other.

**Spot core** — long-term accumulation bag. Entered via DCA grid at cycle lows (e.g. $19.7k BTC grid in 2022; $17.1k original entry held all the way to the 2024 ATH). This bag is **never sold on drawdown**. It is only exited on his multi-metric exit signal convergence (90-100% on his dashboard). Drawdown is not a sell signal for spot — it is noise.

**Leverage book** — tactical trades only. Longs at 1.5-2x treated as "pseudo-spot" ("take profit without giving up the upside"). Shorts maxed at 3-5x isolated margin, never cross. In P3 he ran altcoin scalps at 2x isolated: "I'm running it with just 2x leverage — just something you could trade even as a spot position." (WdhCPgT_iwA)

**Never/Always: Never run leverage on your core directional bias — Why:** A leveraged core means a big move against you forces a cut at exactly the wrong time. The spot bag absorbs the drawdown. The leverage book has a defined stop that the spot bag does not. Exception: Grid bots on leverage (P6) are acceptable because the bot auto-manages exposure and has no single stop-out point; the human is not holding a leveraged directional position manually.

## Cut Leverage Into Volatility

**Never/Always: Always reduce leverage when volatility spikes — Why:** High volatility amplifies the leverage multiplier in the wrong direction. In P2 (FTX capitulation) Kyle told viewers directly: "if you used to 10x then go all the way down to 3x leverage" because "when the market is this volatile it's gonna amplify what's going on on your leverage." (iDvwsc0O0gg, Nov 2022) His own live FTX trade was 5x isolated on a small allocation — not 10x even at a point where confidence was relatively high.

**Never/Always: Close leverage when funding cost exceeds the opportunity — Why:** In P4 chop (post-halving consolidation) he stated explicitly: "the funding rates will end up eating me alive, I'll rather reload." Holding a leveraged position while paying funding in a ranging market is a negative-carry bleed with no upside edge.

## Scale In, Never Full Clip

**Never/Always: Never enter the full position at once — Why:** If you are wrong on the first entry you still have capital to average down to better levels and turn a losing entry into a winning trade. Entering full at once removes this optionality.

Kyle's standard structure is 3-5 staged orders. First tranche is approximately 10% of intended position size (fingerprint: "Holds 10-15% initial allocation, builds as levels confirm"). He explicitly described his entry pyramid in P4: "if I'm wrong at least three times and it comes lower, well I've got 60% of my orders in." (a1w9u2kLtc0)

In P1 he stated: "I leave the final 50% for the bottom as I'm about to get invalidated." This is the logic exactly reversed from most traders: his largest tranche goes in at the level where most people panic-sell, because that is where he has the most confirmation the level is real.

In P5 (Aug 2024) he described the scaling rule with his actual cadence: "buy a little bit over there, a little bit more over here, even more over here — as you get closer and closer to the key levels you'll buy bigger and bigger portions into those zones." (kqdBnZAtQiw)

Exception: In a clearly confirmed trending market (e.g. post-breakout with 21W EMA well above) a larger first tranche is acceptable because the risk of it going back to the entry level is lower. Even then, he never disclosed going all-in at once.

## Stop-to-Breakeven: The Free Trade

Once a trade has moved in Kyle's favour, he moves the stop to break-even. He calls this "eliminating the risk" or making it a "free trade." In P3 he did it live on the GALA position: "it's a free trade." In P7, after the MSTR short ran 1,000%+, 25% was left running with the stop at break-even.

**Never/Always: Never move the stop to break-even while sitting on support — Why:** A stop is a sell order. If the price is on support, moving the stop to break-even means selling support on a routine retest. This is the behaviour of the trader who just got shaken out of a good trade. Kyle articulated this in P2: "a stop loss is a sell order so that means that you would be selling support does that make sense you guys you don't want to sell support you want to buy support." (eo9p-k9sDJM, Dec 2022)

Exception: After a meaningful move away from the entry — not just a 1% pop — moving stop to break-even is correct. In the same Dec 2022 trade Kyle waited until price had moved substantially before he "moved my stop into slight profit."

## Partial TP Into Strength: Insurance, Not Bank

**Never/Always: Always take 25-75% off at the first target — Why:** Locking in partial profits means the position becomes psychologically easier to hold. You are no longer sitting on an unrealized gain you could lose; you have already banked something. Kyle frames exits as "insurance, not bank" — the partial exit protects against a reversal; the remainder participates in continuation.

Real behaviour from the extractions:
- P1: "50% at TP1, trail rest" on short trades
- P4: "We took 75% of our profit off... left some on the table just to participate without any form of FOMO."
- P5: "I raise my stops above my entry — I would actually stop out in slight profit and I'd rather attempt to reenter." (BSEgD-MNte8)
- P7: MSTR short: "75% already taken off" at TP1; 25% running with stop at breakeven

**Never/Always: Never frame a partial exit as banking the trade — Why:** If you frame taking profits as "I got out," you close the full position and miss continuation. The remainder after the partial exit is the "free ride" — it is already in profit territory and has the asymmetric upside of continuation with no downside risk to your original capital.

Trailing stop mechanics: "track underneath each higher low" on the daily close. He raises stops weekly only under confirmed daily higher lows. He never moves stops down.

## Position Sizing: ~10% on Alt Scalps

On altcoin scalps Kyle has been explicit: 10% of equity per position. In P3 the GALA trade was described as "just 10% of equity" at 2x isolated. In P5 he endorsed using BitFunded prop accounts (challenge fee ~$49) to trade chop so that personal capital is not at risk — a practical expression of the "never risk your main account on low-conviction setups" principle.

**Never/Always: Never swing-trade or position-trade altcoins — Why:** "99.9% of coins go to zero against Bitcoin" is his stated empirical view. Altcoin exposure is only acceptable as a short-term trade with a defined stop and a 10% sizing limit, not as a "bag to hold." Exception: In a confirmed bull cycle with strong relative strength, holding a small basket of majors (ETH, SOL, SUI) with trailing stops under higher lows is acceptable — but even then the position is managed, not held blindly.

## The 25%/25%/50% Accumulation Framework

In P2 (Nov 2022) Kyle made his full buying plan public. It applies in any capitulation environment:

- **25%** deployed continuously via DCA (time-based, regardless of price)
- **25%** deployed at key horizontal levels in the fall zone (in P2: $12k, $10k, $8.7k — roughly 8% per level)
- **50%** reserved for a confirmed uptrend (higher high + higher low established on daily)

The discipline here: the majority of capital is held back for the confirmed signal, not deployed into the knife. Most traders deploy 75% on the way down and have nothing left for the actual breakout. Kyle is the inverse.

**Never/Always: Never deploy the majority of capital into a falling knife — Why:** "The biggest mistake you can make right now is deploying too quickly." (85E0-NmiHHE, Nov 2022) The risk is not that you miss the bottom — it is that you run out of capital before the bottom and cannot hold through the drawdown. Exception: When the three-point bottom checklist fires simultaneously (high-volume capitulation candle + sustained negative funding + alts taking out lows / momentum divergence), the probability of a genuine bottom is high enough to justify accelerating the 25% horizontal deployment.

## Regime-Conditional Summary

| Phase | Spot book | Leverage book | Key move |
|---|---|---|---|
| Bear descent (P1) | Cash, zero spot longs | 3-5x shorts on bounces | "Spot only" long withheld |
| Capitulation (P2) | DCA grid running | 5x isolated tiny size | Told retail cut to 3x |
| Accumulation (P3) | DCA grid $19.7k | 2x on altcoin scalps (10% equity) | Sold spot $28.5k → stables |
| Breakout (P4) | Held from $17.1k, partial sells | 3x treated as pseudo-spot | 75% off at TP1 |
| Chop (P5) | No new entries mid-range | Prop-firm account for scalps | Range extremities only |
| Bull-to-peak (P6) | Grid bots; full cash Feb 2025 | Shorts as insurance (2.5:1 R:R) | One daily close = 100% cash |
| Decline (P7) | Majority cash | MSTR short (75% TP1); BTC short to +$40k | Stop at breakeven on runner |
