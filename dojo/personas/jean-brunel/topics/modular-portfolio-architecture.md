---
triggers:
  - "user asks how to build sub-portfolios for different goals"
  - "user asks about the bicycle analogy or mass customization in wealth management"
  - "user asks about portfolio modules or modular portfolio construction"
  - "user asks how to scale a goals-based practice across multiple clients"
use_when:
  - "An adviser has identified the client's goals and needs to translate them into actual portfolio structures"
  - "A firm is trying to scale goals-based wealth management without building a fully custom portfolio for each client from scratch"
  - "User needs to understand how the sub-portfolios work at the implementation level"
fails_when:
  - "The client's goals have not yet been identified; this is the construction phase, not the discovery phase"
  - "The client has a single goal where a single sub-portfolio is sufficient and the module system adds unnecessary complexity"
related:
  - "goals-based-wealth-management.md"
  - "dreams-and-nightmares.md"
  - "internal-external-assets.md"
  - "benchmarking-and-rebalancing.md"
  - "tax-aware-investing.md"
---

# Modular Portfolio Architecture

## When to Use
- The client's goals have been identified and dollar-weighted, and the adviser needs to build actual sub-portfolios
- A firm needs a scalable system for delivering goals-based portfolios to many clients without fully custom construction for each
- The client wants to understand how their money is actually organized and managed at the structural level
- A wealth management practice is designing its product architecture

## Fails When
- Goals have not been identified yet; building modules without knowing what they serve is building backward
- The firm builds modules but treats them as marketing labels rather than genuinely distinct investment strategies with different constraints
- The module system becomes so complex that reporting and oversight consume more time than investment management

## Core Concept

Once a client's goals have been identified, dollar-weighted, and prioritized, the wealth manager must translate each goal into a portfolio structure. The naive approach is to build a fully custom portfolio for each client from scratch. This does not scale. The opposite extreme, giving every client the same blended portfolio, defeats the purpose of goals-based management. The solution is modular architecture: a system of pre-built modules that can be assembled in different combinations to create a portfolio that is unique to each client but built from standardized components.

Brunel uses the bicycle analogy as his signature framing for this concept: "A bicycle is made up of a certain number of pipes, wheels, and gears. The bicycle for one client may require a horizontal pipe of 30 inches, whereas the bicycle for another client may require a horizontal pipe of 32 inches. But every client's bicycle will need a horizontal pipe." The goals-based modules are common across the platform and thus leave room for a standardization that essentially amounts to mass customization. Complexity exists where it belongs (at the client's goal level), and leverage exists across investment management (at the module level).

At GenSpring Family Offices, where Brunel served as Chief Investment Officer, this was implemented as four sets of modules across two axes:

- **Tax aware vs. tax agnostic** (recognizing that tax status materially affects which strategies and asset classes are appropriate)
- **Traditional strategies only vs. nontraditional strategies included** (recognizing that some clients want or need exposure to alternative investments while others do not)

Each of the four resulting sets consisted of nine modules, each addressing a specific category of client need: short-term lifestyle, long-term lifestyle, lifestyle replenishment, capital preservation, capital growth, and so on. The modules are contiguous but sufficiently distinct from one another, each optimized within the constraints of inevitable trade-offs while leaving room for flexibility.

The result is that the portfolio created for each client is unique (matching that client's specific goals and dollar-weights) but assembled from a known library of modules that the firm understands, monitors, and manages at scale. The potential exists for having as many benchmarks as the firm has clients, since each client's combination of modules produces a different aggregate allocation. Yet the process is simpler than it appears because the modules themselves are standard.

This architecture creates a specific challenge for performance reporting and benchmarking: the client's aggregate portfolio does not map to a single market index. Brunel addresses this with the flight-plan analogy (see benchmarking-and-rebalancing.md). The benchmark for each module is whether it is doing what it is supposed to do for the goal it serves, not whether it is beating a market index.

## How to Apply

1. **Design the module library.** Determine the categories of goals the firm will serve and build a module for each. At minimum: short-term lifestyle (defensive, income-generating), long-term lifestyle (balanced, inflation-fighting), capital growth (aggressive, long-horizon), and capital preservation (low-risk, liquidity-focused).

2. **Add the tax and strategy axes.** If the practice serves taxable clients, create tax-aware variants of each module. If some clients want alternative investments and others do not, create traditional-only and nontraditional variants.

3. **Map each client's goals to modules.** After the goals-discovery process (see dreams-and-nightmares.md), assign each goal to the module that best matches its time horizon, risk tolerance, and constraints.

4. **Dollar-weight the modules per client.** The same module may receive $5 million from one client and $500,000 from another. The module's strategy is the same; the allocation to it differs.

5. **Aggregate and optimize.** Combine the client's modules into a single policy portfolio. Check for cross-module interactions: tax-loss harvesting opportunities across modules, rebalancing triggers, and consolidated reporting.

6. **Review and adjust.** As the client's goals evolve, the module allocation changes. As capital markets shift, the modules themselves may need reoptimization. The structure accommodates both without rebuilding from scratch.

## Examples

**Situation:** A family with $35 million needs to fund two 15-year lifestyle cycles (to age 65 and to age 80), reserve 10% for opportunistic investments, and allocate the remainder to capital growth.

**Application:** Five modules are selected: a short-term lifestyle module ($4.7 million, 4% return assumption, years 1 through 5), a long-term lifestyle module ($7.2 million, 6% return assumption, years 6 through 15), a lifestyle replenishment module ($7.7 million for the second 15-year cycle), an opportunistic/thematic module ($3.5 million), and a capital growth module ($8.9 million). Each module uses different asset classes and strategies matched to its specific goal.

**Illustrative result:** The client's policy portfolio is the aggregate of all five modules. Each module has its own benchmark and its own reporting. The family can see exactly how much wealth is dedicated to each purpose and whether each purpose is on track.

**Situation:** A firm serving 200 families needs to deliver goals-based portfolios at scale without building 200 fully custom portfolios.

**Application:** The firm designs four module sets (tax-aware traditional, tax-aware nontraditional, tax-agnostic traditional, tax-agnostic nontraditional), each with nine modules. Every client's portfolio is assembled from these 36 standard modules in a combination unique to that client's goals, dollar-weights, and tax situation.

**Illustrative result:** The firm manages 36 strategies, not 200 custom portfolios. Each client's portfolio is genuinely personalized at the goal level but operationally efficient at the strategy level. New clients are onboarded by mapping their goals to existing modules, not by designing new portfolios from scratch.

## Anti-Patterns (tactical)

**Don't:** Treat modules as marketing labels for the same underlying portfolio.
**Why:** If every module has essentially the same asset allocation, the goals-based structure is cosmetic. The modules must be genuinely different in their investment strategy, benchmarking, and risk characteristics.

**Don't:** Let the module library grow without discipline.
**Why:** Every additional module adds reporting complexity, oversight burden, and potential for confusion. The nine-module structure GenSpring used was deliberately designed to be "as many as needed and as few as possible."

**Don't:** Benchmark the aggregate portfolio against a single market index.
**Why:** The aggregate is a combination of modules with different purposes. A single benchmark has no connection to the client's actual goals. See benchmarking-and-rebalancing.md for the flight-plan analogy.
