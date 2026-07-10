---
triggers:
  - "user asks about interop, FFI, escape hatches, or integrating with a legacy system"
  - "user is pressured to add a bypass 'just this once' to a system with guarantees"
  - "user designs the boundary between a safe core and an unsafe outside world"
  - "user asks why a platform restricts direct access"
use_when:
  - "designing how a system with strong guarantees talks to systems without them"
  - "deciding whether to allow direct bindings/escape hatches or message-passing at a boundary"
  - "weighing short-term adoption speed against long-term properties"
fails_when:
  - "the guarantees being protected aren't actually valuable to your users — a hard boundary defending nothing is just friction"
  - "survival requires adoption now — the longer, harder path assumes you can afford the longer part"
related:
  - "no-runtime-exceptions.md"
  - "enforced-semver.md"
  - "saying-no.md"
  - "the-elm-architecture.md"
---

# Designed Boundaries (ports and the limits of interop)

## When to Use
- Deciding how a typed/pure/validated core integrates with untyped, legacy, or third-party code
- Someone requests a direct escape hatch through your system's guarantees
- Designing a plugin, extension, or integration surface for a platform
- Evaluating a technology by how it treats its boundary with the messy world

## Fails When
- **Nobody bought the guarantees.** The boundary's cost is only justified by the property it protects. If users don't value the property, the friction is pure loss — know which product you're building.
- **You need the ecosystem's speed today.** Refusing to piggyback on an existing ecosystem is a decades-bet. Evan is explicit that it trades short-term growth away; a project that dies young collects nothing on the long position.

## Core Concept

Elm made one of the most contested design decisions in modern languages: **no foreign function interface to JavaScript.** "It is not possible to call arbitrary JavaScript functions at any time." Instead, JavaScript is treated like a separate service you exchange messages with — ports work "as client-server message passing" through a small, explicit, typed channel. Evan's guide chapter on the limits of interop is the clearest statement anywhere of *why you refuse an escape hatch*, and it doubles as his advice to any system designer.

Two reasons for refusing direct bindings. First, **losing guarantees**: "One of the best things about Elm is that there are entire categories of problems you just do not have to worry about. There are no surprise exceptions to catch, and functions cannot mutate data in surprising ways. I think this is the core value of Elm over alternative languages, but if we can call JS directly, all that goes away. Does this package produce runtime exceptions? When? Will it mutate the values I give to it?... Will it send messages to some 3rd party servers? Log passwords?" A guarantee that holds *almost* everywhere is not a guarantee; every consumer must resume auditing everything. Second, **package flooding**: with an open FFI, "in the two years before elm/html existed, I am sure someone would have contributed jQuery bindings if it was possible" — the ecosystem fills with thin wrappers around the host platform, and the chance to design libraries native to the new model is lost forever.

The refusal buys compounding long-term properties: packages "designed for Elm" rather than ported; portability ("if the compiler someday produces x86 or WebAssembly, the whole ecosystem just keeps working"); security ("Elm packages can guarantee that entire categories of exploits just cannot happen, reducing auditing cost"); and optimization freedom (the compiler can change calling conventions and representations because no external code depends on them). His time horizon is the tell: "This is definitely a longer and harder path, but **languages live for 30+ years.** They have to support teams and companies for decades, and when I think about what Elm will look like in 20 or 30 years, I think the trade-offs that come with ports look really promising!"

Just as instructive is *how he holds the position*: with explicit, non-defensive honesty about the trade. "This has tradeoffs that some people really love, but it is not for everyone!... I highly encourage you to look through these interop examples to get a feeling for whether flags, ports, and custom elements can cover everything you need... There are many alternative languages that have a traditional FFI instead, and I encourage you to look into those languages if you think that path might be better." He names the cost ("Elm cannot piggyback on the JS ecosystem to gain more libraries more quickly") and actively helps people select themselves out — especially commercial evaluators. A principled no with a stated why, a stated cost, and a recommended alternative is the full pattern (see saying-no.md).

## How to Apply

1. **Name the guarantee your boundary protects.** Write the sentence: "inside this line, X cannot happen." If you can't write it, you don't have a boundary — you have a preference.
2. **Choose message-passing over direct bindings at the trust line.** Data crossing the boundary is validated once, explicitly, into honest types (see types-as-sets.md); the unsafe side is treated like a remote service, even if it's in the same process. No caller inside can reach through.
3. **Refuse the "just this once" hatch, and say why.** The first exception converts your guarantee from a property into a probability. Answer with the enumeration: here's what every user of the system loses if this exists (see hard-parts-of-open-source.md on "why don't you just").
4. **Price the decision on a decades clock.** Ask what the system must look like in 10-30 years, and which choice compounds: piggybacking gains speed now and locks you to the host platform's shape forever; the designed boundary is slow now and free later.
5. **Publish the trade honestly.** Document what the boundary can't do, show worked examples of living within it, and name the alternatives for people it doesn't fit. Self-selection up front is cheaper than churn and resentment later.
6. **Keep the boundary small and inspectable.** The fewer crossing points, the cheaper the audit and the more portable the core. "The smaller the interface between Elm and JS, the easier it will be to support other platforms."

## Examples

**Situation:** A platform team built a validated, typed core service; a product team requests direct database access "temporarily" to hit a deadline.
**Application:** This is the FFI request. Enumerate what the hatch costs everyone: every invariant the core enforces becomes unverifiable, every future migration must consider an unknown consumer, every audit widens. Offer the ports equivalent — a message-level API added for their use case, fast-tracked — and put the refusal's *why* in writing where the next requester will find it.
**Illustrative result:** The core's guarantees stay global; the product team's need is met through a door that can be maintained instead of a hole that can't be closed.

**Situation:** A startup building a new runtime debates bridging the entire npm ecosystem for launch-day credibility.
**Application:** Weigh package flooding explicitly: the bridge fills your ecosystem with wrappers shaped like the old platform, and your optimization and portability options close. If your core value *is* a guarantee the old ecosystem can't offer, the bridge sells it off. If your core value is convenience, take the bridge — but then guarantees are no longer your pitch. The mistake is claiming both.

**Situation:** An enterprise evaluating a guarantees-heavy technology asks "but what if we need some library it doesn't have?"
**Application:** Evan's own move: don't reassure — route them to the examples and let them check coverage against their actual needs before committing. "This is especially important if you are considering [it] for commercial use!" A boundary sold honestly retains the users it fits.

## Anti-Patterns (tactical)

**Don't:** Grant the escape hatch quietly to your biggest customer and keep advertising the guarantee.
**Why:** The guarantee is now false, and its falseness is invisible until it fails publicly. Every downstream user is still paying the boundary's costs (friction, missing bindings) while the property they paid for no longer exists. Either the boundary holds for everyone or reprice the product around its absence.

**Don't:** Defend the boundary with ideology instead of the enumerated trade.
**Why:** "Because purity" persuades nobody and ages badly. Evan's version works because it lists concrete gains (security, portability, optimization, ecosystem coherence), concedes the concrete cost (slower library growth, not for everyone), and gives the skeptic a respectful exit. Boundaries survive on demonstrated value, not on doctrine.
