---
triggers:
  - "user asks when to split code into modules, files, or services"
  - "user says a file is 'getting too long' or asks about code organization"
  - "user wants to design architecture or shared abstractions up front"
  - "user asks how to grow a codebase without it becoming a mess"
use_when:
  - "structuring a growing codebase and deciding when to extract modules"
  - "someone is designing shared modules or abstractions before writing the concrete code"
  - "reviewing a refactor whose only justification is file length or DRY"
fails_when:
  - "the environment genuinely punishes long files — in a language full of hidden mutation, defensive splitting is rational"
  - "the boundary is a real deployment or team boundary, not a code-organization choice"
related:
  - "culture-shock.md"
  - "types-as-sets.md"
  - "the-elm-architecture.md"
  - "api-design-guidelines.md"
---

# The Life of a File (grow modules; do not plan ahead)

## When to Use
- A codebase is growing and the team is deciding when and where to split
- Someone proposes a shared `Post`/`User`/`Utils` module to serve multiple future pages
- A file crossed 400/600/800 lines and people are getting nervous
- Two features "look similar" and someone wants to unify them before either is finished

## Fails When
- **Your language cannot back you up.** The advice assumes cheap, reliable refactoring and no spooky action at a distance. Where mutation and dynamism make refactoring risky, short files and early boundaries are legitimate defenses — the habits exist for a reason, just not a universal one.
- **The split is organizational, not structural.** When two teams must own two pieces, or two services must deploy independently, the boundary is forced by reality; grow-then-split does not apply to org charts.

## Core Concept

Evan Czaplicki's answer to "how do I grow my codebase?" is to trace the life of a single file: it starts small, grows longer, grows longer still, and eventually breaks apart — but only when the code itself reveals where. The rule from the official guide: "all modules should be built around a central type." Start with one module per page or per problem, "centered around the Model type," and "just keep growing those modules longer and longer. Keep adding the types and functions you need. If I ever notice that I created a custom type with a couple helper functions, I *might* move that out into its own module."

The strategy has a deliberately provocative core: **Do Not Plan Ahead.** "Early in my projects, I always have these grand schemes of how everything will fit together. 'The pages for editing and viewing posts both care about posts, so I will have a Post module!' But as I write my application, I find that only the viewing page should have a publication date. And I actually need to track editing differently to cache data when tabs are closed... I end up turning Post into a big mess to handle all these competing concerns, and it ends up being worse for both pages." Starting concrete makes it "much easier to see when things are **similar**, but not **the same**. The norm in user interfaces!" Maybe you end up with an `EditablePost` and a `ViewablePost`, each with different structure and helpers. Maybe not. "I would just write the code and see what happens."

In the Elm Europe talk he demonstrated why apparent similarity misleads: a settings panel and a fruit-selection list are both "checkboxes," but the right data structure for one is a record with dependent fields, and for the other a size-limited, order-preserving selection list. "We started with two things that look basically the same and ended up with entirely different ways of approaching them — that was all about the data structure... It is true that they share checkboxes, but that's such a small fraction of the actual difficult things that are going to happen in your code that it makes sense to emphasize the data structure instead."

When a split does happen, the payoff is the module boundary itself: expose as little as possible, hide the implementation behind an opaque type, and the module can maintain invariants no caller can break. "If the public API works, the code works everywhere" — and hidden internals can be refactored freely.

## How to Apply

1. **Start with one file built around the central type of the problem.** Model, logic, view/presentation together. Resist creating a second file on day one.
2. **Grow it.** Add types and helper functions as features arrive. 400, 600, 800 lines is not a smell in a language with guarantees — "So I encourage you to push your limit on number of lines! See how far you can go."
3. **Watch for the signal: a custom type with a family of helper functions.** When a distinct data structure accumulates its own operations (insert, remove, member, toggle...), that cluster is a module waiting to be born. Split there — around the type, never around a layer or a visual region.
4. **Close the new module down.** Export the type opaquely and the minimal functions. "Expose as little as possible, but no less." Now the module can enforce its invariant (e.g., "at most two selected") and you can fuzz-test the public API instead of every call site.
5. **When you got it wrong, refactor without fear.** "This works because the compiler makes it really easy to do huge refactors. If I realize I got something majorly wrong across 20 files, I just fix it." Choose tools that make this true, and then rely on it instead of on prophecy.
6. **Interrogate discomfort.** "If you're feeling uncomfortable, like 'this seems like too much code here' — push into that feeling and see if it actually is warranted. Is there actually a problem, or is it just a feeling based on experiences in other languages?"

## Examples

**Situation:** A startup's main page module hits 900 lines and a new hire proposes splitting it into `model.rs`, `handlers.rs`, `views.rs`, plus a shared `helpers.rs`.
**Application:** Ask what *type* is trying to get out, not what layer. If the file has grown a `Subscription` type with six helper functions, extract a `Subscription` module with an opaque type. If there is no such cluster, the file is just long — leave it and keep building.
**Illustrative result:** Modules map to concepts, so "where is the code about books?" has an obvious answer — "it's in the module about books" — instead of being smeared across layers.

**Situation:** Two product surfaces both show "orders," and an architect wants one shared Order abstraction before either surface ships.
**Application:** This is the grand-scheme trap verbatim. Build both concretely first. If they converge, extracting the common type later is cheap; if they diverge (they usually do — similar is not the same), you have avoided building one module that is worse for both.

**Situation:** A team wants to enforce "max 200 lines per file" in their style guide.
**Application:** Ask what constraint that rule was protecting against in the ecosystem it came from, and whether it exists here. A line-count ceiling forces splits at arbitrary points, which manufactures exactly the debatable boundaries the grow-then-split approach avoids.

## Anti-Patterns (tactical)

**Don't:** Add getters and setters to a module you just made opaque.
**Why:** "The whole point of having a module was that we were able to hide implementation details... Setters — their whole point is to expose those details. You've done all this work to put it in a module, and now you're going to give setters that just totally defeat that entire exercise. Just use a record if you want people to have access." Hide, or expose — committing to neither costs you both.

**Don't:** Refactor pre-emptively because it's satisfying.
**Why:** "Just as there's premature optimization, there's premature refactoring... it's like you get to play code golf at work." Wait for a problem you actually have — code you came back to after a month and found confusing — and solve that. The goal is never "more modules"; modules are a tool for hiding details that have started to hurt.
