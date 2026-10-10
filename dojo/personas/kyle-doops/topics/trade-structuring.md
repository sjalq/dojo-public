---
triggers:
  - "user asks how Kyle sizes positions"
  - "user asks about DCA or grid bots"
  - "user asks about pyramiding into levels"
  - "user asks about BitFunded or prop firm"
  - "user asks how Kyle manages a trade"
  - "user asks about spot vs leverage"
  - "user asks when Kyle takes profit"
use_when:
  - "User wants to understand Kyle's entry and position-management method, not just his directional call"
  - "User asks how to scale into a position the way Kyle does"
  - "User asks about the role of DCA grid bots in his workflow"
  - "User asks about prop firms or BitFunded in his approach"
  - "User asks how Kyle structures a trade with a spot core vs leverage"
fails_when:
  - "User wants a current entry signal — this topic covers method, not today's level"
  - "User wants to apply this framework to altcoins; Kyle does not pyramid or grid-accumulate alts"
  - "User treats the spot core and leverage layers as the same capital pool with the same rules"
related:
  - "macro-overlay.md"
  - "market-cycle.md"
  - "risk-management.md"
---

# Trade Structuring

## When to Use
- User wants to know how Kyle actually builds a position, not just where he looks
- User asks about DCA bots, grid strategies, or staggered orders
- User asks about the spot vs leverage split in his approach
- User asks when and how he takes profits or rotates gains
- User asks about prop firms in his workflow

## Fails When
- User wants a live entry signal — this is the method, not the map
- User wants this applied to altcoins; Kyle uses only short-term, tightly-stopped trades on alts, not grids or pyramids
- User treats the three layers (spot core, leveraged tactical, hedge short) as interchangeable; they have different rules and different capital pools

## Core Concept

Kyle does not enter trades. He assembles positions. Every capital commitment is a staged sequence governed by one principle: no single wrong call should damage the account structurally. This is why he separates capital into three permanent layers, uses grid bots for accumulation so emotion cannot override the plan, and caps personal risk-of-ruin by using prop-firm capital during confirmed chop.

The three layers run simultaneously but independently:

1. **Spot core** — DCA/grid-accumulated at cycle lows; never sold on drawdown, only on multi-metric exit convergence
2. **Leveraged tactical** — low leverage (1.5–5x isolated), opened and closed at range extremities only
3. **Hedge short** — introduced at range highs or late cycle; explicitly framed as "insurance, not bank"

## DCA Grid Bots

Grid bots are his accumulation engine at cycle lows. During the 2022–23 bear market he ran aggressive grid DCA across the $15.5k–$19.7k zone, placing staggered buy orders so the bot accumulated more as price fell. He closed one leg of that grid in March 2023 at $28.5k for 120% profit. He said: *"A lot of the community were able to buy Bitcoin all the way down from $16,000 to $15,500 because I showed them how to use that grid strategy."* (K3-2HX4c0uU, Mar 2023)

In the 2024–25 bull run he inverted the logic — grid bots scaled OUT into strength across BTC, ETH, XRP, SOL, SUI, Pepe, Bonk, Penu, NEAR, and Render. (Confirmed Jun–Jul 2025, tyYcGhLqzlc / EvlQfAfcsxI.) The bot removes the willpower problem of selling into euphoria.

**Always pre-load the grid before the anticipated move, not during it — Why:** Grids loaded mid-move have no downside buffer. The accumulation value is that every lower tick fills a cheaper order. Exception: if a structural level is confirmed with a trigger candle after the initial move, a second, smaller DCA tranche can be added — but never chase the run with a fresh full grid.

## Pyramiding Into Levels

The pyramid means: smallest allocation first, growing allocation as price approaches the key support. *"As you get closer and closer to the key levels you'll buy bigger and bigger portions into those zones."* (kqdBnZAtQiw, Aug 2024)

Typical architecture is 3–5 orders:
- First tranche: ~10–20% of intended position, at the first warning level
- Middle tranches: increasing size toward the core support zone
- Final ~50%: held for either the confirmed low (worst-case support tag) or deferred until trend confirmation

In November 2022 he published his live buying plan: 25% via rolling DCA, 25% allocated across key horizontals ($12k / $10k / $8.7k), and 50% reserved for confirmed uptrend. The pyramid meant he had capital left if price fell further — and capital ready when it confirmed.

**Never invert the pyramid (large first, small later) — Why:** Front-loading destroys the blended-entry advantage. If the level fails and price falls further, there is no capital left to average down, and the position becomes illiquid at a losing average. Exception: in a confirmed uptrend with very high-confluence entry (golden pocket + 200 EMA + FVG stack), the first tranche can be larger, but a second order is still staged below.

## Position Types: Spot Core vs. Leveraged Tactical vs. Hedge Short

**Spot core**
- Accumulated at cycle lows via grid/DCA; not touched during intra-cycle corrections
- Only exits on 90–100% convergence across the 12-metric exit dashboard (PI Cycle, Puell, MVRV-Z, NUPL, BTC.D, etc.)
- Firewalled from leverage: stops that close a leverage position leave the spot core untouched
- Example: BTC spot entered at $17.1k held through the entire move to $73k ATH without a single sell (P4, through Jan 2024)

**Leveraged tactical (1.5–5x isolated)**
- Opened and closed at range extremities only — longs at range low, shorts at range high, "nothing in the middle" (j91iGTVSUwo, Apr 2024)
- At 2x: *"think of it more as a spot trade — take profit without giving up the upside"*
- Hard stop below the stated invalidation level; stop moved to break-even only after a confirmed move away from support
- Funding cost gate: closes when funding exceeds expected profit — *"the funding rates will end up eating me alive, I'll rather reload"* (mRRHpCOl_e8, Apr 2024)
- Cut to 3x max during volatility events: *"if you use 10x, go all the way down to 3x"* (iDvwsc0O0gg, Nov 2022)

**Hedge short as insurance**
- Introduced only at high-confidence resistance or when macro trend weakens
- Sized to partially offset spot exposure, not to profit directionally
- Examples: altcoin shorts as hedge on ETF-denial risk (Jan 2024); MSTR short from the ATH in late 2025 — 75% closed at TP1, 25% running free as a "free trade"; described as *"insurance not bank"* explicitly in May 2025 (S1hJeiivZGs)
- Never opened to create net-neutral exposure; the spot core retains its directional bias throughout

## Prop-Firm Capital for Chop (BitFunded)

During confirmed mid-cycle chop (P5, May–Oct 2024) Kyle directed viewers to use BitFunded prop accounts instead of personal capital. The worst-case is the challenge fee (~$49 illustrative), not a drawdown in the real account.

The logic: chop phases are psychologically hard to avoid trading; prop capital limits the damage if multiple range trades stop out. This is not a wealth-building approach — it is a risk-of-ruin firewall for the phase where neither accumulation nor full deployment is correct.

**Never deploy significant personal capital on intraday range trades during confirmed chop — Why:** Expected value of range trades in choppy conditions approaches zero after fees and slippage; the real risk is impairing the capital needed to deploy at the actual trend resumption. Exception: if the range-low entry aligns with the pyramid levels and has multi-timeframe confluence, a small personal allocation with a hard stop below the range low is acceptable.

## Profit Rotation and Partial Exits

Kyle uses a level-to-level, 25–75% structure at every target:
- Counter-trend catch (bull trap / dead cat framing): 75% off at TP1, tight stop on residual
- Trend-aligned trade: 25–50% at TP1, trail the remainder under confirmed higher lows
- Altcoin and meme coin gains: rotated into majors (BTC, ETH, SOL) — *"take profit take profit be careful, don't get wrecked over there"* (Gv6te6QINuQ, Mar 2024)
- Bear-to-bull transition profits: sold BTC at $28.5k into stablecoins, explicitly not into altcoins (WdhCPgT_iwA, May 2023)

**Always take at least partial profits at the first target — Why:** The first TP converts a speculative position into a free or near-free trade. Holding 100% through TP1 exposes the full position to a reversal at that resistance. Exception: in confirmed Phase 4 parabolic conditions he held longer, reasoning that *"80% of all returns in crypto will be made in the final 20% of the cycle"* (Gv6te6QINuQ, Mar 2024) — but this only applies once the cycle is declared parabolic, not as a general rule.

## Anti-Patterns (tactical)

**Don't:** Enter a full position at once, regardless of conviction level.
**Why:** If the level breaks, there is no capital left to average down. Kyle's Nov 2022 plan — 25% / 25% / 50% tranches — is the template; the final 50% is exactly what allows him to deploy at the real low rather than being stuck at a bad average.

**Don't:** Move the stop to break-even while price is sitting on support.
**Why:** A stop is a sell order. Placing it at break-even while price rests on support means selling support. He stated this explicitly in Dec 2022: *"You don't want to sell support — you want to buy support."* Move it only after a confirmed move away from the level.

**Don't:** Load a grid mid-pump and call it DCA accumulation.
**Why:** Every grid order placed mid-pump opens at or near the pump price with no lower buffer. The entire DCA advantage is the spread across falling prices. Grids work on the way down to build average; they do not work on the way up.

**Don't:** Apply the same stop and sizing rules to the leveraged tactical layer and the spot core.
**Why:** The spot core has no stop below the multi-metric exit signal. The leveraged trade has a hard stop stated before entry. Conflating them leads to either stopping out of the spot core at a temporary low or holding leverage through a larger drawdown than was sized for.
