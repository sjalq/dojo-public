---
triggers:
  - "user asks about versioning, breaking changes, or dependency management"
  - "user's ecosystem or platform keeps breaking downstream consumers"
  - "user asks how to build trust in a package registry, marketplace, or plugin system"
  - "user debates policy vs tooling for compatibility promises"
use_when:
  - "designing versioning and compatibility rules for anything with downstream consumers"
  - "deciding whether a guarantee should be enforced by tooling or by convention"
  - "building a package registry, plugin marketplace, or internal shared-library system"
fails_when:
  - "behavior changes under an unchanged interface — mechanical API diffing cannot see semantics; 'the meaning of a function may change even if its type does not'"
  - "there is one consumer and one producer on one team — ceremony without the trust problem it solves"
related:
  - "api-design-guidelines.md"
  - "designed-boundaries.md"
  - "saying-no.md"
  - "batching-and-releases.md"
---

# Enforced Semantic Versioning (trust via tooling, not promises)

## When to Use
- Designing version and compatibility policy for a platform, SDK, registry, or shared internal libraries
- Downstream consumers get broken by "minor" updates and trust is eroding
- Deciding what a marketplace should *guarantee* vs merely *recommend*
- Anywhere a promise is currently kept by author diligence and could be kept by a machine

## Fails When
- **Semantics shift silently.** Type-level diffing certifies shape, not meaning. A function that returns sorted results yesterday and unsorted today is a breaking change no signature-diff can catch — tests and changelog discipline still matter.
- **The trust radius is tiny.** Enforcement machinery pays off across many strangers; inside one small team, a conversation is cheaper.

## Core Concept

Semantic versioning is usually a social convention: authors *promise* that minor versions don't break you, and everyone knows the promise is kept unevenly. Evan Czaplicki's move was to make the machine keep it. He stated the goal in the original 2013 package-manager announcement: "Eventually, I'd like to automatically enforce semantic versioning by actually comparing APIs between versions and finding type changes and additional values." Elm shipped exactly that: `elm diff` compares any two published versions of a package and reports everything added, removed, and changed. From his Convergent Evolution talk: "when someone's publishing, I can say okay, I looked at your code, you have made major changes, this is the new version number that you will be using. And so it's not a matter of like, oh, do people get semantic versioning, do they like it or not — the Elm ecosystem uses semantic versioning, and if you're making a major change, everyone's going to get that major change. **There's no way to sneak through** like, well, I know it'll break people's code, but it doesn't feel important, it doesn't feel major." The guide lists the result as a headline language benefit: "automatically enforced semantic versioning for all Elm packages."

The general principle is bigger than versioning: **wherever trust currently depends on every author's judgment, see if a tool can make the good behavior mandatory.** A promise enforced by tooling is a property of the ecosystem; a promise kept by convention is a property of each author's mood that week. Elm could do this only because the language gave the tool something to analyze (typed, public APIs) — guarantees stack on guarantees (see designed-boundaries.md).

Why he cared so much about the package ecosystem at all: "Upstart languages live and die by their libraries." His case study is OCaml vs Haskell — similar roots, but "until 2013, OCaml did not have a way to share libraries... Without collaboration and sharing, the start-up costs to using OCaml remained constant," while Haskell's shared libraries compounded for a decade. His stated goals for Elm's registry were a design brief for any marketplace: "Encourage collaboration and experimentation, make sharing easy" — with the caveat that "having 9 terrible libraries is worse than having none. Now you have to try them all *before* writing your own" — "guide authors towards high quality APIs" (published design guidelines, docs required for publication), and "make it easy to use... most importantly, it should make every effort to avoid dependency hell!" Note the quality-over-quantity stance throughout: he wants "50 really nice packages" over 700,000 ("what can you make with ten thousand kitchens? Eggs.") — the registry's job is trust, not volume (see what-is-success.md).

## How to Apply

1. **List every promise your platform makes by convention.** "Minor versions don't break." "Plugins don't touch each other's data." "Docs exist." For each: could a machine check it at publish time?
2. **Enforce at the gate, not after the incident.** The check belongs where the artifact enters the ecosystem — publication, deployment, merge. `elm diff` runs when you publish, so a breaking change *cannot* wear a minor number, rather than being scolded afterward.
3. **Make the diff a first-class consumer tool too.** Anyone can run `elm diff` on any two versions and see exactly what changed — upgrade decisions become informed instead of faith-based. Expose your compatibility data, don't just act on it.
4. **Design APIs so the tool sees the truth.** Mechanical enforcement requires that the public surface *is* the contract: typed interfaces, opaque internals (see api-design-guidelines.md on hiding constructors so you can evolve without majors). Escape hatches that bypass the public surface blind the tool.
5. **Pair enforcement with editorial quality pressure.** Enforcement stops lies; it doesn't create quality. Design guidelines, mandatory documentation, and author attribution ("social tools can push quality higher, like clearly associating projects with authors") do the rest.
6. **Batch your own breaking changes.** Enforcement makes breakage *visible and honest*, not free — every major still taxes every consumer. Bundle them (see batching-and-releases.md).

## Examples

**Situation:** A company's forty internal services share a dozen libraries; every week someone's build breaks on a "patch" bump.
**Application:** Put an API-diff gate in the library publish pipeline: signature changes force a major version, additions force a minor, and the pipeline — not the author's judgment — assigns the floor. Publish the diffs so consuming teams can read exactly what changed before upgrading.
**Illustrative result:** "It didn't feel major to me" stops being a failure mode; upgrade trust becomes a property of the system rather than of individual authors.

**Situation:** A founder is building a plugin marketplace and drafting its rules as guidelines.
**Application:** Apply Evan's registry brief: decide what consumers must be able to trust (compatibility honesty, docs present, no undeclared capabilities), then enforce those at submission mechanically. Guidelines create averages; gates create floors. And optimize for a smaller set of excellent plugins over raw count — nine terrible options are worse than none.

**Situation:** A platform team relies on a CHANGELOG.md convention to communicate breaking changes.
**Application:** The changelog documents intent; the diff documents reality. Generate the compatibility report from the artifacts themselves and attach it to every release. Keep the changelog for the semantics the machine can't see — which is also the honest caveat to state: behavioral changes still need human words.

## Anti-Patterns (tactical)

**Don't:** Rely on authors' feelings about what "counts" as breaking.
**Why:** The sneak-through is rarely malicious — it's "doesn't feel important." Feelings don't compose across hundreds of authors and thousands of consumers; a compiler-checked contract does. The entire value of the system is that the judgment call is removed.

**Don't:** Build enforcement on a surface you let people bypass.
**Why:** If plugins can reach around the public API (reflection, private imports, direct DB access), the diff certifies a contract nobody is actually bound by. Enforced semver is a stacked guarantee: it works because the boundary underneath it is real. Close the boundary first (see designed-boundaries.md).
