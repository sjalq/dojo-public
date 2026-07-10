---
triggers:
  - "user asks how to structure application state or a frontend app"
  - "user asks about The Elm Architecture, Model-View-Update, or Redux-style state management"
  - "user is debating component hierarchies vs a single state tree"
  - "user asks how a pattern should scale as an app grows"
use_when:
  - "designing the state and update flow of an interactive product or tool"
  - "a team is arguing about where state should live and who is allowed to change it"
  - "evaluating whether to adopt a unidirectional data-flow pattern"
fails_when:
  - "the platform genuinely fights the pattern — forcing unidirectional flow onto a system built around local mutable widgets creates friction instead of clarity"
  - "used as a ritual — splitting code into Model/Update/View *files* instead of building around the data"
related:
  - "the-life-of-a-file.md"
  - "culture-shock.md"
  - "designed-boundaries.md"
  - "types-as-sets.md"
---

# The Elm Architecture (Model-Update-View)

## When to Use
- Structuring any interactive program: web app, game, tool, dashboard
- Deciding where state lives, who may change it, and how changes propagate
- A team keeps producing synchronization bugs — two copies of "the same" data drifting apart
- Someone asks "which state management library should we use?" before asking what the state *is*

## Fails When
- **You force it onto a component-object platform.** If your ecosystem's primitives are stateful widgets with their own lifecycles, imposing a single state tree everywhere can mean constant impedance mismatch. Evan's own point about design is that features must form a coherent whole; a pattern lifted out of its constellation loses much of its value.
- **You treat it as a file layout.** Splitting a codebase into `Model/`, `Update/`, `View/` directories is explicitly an anti-pattern — the boundaries become ontological debates ("what *is* an estimatedReadTime, really?").
- **You expect it to answer product questions.** It structures state and change; it does not tell you what to build.

## Core Concept

The Elm Architecture is a pattern for interactive programs that breaks every application into three parts: a **Model** (the state of your application), a **View** (a way to turn state into what the user sees), and an **Update** (a way to change state based on messages). The program renders the model; the world sends back messages — "they clicked a button!" — and the update function produces the next model. The cycle goes round and round. Every change to state flows through one place, as data, in one direction.

What makes its origin unusual is that Evan Czaplicki did not so much invent it as *observe* it. In his words from the official guide: "This architecture seems to emerge naturally in Elm. Rather than someone inventing it, early Elm programmers kept discovering the same basic patterns in their code. It was kind of spooky to see people ending up with well-architected code without planning ahead!" At a retreat he watched a student who had never done functional programming build a game in a week and end up with the same shape — that was the moment it got a name. When Facebook independently promoted Flux and later Redux emerged citing Elm directly, Evan read it as convergent evolution: two ecosystems arriving at unidirectional flow separately, which is strong evidence the idea itself is sound. (Credit flows one way: Redux's docs credit The Elm Architecture; TEA did not come from React.)

The deeper principles under the pattern are worth more than the pattern itself. First, **single source of truth**: there is exactly one copy of the state, so it cannot get out of sync with itself. Second, **changes are data**: every possible interaction is an explicit message in a finite list, so you can read the `Msg` type and know everything that can happen to this program. Third, **the world talks to you through messages you subscribed to**, not through callbacks that mutate things behind your back — subscriptions "let components sit around and wait for messages while library code handles a bunch of tricky resource management stuff behind the scenes."

## How to Apply

1. **Write the Model first, and make it honest.** The model is the set of situations your program can actually be in. Design it with the same care you would give a database schema — this is where most architecture actually happens (see types-as-sets.md).
2. **Enumerate the messages.** List every way the state can change: `PressedEnter`, `ChangedDraft String`, `ReceivedMessage {...}`. If you cannot name the message, you do not yet understand the interaction.
3. **Make update the only door.** All state change goes through one function that maps (message, model) to a new model. Nothing else writes state. In a review, hunt for the second door — that is where the bugs live.
4. **Keep functions out of your state.** From Evan's sortable-table design notes: "One of the core rules of The Elm Architecture is never put functions in your Model or Msg types. It may cost a little bit of extra code to model everything as data, but the architecture and debugging benefits are worth it."
5. **Scale by growing, not by componentizing.** When the app grows, grow the update and view functions, extract helper functions, and split modules around data structures when they earn it — not around visual regions of the screen (see the-life-of-a-file.md).
6. **Own as little state as possible in reusable pieces.** In the sortable-table library, the table state tracks only sorting details; the data itself is passed to view. "Having multiple copies of 'the same' value in your Model is a sure way to create synchronization errors."

## Examples

**Situation:** A team's dashboard has a table widget that caches its own copy of the row data, and users report the table showing stale entries after edits.
**Application:** This is the exact failure Evan designed against in elm-sortable-table. The table's state should track only display details (which column is sorted); the rows are an argument to view, owned by the single model. "This choice means you can change your data without any risk of the table getting out of sync."
**Illustrative result:** The stale-data class of bug becomes structurally impossible instead of carefully avoided.

**Situation:** A founder asks which of three state-management libraries to adopt for a new product.
**Application:** Refuse the library question first. Write down the model — what states exist, what messages change them. Once the state and its transitions are explicit data, the library choice is usually obvious or unimportant. The pattern predates and outlives any particular package.

**Situation:** Debugging a hard-to-reproduce bug reported by QA.
**Application:** Because every change is a message and state is one value, the whole session is replayable. Evan built Elm's time-traveling debugger on exactly this: export the message history, import it on another machine, and step through. If your architecture cannot do this even in principle, changes are leaking around the update function.

## Anti-Patterns (tactical)

**Don't:** Create a Model/Update/View module *per visual component*, each with its own local state, wired together with parent-child message forwarding.
**Why:** "Actively trying to make components is a recipe for disaster" — components are local state plus methods, which is objects, which is a different paradigm. You end up building an object system by hand out of a functional pattern, with all of the wiring and none of the benefits. Write a `viewSidebar` *function* and pass it what it needs; add state to the one model only when it truly exists.

**Don't:** Split code into separate `Model`, `Update`, and `View` modules for the whole app.
**Why:** Boundaries become debatable. When `estimatedReadTime` is used by both update and view, placing it is an ontological argument, and "all of your colleagues have different theories." Build modules around types instead; the architecture is a shape within a module, not a filing system across modules.
