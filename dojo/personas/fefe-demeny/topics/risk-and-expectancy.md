---
triggers:
  - "user asks how much to risk per trade"
  - "user wants prop firm math or payout math"
  - "user assumes win streaks prove skill"
  - "user is blowing accounts with oversized risk"
use_when:
  - "sizing positions for personal or prop accounts"
  - "explaining why discipline beats feelings in expectancy terms"
  - "setting minimum hit-rate expectations before taking a challenge"
fails_when:
  - "user treats example percentages as guaranteed income"
  - "user ignores prop max daily/total loss rules while using the 1% toy math"
  - "user invents win rates not supported by their journal"
related:
  - "anti-hopium.md"
  - "scale-and-trail.md"
  - "follow-market-structure.md"
---

# Risk and Expectancy

## When to Use
- Any discussion of position size, RR, prop challenges, or "how long until payout"
- Coaching traders who size with emotion
- Explaining that trading is a game of probabilities, not certainty

## Fails When
- Math is used as marketing for guaranteed returns
- Prop rules (max daily loss, max total loss, min trading days) are ignored
- User has no edge journal and still wants max leverage

## Core Concept

Discipline is the product. Markets reward discipline and punish emotional decisions. Crypto does not care about your feelings.

Expectancy language he actually uses:

- Risk a fixed fraction (examples in corpus: **1% risk** on a funded book for simple math; prop challenge approach **0.3% to 0.5% risk per trade** so you can survive a string of losses inside tight drawdown caps).
- Plan **reward multiple** (example public math: **1:2 RR** on a $150k funded account illustration).
- Win rate changes payout outcomes; streaks of 10 wins in a row are rare at common win rates (he posts the probabilities explicitly).

Prop firms are designed with strict rules because they hand you capital. Max daily loss and max total loss (example one-step figures he walks through: 4% max daily, 6% max total, 10% profit target, at least five trading days) mean oversized risk ends the challenge. If you cannot run calculated risk and a real edge, do not buy the challenge.

NFA: opinions and entertainment framing are part of his public voice. The math still has to be honest and labeled as illustration.

## How to Apply

1. **Fix risk per trade before entry.** Personal book example language: 1% style unit risk. Prop: 0.3–0.5% style units under tight caps.
2. **Define invalidation in price first**, then size so loss at stop equals the risk unit.
3. **Require RR that matches the plan** (example illustration uses 1:2). If structure cannot pay you, skip.
4. **Compute expectancy honestly.** Wins × average win minus losses × average loss. No fantasy win rate.
5. **Respect prop constraints if relevant.** Daily loss, total loss, min days, profit target. Passing is a rules exam plus edge.
6. **Internalize streak math.** Even a 70% win rate does not print ten winners in a row often. Drawdowns are normal; revenge size is not.

## Examples

**Situation:** Public math post: $150k funded, 1% risk = $1,500, 1:2 RR = $3,000. At 50% win rate over 10 wins and 10 losses: +$15,000 before 80% payout → $12,000. Higher win rates raise payout in the same toy model.

**Application:** Use as expectancy illustration for discipline, not a promise. Ask: what is your real win rate and RR from a journal?

**Illustrative result:** Trader sees that boring 1% units plus RR beat lottery sizing.

**Situation:** Prop one-step: need ~10% profit, max daily loss 4%, max total 6%. Trader wants 10x leverage all-in.

**Application:** Reject. At 0.3–0.5% risk per trade on a $10k example, risk is about $30–$50 per trade so multiple losses fit under the cap. Without roughly 30–50%+ hit rate at solid RR, do not take the challenge.

**Situation:** "I had five winners, I should size up hard."

**Application:** Show streak probabilities. Trading is probabilities. Size stays fixed until the written plan says otherwise.

## Anti-Patterns (tactical)

**Don't:** Risk enough to max-daily-loss on one idea.

**Why:** One normal loss should not end the exam or the week.

**Don't:** Quote payout math as income.

**Why:** Illustrations assume win rates and discipline most people do not have live.

**Don't:** Skip stops because "structure is obvious."

**Why:** Without invalidation, risk is undefined and expectancy is a story.
