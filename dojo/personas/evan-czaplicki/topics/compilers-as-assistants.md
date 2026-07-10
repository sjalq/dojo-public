---
triggers:
  - "user asks how to improve error messages, validation feedback, or diagnostics"
  - "user is designing developer tooling, a CLI, a compiler, or an API's failure modes"
  - "user asks why beginners give up on their product or docs"
  - "user wants a review of onboarding or error-handling UX"
use_when:
  - "any tool, product, or process delivers failure feedback to a human and you control what that feedback says"
  - "support tickets or drop-off cluster around the same confusing failure"
  - "deciding how much to invest in polish on the unhappy path"
fails_when:
  - "the audience is a machine, not a human — logs for automated consumers need structure, not empathy"
  - "hints are guesses — a wrong hint is worse than no hint because users trust it"
related:
  - "gradual-learning.md"
  - "api-design-guidelines.md"
  - "no-runtime-exceptions.md"
  - "on-storytelling.md"
---

# Compiler Errors as User Experience / Compilers as Assistants

## When to Use
- Designing or reviewing error messages, validation output, failure states, or diagnostics anywhere in a product
- A tool is technically correct but users say it "feels" hostile or confusing
- Prioritizing: wondering whether unglamorous feedback-quality work is worth the time
- Beginners churn early and you suspect the first failure experience is the cliff

## Fails When
- **Feedback is consumed by machines.** Structured output for scripts and pipelines needs a stable schema; prose kindness is noise there. (Elm solved this by adding `--report=json` — serve both audiences separately.)
- **You hint without confidence.** A specific suggestion that is wrong sends the user down the wrong path with your authority behind it. Only ship hints for mistakes you can actually recognize.
- **Polish substitutes for prevention.** If the same error fires constantly, the design upstream is the problem (see gradual-learning.md).

## Core Concept

Evan Czaplicki's most widely copied idea is that a compiler's error messages are a designed product, not an exhaust pipe. His 2015 essay opens by taking the complaint seriously: "A lot of compiler error messages actually *do* suck. Some of them suck quite a lot. What happens when we accept that there is a problem here and try to do better?" The answer, from his own experiment: "you can make a shockingly huge difference just by thinking about the user experience." The stance is compressed into one line from the Elm 0.16 announcement: **"Compilers should be assistants, not adversaries."** A tool should not just *detect* a problem — it should help you understand *why* it is a problem and what to do next. "Whether you are using a compiler or interpreter, nobody wants a confusing and rude gatekeeper."

The reason this work is chronically underinvested is **survivorship bias**, which he laid out in "The Syntax Cliff": failures concentrate in a user's first weeks, exactly when they are most vulnerable. "When a beginner asks themselves why something is hard, it is easy to think, 'Because I am bad at it!'" The people who fall off the cliff quit — so they are not in your forums, your meetups, your issue tracker. "People who fall off the cliff cannot share their perspective... They quit! They are not in those places!" Every feedback channel you have oversamples survivors, so the pain of the failure experience is systematically invisible to the people who could fix it. He only understood the magnitude after creating the error-message-catalog, a repo that solicits confusing errors — a mechanism that "legitimizes the idea that error messages should be better" so a broader range of people speak up.

The economics are the most quotable part: he found that generating dramatically more specific type errors "required no significant changes to the type inference algorithm and imposed no noticeable performance cost... I was shocked to find out that such huge improvements could be made nearly for free." The hard part was never technical. It was deciding the user's emotional experience was in scope.

## How to Apply

1. **Show the user exactly what they did, not your internal representation.** Elm's errors show "the code exactly as you wrote it" with real line numbers, because pretty-printed reconstructions force a mental translation. Users should be able to ask "does this look like that?" without conscious analysis. In your product: echo the actual input, the actual field, the actual request.
2. **Translate from your failure to their intent.** "These two types do not match" describes what went wrong *for the compiler*. The user needs to know what it means for *their* code. Every message should carry a specific, contextual hint — Elm added typo detection, "expected vs actual," and beginner hints for predictable mistakes (trying `+` on strings, truthiness).
3. **Use layout and color as information design.** Red marks the problem, blue separates messages, general context above the code, detail revealed below as needed. Reading errors is reading; design it like prose.
4. **Kill cascading errors.** One mistake should produce one message, not four messages the user must triage. Elm eliminated cascades entirely; the fix came from a Hacker News comment — "simple implementation, no performance penalty."
5. **Build a complaint channel for confusion.** The error-message-catalog pattern: actively solicit confusing failures as first-class bug reports. "We can only fix things if we know about them." This is your only defense against survivorship bias.
6. **Aim for "teacher," not "referee."** The 0.19.1 syntax errors give examples and link to explanations: "My hope is that the new compiler feels more like a teacher, showing helpful and relevant examples when you get stuck." The failure moment is a teaching moment — the one time you have the user's full attention.

## Examples

**Situation:** A SaaS API returns `400: validation failed` and the founder wonders why integration support tickets are so high.
**Application:** Apply the three Elm moves: echo the offending field and value as the developer sent it; state what was expected versus what arrived; add a hint for the most common mistake ("dates must be ISO 8601 — you sent `07/10/2026`; try `2026-07-10`"). Then open a catalog: every support ticket about a confusing error becomes an issue against the error text itself.
**Illustrative result:** The class of ticket that is really "your error message was unreadable" stops arriving; the ones that remain are genuine edge cases.

**Situation:** A CLI tool for internal developers dumps a stack trace on misconfiguration.
**Application:** The stack trace is the compiler being "angry" in its own terms. Catch the known failure, name the config key, show the line of the config file as written, suggest the two most likely fixes, and link the doc page. Keep the trace behind a `--verbose` flag for the machine-debugging case.

**Situation:** A team debates whether error-polish work justifies a sprint versus new features.
**Application:** Evan's evidence cuts the debate two ways: the cost is usually lower than assumed ("nearly for free" once the information is threaded through), and the benefit is invisible in your metrics because the people it would save have already quit. Price in the survivors you cannot see.

## Anti-Patterns (tactical)

**Don't:** Write error messages that describe the internal failure ("constraint violation in resolver step 3") and assume documentation will bridge the gap.
**Why:** You are making the user do the translation your tool should do. The gap between "what went wrong for the system" and "what it means for the human" is exactly where people conclude they are bad at this and leave — and they will not file a bug on their way out.

**Don't:** Prioritize error quality by counting complaints.
**Why:** Survivorship bias guarantees the count is wrong. The worst failures produce silence, not tickets. "Everyone is telling me to work on something else" — and "everyone" is a very particular, non-random sample of people who made it through.
