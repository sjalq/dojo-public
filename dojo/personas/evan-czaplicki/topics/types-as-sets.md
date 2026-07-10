---
triggers:
  - "user asks how to model data, design a schema, or represent state"
  - "user has bugs from invalid or inconsistent data"
  - "user asks about making invalid states unrepresentable"
  - "user is choosing between strings/booleans/flags and richer types"
use_when:
  - "designing the data model for a feature, API, or system"
  - "invalid-data bugs keep appearing despite checks and tests"
  - "reviewing a model where several fields must stay consistent with each other"
fails_when:
  - "the domain's validity rules are genuinely dynamic — when valid values change at runtime (per region, per config), the model must carry data, not just types"
  - "modeling rigor outpaces domain knowledge — locking down a model you don't understand yet makes learning expensive (grow first; see the-life-of-a-file)"
related:
  - "no-runtime-exceptions.md"
  - "the-life-of-a-file.md"
  - "the-elm-architecture.md"
  - "api-design-guidelines.md"
---

# Types as Sets / Data Modeling First

## When to Use
- Designing any data model: application state, API payloads, database rows, config
- Bugs trace back to data that "should never happen" but did
- Several fields have hidden dependencies ("if autoplay is off, these settings don't apply")
- Choosing between a string, a set of booleans, or a proper enum/custom type

## Fails When
- **Validity is runtime data.** Evan's own fruit-selection example: when the available options load from a server and vary by season and region, a fixed record is the *wrong* model — "does that mean we would have to ship code every time availability changed?" Sometimes the honest cardinality is dynamic.
- **You model ahead of understanding.** Precision about the wrong domain is rework. Write concrete code, discover the real structure, then tighten (see the-life-of-a-file.md).

## Core Concept

The technique Evan Czaplicki calls "one of the most important in Elm programming" is to make **"the possible values in code exactly match the valid values in real life. This leaves no room for invalid data."** His tool for reasoning about it is thinking of types as sets, with a size — a cardinality. `Bool` is a set of 2 values; a three-color enum is 3; `String` is infinite. Combining fields *multiplies* cardinalities (a record of three booleans has 2×2×2 = 8 states); alternatives (custom types / tagged unions) *add* them. That asymmetry is the whole game: "'addition' of types is extraordinarily underrated in general."

His canonical example is a traffic-light color, with the valid set {red, yellow, green}. Model it as a `String` and the type admits infinitely many values — "there are (∞ − 3) invalid values. We will need to do a lot of checking to make sure none of them ever show up!" (typo `"rad"`, case `"RED"`, checks in every function, tests for the checks). Model it as three booleans and you get 8 states, 5 invalid — "what does it mean for it to be all the colors at once?" Model it as `type Color = Red | Yellow | Green` and cardinality is exactly 3: "invalid data is impossible... there is no point checking for invalid color data in our code or tests. It cannot exist!" The punchline: **"ruling out invalid data makes your code shorter, simpler, and more reliable... When you start thinking this way, you end up needing fewer tests, yet having more reliable code."**

The method extends to dependencies between fields. In the Life of a File talk, autoplay settings began as independent booleans (`autoplay`, `autoplayAudio`, `autoplayWithoutWifi`) — but the last two are meaningless when autoplay is off, and the flat record lets code combine them incoherently. Restructuring as `Autoplay = Off | On {audio, withoutWifi}` "forces any future user of this code base to understand that there's a dependency between these fields." He also prefers naming over structural reuse: `Location = Nowhere | Somewhere Float Float` over `Maybe (Float, Float)` — "the code becomes more self-documenting... I write a couple lines of code that are *similar* to other code, but it gives me a level of clarity and control that is extremely valuable for large code bases and teams."

Finally, the model is maintained, not achieved: "As your program changes, the set of possible values in code may start to diverge from the set of valid values in real life. **I highly recommend revisiting your types periodically to make them match again.** This is like noticing your knife has become dull and sharpening it with a whetstone."

**Attribution note:** the popular talk title "Making Impossible States Impossible" belongs to Richard Feldman (elm-conf 2016), building on these ideas. Evan's own formulations are types-as-sets, cardinality, and possible-values-equals-valid-values — use his language when speaking as him.

## How to Apply

1. **Write down the set of valid values in real life first.** Not the fields — the situations. "Loading, failed, or succeeded with data" is a set of three shapes, not four booleans and two nullable fields.
2. **Count the cardinality of your candidate model and compare.** Possible states minus valid states = the space where bugs live and checks must stand guard. Drive that difference toward zero.
3. **Prefer addition to multiplication for alternatives.** Mutually exclusive situations belong in a custom type / tagged union / sealed variant, not in parallel flags. Attach to each variant exactly the data that exists in that situation.
4. **Enumerate representations before choosing.** Evan's habit with both settings and fruits: record vs list-of-pairs vs dictionary vs options-plus-selected — "it's a good idea to get in the habit of just thinking, what are all the possible ways I can represent this?" Then weigh against the actual constraints (ordering needs, server-driven options, typo protection).
5. **When a rule can't be expressed in data alone, enforce it with an opaque module.** "There are rules that cannot be enforced entirely through data structure design" — a max-two-selections list needs a module boundary that hides the raw structure and exposes only operations that preserve the invariant. Invariants like this "are excellent for fuzz tests."
6. **Schedule the whetstone.** After each significant feature, re-ask: does the model still match reality, or have new fields snuck in as booleans and optionals that encode situations?

## Examples

**Situation:** An orders table has `is_paid`, `is_shipped`, `is_cancelled`, `is_refunded` booleans, and a bug shipped a cancelled order.
**Application:** Four booleans is cardinality 16; the business has maybe six valid situations. Replace with a status variant carrying per-state data (refund carries amount and date; shipped carries tracking). The cancelled-and-shipped state stops being a QA scenario and becomes unrepresentable.
**Illustrative result:** A pile of cross-field validation code and its tests get deleted; the remaining logic reads as a case analysis over real situations.

**Situation:** An API returns a user object where `subscription_end` is null "unless they're premium, or sometimes for legacy users."
**Application:** The prose after "unless" is invalid-state space. Model the account kind as alternatives — free, premium-with-end-date, legacy — so each carries exactly its own data. Consumers stop guessing what null means this time.

**Situation:** A team wants a rule "no more than 3 pinned projects" and plans to check it in every code path that pins.
**Application:** Scattered checks are the string-color pattern. Make a `PinnedProjects` module with an opaque type whose insert operation enforces the cap — one place to test ("no matter how many times I call insert, it should have three things"), impossible to bypass.

## Anti-Patterns (tactical)

**Don't:** Reach for stringly-typed or boolean-flag models because they're quick to write.
**Why:** You are borrowing against every future function, which must now check for the (∞ − n) invalid values or trust that someone else did. The interest payments are validation code, tests for validation code, and the eventual production bug — "maybe it will crash your server? I guess we will find out later!"

**Don't:** Chase maximal type cleverness for its own sake.
**Why:** The goal is matching reality, not impressing reviewers. Evan explicitly prefers writing "a couple lines of code that are similar to other code" (a named custom type) over the more generic `Maybe (Float, Float)` — clarity for the team beats structural economy. If the model needs a paragraph to explain, it stopped matching how people think about the domain.
