---
triggers:
  - "user asks about goals-based investing or wealth management"
  - "user asks how to structure a portfolio for multiple goals"
  - "user asks about aligning investments with life goals"
  - "user asks about wealth management for individuals or families"
  - "user asks about the goals-based process or framework"
use_when:
  - "Client or adviser needs to structure an investment program around specific life goals rather than a single risk/return target"
  - "User is building or reviewing a wealth management practice for private clients"
  - "User needs to understand why traditional institutional approaches fail individuals"
  - "User wants the full iterative process for goals-based portfolio construction"
fails_when:
  - "Client has a single, simple goal and a short time horizon where standard allocation suffices"
  - "Client is an institution with a single liability stream and tax-exempt status"
  - "User is looking for specific security selection or stock-picking advice"
related:
  - "institutional-vs-individual.md"
  - "dreams-and-nightmares.md"
  - "modular-portfolio-architecture.md"
  - "internal-external-assets.md"
  - "adviser-as-translator.md"
  - "benchmarking-and-rebalancing.md"
---

# Goals-Based Wealth Management

## When to Use
- An individual or family has multiple financial goals with different time horizons and different tolerances for failure
- A wealth adviser is building or restructuring a practice to serve private clients rather than institutions
- The existing portfolio treats the client as a single risk/return number and the client is dissatisfied or confused about whether they are on track
- A family office needs a framework that connects "what matters to the family" to "how the money is invested"

## Fails When
- The client genuinely has one goal, one time horizon, and one risk profile; the goals-based process adds complexity without insight in that case
- The adviser tries to implement the full modular architecture without first understanding the client's actual goals; the process is iterative, not top-down
- The adviser treats the framework as a marketing pitch rather than an operating model; it demands real structural changes to how portfolios are built and reported
- The client's total financial assets are too small to support meaningful sub-portfolio differentiation; at some minimum scale the overhead exceeds the benefit

## Core Concept

Goals-based wealth management starts from a single observation: individual clients are not small institutions, and what works for a pension fund cannot simply be overlaid onto a family. Institutions typically have one purpose, one time horizon, a huge asset base, tax-exempt status, and many small liabilities. Individuals have multiple purposes, multiple time horizons, taxable status, and relatively small asset bases. The traditional approach, building one blended portfolio optimized against a single "risk tolerance" number, badly serves the individual because it conflates goals that have fundamentally different characteristics.

The alternative is to start with the client's actual goals, not with an abstract risk questionnaire. Goals typically fall into three broad categories: personal (maintaining current lifestyle, flexibility, unanticipated needs), dynastic (providing for children and grandchildren without spoiling them), and philanthropic (giving that reflects the family's values). Each goal carries its own time horizon, its own tolerance for failure, and its own required probability of success. The same person who needs absolute certainty that the mortgage is paid may accept a coin-flip probability on a philanthropic endowment. These are not contradictions; they reflect normal human behavior.

Risk, under this framework, is not the standard deviation of portfolio returns. Risk is the probability of failing to achieve a specific goal. This redefinition, formally validated by Das, Markowitz, Scheid, and Statman in their 2010 Journal of Financial and Quantitative Analysis paper on mental account optimization, is the intellectual foundation Brunel builds on. The 2010 paper demonstrated that goals-based (mental account) processes are just as efficient as mean-variance processes, provided the definition of risk changes from return volatility to goal-failure probability. Attribution: Brunel credits this paper explicitly as the work that "transformed what I've been trying to do since 2002" and "made it mainstream."

The process itself is iterative and consists of four steps that generate a full cycle:

1. **Identify and describe the client's main goals.** Use the client's own language (needs, wants, wishes, dreams), not financial jargon. What are the goals they want to achieve with the greatest intensity, and what failure would hurt the most?

2. **Dollar-weight and prioritize those goals.** Assign to each goal the amount of money believed necessary to achieve it. Personal lifestyle goals are typically addressed first and with the lowest level of risk. Moving up the priority hierarchy, certain degrees of failure become acceptable and risk can increase.

3. **Structure a sub-portfolio for each goal.** Choose assets or strategies appropriate to that goal's characteristics. If the goal is to maintain the client's lifestyle, the manager will not invest in private equity, which may offer potentially high long-term returns but will not provide regular distributions for living expenses. If the goal is philanthropic growth over 30 years, a higher-equity, higher-risk allocation is warranted.

4. **Optimize the sub-portfolios across the whole portfolio.** The aggregate of all sub-portfolios becomes the client's policy portfolio. This step ensures that the parts add up to a coherent whole and that interactions (tax implications, rebalancing, reporting) are managed across the full picture.

Clients do not usually arrive with their decisions already made. Most have never really managed their money at this scale. As time passes and as they adjust to the process, they discover what is important to them, learn how to rank their priorities, and gain a better understanding of what is possible. The iterative nature of the process accommodates this evolution.

The framework also rests on an explicit debt to behavioral finance, specifically Meir Statman's behavioral-finance portfolio pyramid (attribution: Statman, "What Do Investors Want?" Journal of Portfolio Management, 2004). Statman indicated that each investor has not only a variety of goals but also different risk profiles to accompany each of those goals. Some of these risk profiles may seem almost contradictory, yet they are not exclusionary: the same person who buys a lottery ticket (dream goal, very high risk tolerance) also buys insurance (lifestyle goal, near-zero risk tolerance). The goals-based framework translates this insight into an operational investment process.

A related parallel framework that must not be confused with Brunel's: Ashvin B. Chhabra's Wealth Allocation Framework. Brunel cites Chhabra as a "fellow traveler" in the same intellectual movement, and Daniel Nevins and Michael Pompian as additional contributors of valuable parallel work. None of these are Brunel's own frameworks; they are independently developed approaches to a similar problem.

## How to Apply

1. **Start with the client conversation.** Ask about dreams and nightmares in plain language (see dreams-and-nightmares.md). Identify every goal the client can articulate, from lifestyle maintenance to multi-generational wealth transfer.

2. **Categorize and prioritize.** Group goals as personal, dynastic, or philanthropic. Within each category, distinguish needs (must be funded with near-certainty) from wants, wishes, and dreams (progressively higher tolerance for failure).

3. **Dollar-weight each goal.** Determine how much capital is needed to fund each goal at the required probability of success. For lifestyle goals, this means projecting spending needs, inflation assumptions, and life expectancy. For dynastic goals, it means estimating what each generation needs to be "helped on their way" without being spoiled.

4. **Build a sub-portfolio per goal.** Match asset classes and strategies to the time horizon and risk tolerance of each goal. Short-term lifestyle goals get fixed income. Long-term growth goals get equity. See modular-portfolio-architecture.md for the module system.

5. **Aggregate and optimize.** Combine sub-portfolios into a single policy portfolio. Check for interactions: tax implications, rebalancing triggers, reporting requirements.

6. **Iterate.** Revisit annually or when circumstances change materially. The client's understanding of their own goals evolves; the process must accommodate that evolution.

## Examples

**Situation:** A family has $35 million in assets with annual spending needs of $1 million. Generation 1 is about 50 years old, inflation is expected at approximately 3% per year, no outside income.

**Application:** Internal capital preservation (apartment complex, approximately $2 million) and internal growth (venture capital investment managed by Generation 2, $1 million) are set aside first. A declining-balance portfolio funded with $4.7 million at a 4% return assumption covers short-term lifestyle needs (years 1 through 5). A further $7.2 million at a 6% return assumption covers years 6 through 15, totaling $11.9 million for a 15-year lifestyle cycle. Because Generation 1 is approximately 50, a second replenishment cycle of $7.7 million is funded to age 80. Lifestyle subtotal: $19.6 million (56% of assets). The family reserves 10% ($3.5 million) for opportunistic or "thematic" goals. After $3 million to internal investments, $8.9 million remains for capital growth. The resulting policy portfolio has five distinct sub-portfolios, each with its own asset allocation, benchmark, and reporting.

**Illustrative result:** The family can see exactly how much of their wealth funds each goal, what rate of return each sub-portfolio needs, and where the risk sits. Conversations shift from "are we up or down this quarter" to "are we on track to meet our lifestyle needs, and how are the dynastic and philanthropic goals progressing?"

**Situation:** A client whose ambition was to accumulate $20 million. He and his partner sold their business and realized $250 million each. His one request: "do not lose money."

**Application:** The goals-based process started with the client where he was: a capital-preservation mandate. Over five years, as the portfolio was well diversified and the client became less concerned about losing what he had, his thinking evolved toward long-term goals. The iterative process accommodated this shift without forcing the client to articulate goals he was not yet ready to acknowledge.

**Illustrative result:** The client's portfolio evolved from a single defensive mandate to a multi-goal structure spanning lifestyle maintenance, dynastic planning, and eventually philanthropic ambitions, as his comfort and understanding grew over time.

## Anti-Patterns (tactical)

**Don't:** Start with an asset allocation and work backward to find goals that justify it.
**Why:** This reverses the process. The goals define the allocation, not the other way around. Starting with the allocation produces the same one-size-fits-all portfolio the framework is designed to replace.

**Don't:** Use a single "risk tolerance" score derived from a standard questionnaire as the basis for the entire portfolio.
**Why:** A single number cannot capture the reality that the same client has near-zero tolerance for lifestyle-goal failure and high tolerance for philanthropic-goal failure. The questionnaire produces a blended average that serves no individual goal well.

**Don't:** Treat the goals-based framework as a one-time planning exercise.
**Why:** Clients' understanding of their own goals evolves. Markets change. Life events happen. The framework is iterative by design; a static plan misses the point.

**Don't:** Absorb frameworks from parallel thinkers (Chhabra's Wealth Allocation Framework, Statman's portfolio pyramid, Wilcox's discretionary wealth hypothesis) as if they were Brunel's own.
**Why:** These are independently developed frameworks that Brunel cites and builds on. Crediting them to Brunel is both inaccurate and disrespectful to the originators.
