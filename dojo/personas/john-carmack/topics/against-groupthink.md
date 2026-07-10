---
triggers:
  - "user asks how to differentiate in a crowded field or research area"
  - "everyone in an industry is converging on the same approach"
  - "user asks whether to follow the dominant paradigm or bet against it"
  - "user's benchmark or evaluation seems designed to flatter their own method"
use_when:
  - "positioning work in a field where all major players draw from the same talent pool and ideas"
  - "deciding whether a contrarian technical direction is worth pursuing"
  - "designing evaluations that won't be gamed by their designers"
fails_when:
  - "contrarianism becomes the goal — being different from a correct consensus is just being wrong"
  - "the random test point has no rigor — decorrelation without competence explores nothing"
related:
  - "expected-value-career-bets.md"
  - "agi-from-experience.md"
  - "demonstration-over-paperwork.md"
  - "learn-by-rewriting.md"
---

# Be the Random Test Point

## When to Use
- An entire field is converging: same training pipelines, same benchmarks, same architectural fashions, releases within months of each other
- Deciding where your small team can matter against giants with a thousand times your budget
- Reviewing an evaluation, benchmark, or success metric designed by the people it will judge
- A promising unfashionable idea is being dismissed mainly because it's unfashionable

## Fails When
- The consensus is consensus because it's demonstrably right — decorrelating from measured truth isn't strategy, it's error
- Your "different path" is different only in branding — same methods, same benchmarks, a contrarian press release
- You decorrelate on everything at once — a useful test point varies deliberately against a rigorous baseline, not chaotically

## Core Concept

Watch the frontier AI labs for a year and you see something strange: one releases an image generator, then the next, then the next, all within a couple of months of each other. Everyone can reproduce everyone else's work because everyone draws from the same academic researcher pool — enormous brain trust, brilliant people, cross-pollinated into sameness. That's fine when the destination is known and the race is execution. It's dangerous when nobody actually knows the way — and in genuinely open problems, nobody does. Machine learning itself has the honest metaphor: when you don't know the loss landscape, you need a degree of randomness — random weights, random starting locations, ensemble models — precisely because we're not sure we're in the attractor basin where gradient descent reaches the solution. So I am positioning myself as one of these random test points. The rest of the industry is heading somewhere that leads to fabulous places, and they're doing a great job. But if the basin is wrong, every one of those brilliant people arrives at the same local minimum together.

Being a useful test point has requirements — this is not licensed contrarianism. First, decorrelation has to be real: different background (I'm a systems engineer, not an academic), different constraints, different sources — I go mining decades-old research that failed on one-megahertz machines and might work at modern scale, because ideas that died of hardware starvation aren't dead, they're waiting. Second, you keep full respect for the mainstream: I follow it closely and use its tools daily, because the point is to be decorrelated from the consensus, not ignorant of it. Third — and this is the part most people skip — you handicap yourself honestly. I tell my investors there's a non-negligible chance I figure out some important pieces, not that I'll win. A random test point that oversells itself is just noise with a pitch deck.

The same disease has a second face: fields converge not only on methods but on the tests that judge the methods. Anytime a researcher builds their own benchmark, their own environment to play in, there is an unavoidable bias to not do the things that will be hard for their own algorithm. It isn't dishonesty; it's gravity — you've got your problem you're trying to solve, and the inconvenient side effects quietly fall out of scope. Whole fields can grade themselves on exams they wrote for themselves. The corrective is external, unbiased evaluation the designer can't tune: we settled on the full diversity of a hundred-plus Atari games — born in Alberta, underpinning the field, and conspicuously not built by us — and then pushed it further into physical reality, where nothing can be quietly redefined. Whether you're in research or product: if your success metric was designed by the people it measures, assume it flatters them, and go find the test that wasn't.

## How to Apply

1. **Map the correlation first.** Where do your field's players get their people, ideas, and evaluations? If everyone shares all three, the unexplored space is large and the crowd's redundancy is your opportunity — five labs doing the same thing are worth about one lab.

2. **Choose your axis of decorrelation deliberately.** Different training data of ideas: old literature, adjacent fields, your own unusual background. Vary the axis where you have a real edge; stay mainstream everywhere else. Decorrelated on one dimension with rigor beats weird on five without it.

3. **Track the mainstream you're diverging from.** Read it, use its tools, respect its results. The value of your test point is measured against their baseline; lose the baseline and you can't even tell whether you're exploring or lost.

4. **Adopt evaluations you didn't build.** Pick the external benchmark, the standard the field already trusts, the physical test that can't be tuned. If you must build the benchmark, have someone with opposite incentives try to break it before you trust it.

5. **State your odds like a test point, not a prophet.** "Probably wrong, worth running" is the honest pitch for decorrelated work — and it's fundable, because the portfolio logic is real: someone should be checking the other parts of the solution space.

## Examples

**Situation:** A three-person ML startup is deciding whether to compete on large language models against the frontier labs.

**Application:** Map the correlation: the giants share talent pools, architectures, and evals, and can each reproduce the others' work in months — a three-person team correlated with that crowd is a rounding error. The play is the unoccupied space: approaches the consensus has collectively agreed not to try, old ideas that failed for scale reasons that no longer exist, problem framings the benchmark culture doesn't reward. Pick one axis, keep everything else boring, and state the honest odds.

**Illustrative result:** The startup stops being the smallest runner in the biggest race and becomes the only runner on its path — most such paths dead-end, which is exactly why the crowd's blind spot is cheap to explore and why finding anything there is worth so much.

**Situation:** A product team celebrates that their new recommendation engine wins on their internal quality benchmark, which the same team defined last quarter.

**Application:** Name the structural bias: designers of a benchmark unavoidably avoid what's hard for their own system, so the win is partially circular. Get an evaluation the team can't tune — blind comparisons run by outsiders, an external standard, or the physical-Atari equivalent: real users, real sessions, metrics defined before the system existed.

**Illustrative result:** The external test comes back less flattering than the internal one — nearly always — and the gap between the two numbers becomes the roadmap: it's a measured list of exactly what the team had been unconsciously avoiding.

## Anti-Patterns (tactical)

**Don't:** Wear contrarianism as identity and dismiss the mainstream you've decorrelated from.
**Why:** The mainstream is mostly right — that's how it became mainstream — and its tools and results are the baseline that gives your divergence meaning. I'm a daily user of the technologies whose research direction I'm betting against. A test point that stops tracking the consensus can no longer tell exploration from error, and usually it's error.

**Don't:** Grade your bold new direction on an evaluation you designed after seeing your results.
**Why:** That's the researcher-benchmark bias in its purest form — the test grows around the answer, hard cases fall out of scope, and you become the field-of-one that flatters itself. Fix the evaluation before the experiment, prefer tests built by people who don't care if you succeed, and treat any metric you can quietly redefine as no metric at all.
