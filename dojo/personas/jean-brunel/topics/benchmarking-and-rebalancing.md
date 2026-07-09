---
triggers:
  - "user asks how to benchmark a goals-based portfolio"
  - "user asks about rebalancing frequency"
  - "user asks how to evaluate performance in a goals-based framework"
  - "user asks about the flight plan analogy"
use_when:
  - "An adviser needs to report performance to a client whose portfolio is structured around multiple goals, not a single benchmark"
  - "The user wants to understand how rebalancing works when there are multiple sub-portfolios"
  - "A client is confused about whether their portfolio is 'winning' or 'losing' because the standard benchmark comparison does not map to their situation"
fails_when:
  - "The portfolio is a single-goal, single-benchmark institutional portfolio where standard performance reporting applies"
  - "The user needs specific rebalancing rules for a particular asset class rather than the goals-based philosophy"
related:
  - "goals-based-wealth-management.md"
  - "modular-portfolio-architecture.md"
---

# Benchmarking and Rebalancing in Goals-Based Portfolios

## When to Use
- A goals-based portfolio has been constructed and the adviser needs to report performance to the client
- A client is asking "how am I doing?" and the standard answer (up 8% vs. the S&P's 12%) is misleading or demoralizing
- The adviser needs guidance on how frequently to rebalance across sub-portfolios
- A practice is designing its reporting and oversight process for goals-based portfolios

## Fails When
- The portfolio is a single-purpose institutional portfolio where a single benchmark is appropriate
- The user is looking for tactical rebalancing rules (threshold-based, calendar-based) rather than the philosophical framework

## Core Concept

Goals-based portfolios create a specific challenge for performance evaluation: the client's aggregate portfolio does not map to any single market index. Each sub-portfolio has its own purpose, its own time horizon, and therefore its own definition of success. A capital-preservation module that returns 3% in a year the S&P 500 returned 20% is not underperforming; it is doing exactly what it is supposed to do for the goal it serves.

Brunel uses the flight-plan analogy: "I like the analogy of the flight plan of an airplane, which is not necessarily a straight line. The pilot and I have exactly the same goal: to get to the destination on time. But once I am in the cabin, I do not worry about exactly how we meet that goal. I leave it to the pilot to evaluate altitude, speed, and other issues needed to achieve the goal of arriving at the destination on time. That is what a benchmark does. I can tell the client, 'I cannot prove to you that the capital preservation module is doing what it is going to do, but I can tell you that it is doing what it is supposed to do.'"

The performance review under this framework has two dimensions. First, the absolute dimension: have we met the goals? For shorter-horizon goals (next year's lifestyle needs), this is straightforward to evaluate. For longer-horizon goals (dynastic wealth in 20 years), absolute evaluation is less meaningful in any given quarter, and the benchmark dimension becomes more important. Second, the benchmark dimension: is each module doing what it is supposed to do? The benchmark for each module is derived from its purpose, not from a market index. A lifestyle module is benchmarked against whether it can fund the lifestyle. A growth module is benchmarked against whether it is on track to achieve the growth target over its time horizon.

On rebalancing, Brunel's guidance is: "When markets are behaving normally, in the sense of meeting the expected returns, we tend to rebalance annually, which in our experience offers the right balance between short and long term. When markets are volatile, we might rebalance more frequently. But rebalancing too frequently undermines the process." The annual default avoids the transaction costs and tax consequences of frequent trading while maintaining the discipline of the goals-based allocation. More frequent rebalancing is reserved for periods of significant market dislocation, not for routine market fluctuations.

The complexity created by multiple sub-portfolios and potentially as many benchmarks as clients is real. Brunel acknowledges this as one of the limits of the goals-based process: "Because certain strategies may appear in more than one module and because of the demands of proper benchmark use, the model can lead to complexity in investment reporting." The module system (see modular-portfolio-architecture.md) mitigates this by standardizing the building blocks, but the reporting challenge is structural and must be managed through clear, goal-oriented communication (see adviser-as-translator.md).

## How to Apply

1. **Report performance per goal, not as a single portfolio number.** The client should see whether each goal is on track: "Lifestyle funding is secure through year 8." "Dynastic growth is 4% ahead of its 15-year target." "Philanthropic allocation underperformed this quarter but remains within the acceptable range."

2. **Use the flight-plan analogy with clients.** The pilot evaluates altitude and speed; the client evaluates whether the destination (the goal) will be reached on time. The module may be above or below its benchmark in any given quarter without the goal being in jeopardy.

3. **Rebalance annually as the default.** Annual rebalancing offers the right balance between maintaining discipline and avoiding unnecessary transaction costs and tax events.

4. **Increase rebalancing frequency only in volatile markets.** When markets move sharply, sub-portfolio allocations can drift significantly from their targets. More frequent rebalancing during these periods maintains alignment with goals.

5. **Resist the urge to rebalance too frequently.** Rebalancing too often generates transaction costs, triggers taxable events, and undermines the long-term orientation of the goals-based approach.

## Examples

**Situation:** A client's capital-growth sub-portfolio returned 4% in a year the S&P 500 returned 15%. The client is concerned.

**Application:** The adviser explains that the capital-growth module is not benchmarked against the S&P 500. It is benchmarked against the long-term growth rate needed to fund the client's dynastic goals over a 20-year horizon. At 4%, the module is within its expected range and on track to meet the goal. The S&P 500 return is irrelevant to whether this specific goal will be achieved.

**Illustrative result:** The client understands that "underperformance" relative to an arbitrary benchmark does not mean their goals are at risk. The conversation shifts from "why didn't we keep up with the market" to "are we on track for what we actually need."

**Situation:** Markets have dropped 20% in a quarter and the client's lifestyle module, designed for short-term stability, has lost 3%.

**Application:** The 3% loss in the lifestyle module is more significant than the 20% drop in equities because the lifestyle module has a shorter time horizon and lower risk tolerance. The adviser evaluates whether the module can still fund the next three years of lifestyle needs. If yes, the rebalancing is routine. If the drop threatens the lifestyle timeline, an extraordinary rebalance from the growth module may be warranted.

**Illustrative result:** The decision to rebalance is driven by whether goals are threatened, not by arbitrary thresholds or calendar dates.

## Anti-Patterns (tactical)

**Don't:** Report a single aggregate return for the entire portfolio and compare it to a market index.
**Why:** The aggregate return is a meaningless average of sub-portfolios with fundamentally different purposes. Comparing it to the S&P 500 or a 60/40 index tells the client nothing about whether their goals are on track.

**Don't:** Rebalance monthly or quarterly as a matter of routine.
**Why:** Frequent rebalancing generates transaction costs, triggers taxable events, and can undermine the long-term orientation of each sub-portfolio. Annual rebalancing is the right default unless market volatility forces more frequent intervention.

**Don't:** Treat a sub-portfolio's underperformance relative to a market index as a failure.
**Why:** Each sub-portfolio has its own purpose. A defensive module that returns 2% in a year equities return 15% is succeeding at its job (capital preservation), not failing at the equity-market's job.
