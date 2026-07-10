---
triggers:
  - "user asks how to sell a technical product to businesses rather than developers"
  - "user asks why superior technology isn't being adopted"
  - "user is pricing a devtool or wondering why cheap isn't winning enterprise deals"
  - "user asks about platform strategy or competing with a platform default"
use_when:
  - "positioning a tool that competes with a platform's built-in default"
  - "translating developer benefits into terms a non-technical decision maker weighs"
  - "deciding pricing and go-to-market for productivity-class technology"
fails_when:
  - "the buyer actually is the developer — bottom-up, individual-developer adoption plays by developer rules"
  - "the product is a platform play itself — then marketplace economics, not productivity economics, apply"
related:
  - "economics-of-programming-languages.md"
  - "on-storytelling.md"
  - "what-is-success.md"
---

# Platform Languages vs Productivity Languages

## When to Use
- Positioning any tool whose competitor is "the default that comes with the platform"
- Preparing to pitch technology to executives, procurement, or a non-technical founder
- Setting a price for a productivity tool aimed at businesses
- Diagnosing why technically-superior tech loses adoption fights

## Fails When
- **Adoption is genuinely bottom-up.** Where individual developers choose their own tools, developer-facing arguments (and free tiers) still rule; the business-person analysis applies where decisions ride up the hierarchy.
- **You mistake which game you're in.** If your product *is* the marketplace, you want platform-language economics — maximum accommodation, maximum size — not productivity-language focus.

## Core Concept

Evan Czaplicki's Lambda Days 2025 keynote reframes technology adoption around a person most builders never model: **"the final boss of adoption is the non-technical business person."** Developers don't decide which languages are used; even supportive CTOs "have to make their decisions along with their other executives; they change jobs." At the end of every chain "there's going to be someone looking in an Excel spreadsheet and crossing off the fundamental investments in their own business."

His two categories. A **platform language** is "the language that's built into a specific digital marketplace" — JavaScript in the browser, Swift in the App Store, C on the desktop. From the business person's view the browser isn't a browser: "This is a digital marketplace. We're not surfing the web. We're connecting buyers and sellers." The genius of platform-language economics is that **the cost never appears on the buyer's budget** — it is taken out *before* revenue arrives, via the app-store commission and ad spend that becomes traffic acquisition cost. "These languages are getting paid for without the business people even knowing that it's part of their budget," and business success automatically funds the language: "There's no reality where you outgrow them." Design follows: marketplaces want every kind of business, so platform languages "add many features and have companies use their preferred subset — it's better to have a complex language than to have a business switch to an alternative marketplace."

A **productivity language** "makes development more efficient than using the underlying platform language directly" — Elm over JavaScript. It doesn't need the whole market: "if for a certain type of business we can make them 20% more effective, that's great. If it doesn't work at all for some large class of other businesses, that's not a problem for us." But it has no invisible funding, so it must either **compete on price** (free — which raises the buyer's real questions: "Can it support our needs as we grow? Who do I call if something goes wrong? Will I be able to get support in 10 years? Adobe Flash did stop existing") or **appear on the budget** as a paid productivity tool, the JetBrains/Kotlin route — the only place businesses already knowingly pay for developer-productivity technology.

Two buyer-psychology findings he flags, with sources. From a Silicon Valley adoption book he says he doesn't particularly like ("but it's a good way of learning how Silicon Valley people see themselves"): the pragmatist buyer, unlike the visionary chasing "a quantum leap forward," wants "incremental, measurable, predictable progress... the word risk is negative in their vocabulary." From Hermann Simon's *Confessions of a Pricing Man*: **price signals quality** — a cloud firm priced at a fifth of the competition found "larger companies think our price point is so low that they have no faith in our product." Evan's field version: a European financial-institution contact told him a foundational technology "can't even get on the desk of the person who will decide unless it costs €60,000 a year" — partly accountability theater, partly a real signal ("I assessed this area as important and invested accordingly"). And the language must change: "the business person doesn't really know what a runtime error is. They say, I don't care if there's a million or a thousand or zero. I care if it's released in Q2." The translations that land: deliver features faster, less time on bug fixing, retain developers longer — "obviously this is extremely off-putting to developers, but the purpose is to define the challenge."

His resolution sketch: take the *organizational* perspective, not just the technical one — authors produce quality, developers produce for businesses, businesses fund a healthy environment for authors, "we all grow stronger together." He looks to cultures that do this without Silicon Valley's values: the long-lived Japanese companies of a Bank of Korea longevity report — century-old firms like Nintendo and Kongo Gumi (trust over generations, "thing making is people making," the insect strategy of staying deliberately small) and Danish agricultural cooperatives (small producers pooling well-defined capital investments and shared quality marks). "Silicon Valley values aren't inevitable... move fast and break things isn't suitable for language design — you can't move fast and break things in the foundation of the building."

## How to Apply

1. **Identify the real decision maker and their spreadsheet.** Trace who ultimately approves the fundamental-technology line item. That person's vocabulary — risk, support, Q2, references — is the one your pitch must speak.
2. **Classify your product: platform or productivity.** If you're a productivity play, accept the two consequences: you must be dramatically better for a *specific* class of user (not somewhat better for everyone), and you must choose how you appear (or don't) on the buyer's budget.
3. **Translate every technical claim into business outcomes.** "No runtime exceptions" becomes "less time on tests and bug fixes, features ship on schedule." Collect the case-study evidence buyers want: hiring, retention, delivery — "I don't care technically what happened, but how did it work for hiring? What was retention?"
4. **Price as a signal, not just as economics.** For enterprise-critical technology, a too-low price can *disqualify* you — the buyer needs the price to certify seriousness and to buy accountability. Consider the dual model: free open core plus a paid product the balance sheet understands ("salary for open source engineer" gets crossed off; a tool license reads as free money).
5. **Answer the risk questions before they're asked.** Growth support, support contract, ten-year story. The pragmatist buyer's checklist is knowable in advance; a productivity vendor without written answers loses to a worse product that has them.
6. **Organize for continuity.** Scattered part-time in-house efforts lose talent, knowledge, and strategy ("the work can get lost easily... there's no mechanism for that knowledge to be passed on"). Pool them — cooperative structures, shared roles, real careers for the people your ecosystem depends on.

## Examples

**Situation:** A founder selling a reliability-focused framework keeps winning developer enthusiasm and losing executive sign-off.
**Application:** The pitch is stuck in developer language. Rebuild it for the final boss: delivery predictability, bug-fix cost, retention, references — plus written answers to "who do I call" and "where are you in 10 years." Consider whether a paid support tier exists mainly so the buyer has something to point to when assigning risk.
**Illustrative result:** The same technology clears procurement because the buyer can now defend the decision in their own hierarchy's terms.

**Situation:** A devtools startup prices its enterprise plan at $99/month to undercut a $500/month incumbent.
**Application:** Simon's warning applies: below a threshold, price reads as no-faith. If the tool is foundational to the buyer's business, the low price may keep it off the decision maker's desk entirely. Price to the value class and the accountability the buyer is purchasing, and let the free tier serve the bottom-up motion separately.

**Situation:** An indie language author is discouraged that adoption plateaued despite technical superiority.
**Application:** Superiority is a developer argument; adoption above a certain company size is a business decision funneled through people who will never run the compiler. Either target the niche where bottom-up choice rules (and be content with it — see what-is-success.md), or build the organizational apparatus the business buyer requires. Choosing neither is choosing the plateau.

## Anti-Patterns (tactical)

**Don't:** Pitch a non-technical decision maker on technical mechanisms.
**Why:** "If between me and the release there's a million runtime exceptions or a billion — I don't know what that is. I want it in Q2." The mechanism is your evidence, not your message; the message is delivery, cost, and risk in their units.

**Don't:** Treat "free" as an unambiguous advantage in enterprise sales.
**Why:** Free moves the cost from the budget line (visible, defensible, cancellable) to invisible risk the buyer personally carries. Platform languages get away with invisible cost because a trillion-dollar marketplace stands behind them; a small vendor offering free carries the same invisibility with none of the reassurance — and gets crossed off by the person with the spreadsheet.
