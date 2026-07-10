---
triggers:
  - "user asks how to make software reliable or reduce production errors"
  - "user asks about null handling, error handling strategy, or defensive programming"
  - "user debates types vs tests, or asks what guarantees are worth"
  - "user wants fearless refactoring or confidence in large changes"
use_when:
  - "deciding which failure classes to eliminate by design rather than manage by process"
  - "evaluating tools or architecture by the guarantees they give"
  - "a team spends heavily on defensive checks, tests, and production firefighting for the same recurring error classes"
fails_when:
  - "the failure class can't be designed away — network partitions, hardware, and third-party outages need handling, not elimination"
  - "reliability rhetoric is used without the discipline — claiming guarantees while keeping escape hatches is worse than claiming nothing"
related:
  - "types-as-sets.md"
  - "designed-boundaries.md"
  - "compilers-as-assistants.md"
  - "the-elm-architecture.md"
---

# No Runtime Exceptions (reliability as a designed property)

## When to Use
- Choosing where reliability should come from: design guarantees vs. tests vs. process vs. heroics
- A team fights the same class of production error repeatedly (null crashes, unhandled cases, sync bugs)
- Justifying investment in tools or architecture that make bug classes impossible
- Deciding whether an "escape hatch" is worth the guarantees it forfeits

## Fails When
- **The world is the failure source.** Timeouts, partial failures, and bad input from outside must be modeled and handled; "no runtime exceptions" means *your* logic can't crash, not that reality cooperates.
- **The guarantee is aspirational.** One `any`-typed backdoor or unchecked cast and the property is gone globally. Guarantees are all-or-nothing; partial adoption yields the costs without the confidence.

## Core Concept

Elm's most famous claim — the one Evan Czaplicki chose precisely because it sounds impossible ("wait, is that possible? Are you a liar?") — is **no runtime errors in practice**. It is not a testing achievement; it is a design decision. The language simply does not contain the ingredients for whole categories of crashes: no null, no exceptions in normal code, no incomplete case left silently unhandled, no mutation from a distance. His standing evidence was NoRedInk: hundreds of thousands of lines of Elm in production, and as he put it at Deconstruct, "in the year and a half they've been using it in production, still no runtime errors." (Asked how he knows it's zero: legacy JavaScript in the same product still throws, "so we know errors can be detected.")

The mechanism has two halves. First, **remove the billion-dollar mistake**. Evan quotes Tony Hoare on inventing null in 1965: "This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage." Elm replaces null with `Maybe` — absence becomes a value the type system forces you to confront: "Should you check? Did the person giving you the value check? Maybe it will be fine? I guess we will find out later!" is exactly the conversation the design deletes. Second, **make partiality visible**. The compiler detects incomplete pattern matches — the function that handles some cases and crashes on the rest — and "this is particularly helpful when you have a large codebase and add a tag to a custom type. Now the compiler will point out all the case expressions scattered throughout your code that need an extra branch."

What Evan sells is not the absence of crashes but what the absence buys: **confidence**. From the guide: "it is quite common for Elm programmers to say they never felt so confident while programming. Confident to add features quickly. Confident to refactor thousands of lines. But without the background anxiety that you missed something important!" Reliability-by-design converts refactoring from a risk into a routine — which is what makes grow-then-split code structure viable at all (see the-life-of-a-file.md) — and it changes daily experience: the type errors arrive at compile time "in a way that feels like a pair programmer saying hey, did you think about this case?" (see compilers-as-assistants.md). The refactor-bug he uses as the canonical example: change the shape of a "person," forget two functions that relied on the old shape, and in JS "the version of `isOver50` thinks an ageless person is under 50, a very sneaky bug... you would eventually find out about the missing field, but probably weeks later in a bug report. The risks introduced by a refactor in JS often mean that people just refactor less, even if it is 'the right thing to do.'"

The price is discipline at the boundary: guarantees survive only if nothing inside the system can violate them, which is why Elm refuses arbitrary JS interop (see designed-boundaries.md). "One of the best things about Elm is that there are entire categories of problems you just do not have to worry about... but if we can call JS directly, all that goes away."

## How to Apply

1. **Inventory your production errors by class, not by incident.** Null/undefined access, unhandled cases, invalid states, sync drift. For each class ask: could a design make this *impossible* rather than *rarer*?
2. **Make absence and failure explicit values.** Replace null-ish conventions with types that force the question at the point of use (Maybe/Result/option patterns in whatever stack you have). The goal is that "forgot to check" fails at build time, not in a bug report weeks later.
3. **Ban silent partiality.** Every case-analysis over a finite set of possibilities should be checked for completeness by a machine. Adding a new variant should produce a to-do list from the compiler, not a production surprise.
4. **Count the second-order payoff.** The business case is not "fewer crashes" alone — it's cheaper refactoring, faster feature work, fewer defensive tests, and developers who make big improvements because they aren't scared. Teams that can't refactor safely stop refactoring; the codebase's decline is the compounding cost.
5. **Protect the guarantee at the boundary.** Decide explicitly where unchecked data enters (APIs, user input, interop) and validate it into honest types there, once. Inside the boundary, no exceptions to the rules — an escape hatch anywhere is a guarantee nowhere.
6. **Advertise the property the way Evan does.** If you achieve a real guarantee, state it in its impossible-sounding form and invite the fact-check (see on-storytelling.md). Checkable bold claims convert skeptics.

## Examples

**Situation:** A SaaS team's top three incident causes for the year are all `undefined is not a function` variants in the frontend.
**Application:** That is one error *class*, not three problems. Introduce a typed layer (or language) where absent values are explicit, and validate all API responses into honest types at the boundary. The test suite shrinks where the type system takes over.
**Illustrative result:** The recurring class disappears rather than declines; on-call load drops and refactors stop being scheduled around fear.

**Situation:** A team adds an enum variant ("order status: refunded") and spends two weeks finding every switch statement that mishandles it.
**Application:** This is exactly Elm's incomplete-pattern-match scenario. Adopt exhaustiveness checking wherever the stack allows; the compiler should have produced the complete list of sites in seconds. Where the language can't, structure the code so the variant list and its handlers live together.

**Situation:** A founder asks whether "no runtime exceptions" style rigor is worth it versus "move fast."
**Application:** Reframe: the rigor is *how* you move fast after month three. The alternative is the JS-refactor economy — "people just refactor less" — where speed decays as the codebase grows. Guarantees are an investment whose return is sustained velocity and, per the guide, "fewer tests, yet more reliable code."

## Anti-Patterns (tactical)

**Don't:** Chase reliability by adding defensive checks everywhere ("if not null" at every entry).
**Why:** Scattered checks are the tax you pay for a data model that permits invalid states. The checks multiply, drift, and still miss cases. Fix the model so the invalid state cannot be represented (see types-as-sets.md), and the checks become unnecessary rather than exhaustive.

**Don't:** Keep "just one" unchecked escape hatch for convenience.
**Why:** Guarantees are global properties. "Does this package produce runtime exceptions? When? Will it mutate the values I give to it?" — the moment one path can, every consumer must ask those questions about everything again. You pay the full discipline cost and get none of the confidence dividend.
