---
triggers:
  - "user guards array[0] or uses find then null-checks critical data"
  - "user needs at least one item (primary account, first flag, head of list)"
  - "user mixes currencies, units, or other product fields that must match"
  - "user asks about NonEmptyArray, head safety, or TypeScript indexed access types"
  - "business rule is only enforced by throw at runtime after half-typed models"
use_when:
  - "domain requires one guaranteed element plus optional rest"
  - "combining two product values where a field (currency, unit, brand) must agree"
  - "pushing invariants into types so total functions get better inputs"
  - "replacing scattered empty-array and mismatch checks"
fails_when:
  - "empty really is valid and you force NonEmpty everywhere out of cargo cult"
  - "you encode constraints the type system cannot hold without lying casts"
  - "you use indexed types only as clever syntax, not to encode a real rule"
related:
  - "product-and-union-types.md"
  - "pure-and-total-functions.md"
  - "smart-constructors.md"
  - "schema-at-the-boundary.md"
  - "typestate-and-capabilities.md"
---

# Non-Empty Collections and Indexed Types

## When to Use

- Critical data lives in an array you cannot guarantee is non-empty: multi-account UIs, "important item first, rest later," feature-flag lists that must have a default.
- Code is full of `if (data[0])`, `data.find(...)`, and optional chains because the type is `Array<T>` and the domain is "at least one T."
- Two values of the same product shape must share a field (same currency money, same unit metrics, same brand of ID family) and today that is a runtime `if` + throw.
- You are totalizing functions: better input types (non-empty, same-currency) beat returning nonsense or throwing from "pure" helpers.

## Fails When

- Empty collections are legitimate and you stamp `NonEmptyArray` on every list to look advanced. That just pushes lie-casts to construction sites.
- You need full dependent types (value-level proofs everywhere). TypeScript indexing and generics are dependent-ish, not Idris. Encode the rules they can actually hold.
- Construction of non-empty or same-currency values is forgeable with `as` and no boundary parse. The type becomes theater.

## Core Concept

The Big 3 (branded "a thing", product "this AND that", union "this OR that") get sharper when you add **type parameters**. Generics are not academic decoration; they are how you say "at least one Account" or "Money in currency C" instead of "array of stuff" and "money maybe."

### Non-empty collections

Arrays often hold critical data yet cannot promise contents. Callers null-check heads forever. Two practical encodings:

**Product with guaranteed head:**

```ts
type AtLeast1<T> = {
  item: T
  data: Array<T>
}

type AtLeast1Account = AtLeast1<Account>
// item always present; data may be empty
```

**Tuple head + rest (NonEmptyArray):**

```ts
type NonEmptyArray<T> = [T, ...Array<T>]

const empty: NonEmptyArray<string> = [] // does not compile
const hasOne: NonEmptyArray<string> = ["🐮"] // ok
```

Use cases: customer must have a primary account plus optional others; UI always has a selected tab; batch job always has a first row to define schema. Non-empty lists are classic FP data-structure thinking; the TS tuple form is a pragmatic encoding, not a new invention.

Once the type says "at least one," `head` is total for that type. You stop writing the same empty guard in five modules. Prefer constructing non-empty at the boundary (schema, smart constructor) so domain functions receive already-valid shape.

### Indexed types (dependent-ish TypeScript)

You know how to read object fields at runtime: `person.first` or `person["first"]`. TypeScript also lets you **index into types**:

```ts
type Person = { first: string; age: number }
type First = Person["first"] // string
```

That matters when two products combine and a business rule lives in a field relationship. Money is the teaching example:

```ts
type Money<C> = {
  currency: C
  amount: number
}

// Library-style half-typing: still throws at runtime
function add(a: Money, b: Money): Money {
  if (a.currency !== b.currency) throw new Error("currency mismatch")
  return { currency: a.currency, amount: a.amount + b.amount }
}

// Rule in the type system: both must share C
function add<C>(a: Money<C>, b: Money<C>): Money<C> {
  return { currency: a.currency, amount: a.amount + b.amount }
}
```

Same pattern for Metric vs Imperial temperatures, account migration maps, or any "these two records must agree on axis X." Indexing and generics let you query and refine product fields when combining values. Jesse contrasts this with money libraries that explode at runtime rather than fully encoding currency equality (e.g. dinero-style APIs that check later).

TypeScript nuance: sometimes inference unions `C` incorrectly; `NoInfer` on a parameter can keep the first argument's currency from widening. That is a compiler detail, not a reason to abandon the pattern.

### How this feeds total functions

Partial functions throw or return nonsense for some inputs. One way to totalize is **better inputs**: `Divide` with `PositiveInteger` denominator; `average` over `NonEmptyArray<number>`; `add` only same-currency money. The other way is `Result` on failure. Prefer constraining the type when the domain truly forbids the bad case; use Result when failure is expected and recoverable.

No category theory required. "Non-empty list" and "same currency" are business sentences. Types just stop you from saying the wrong sentence in code.

## How to Apply

1. **Find critical heads.** Grep for `[0]`, `.find`, "primary", "default item", "first account." If empty is a bug, model non-empty.

2. **Pick encoding.** Primary + others → product `{ first, rest }`. Order-sensitive list that must not be empty → `NonEmptyArray<T>`. Schema/Zod can refine `.nonempty()` and brand the result.

3. **Construct at the edge.** Parse API payloads into non-empty. Do not scatter `as NonEmptyArray` in the core. Smart constructors return `Result` or Maybe when the list is empty.

4. **For matching fields, parameterize the product.** `Money<C>`, `Measure<Unit>`, then write binary ops that share the type parameter.

5. **Index intentionally.** Use `T["field"]` when deriving related types (form fields, patch types, currency of a money value) so renames propagate.

6. **Prefer type-level rules over throw.** If the only enforcement is runtime throw after a wide type, you still need tests and you still get production surprises. Move the rule left.

7. **Property-test constructors.** Empty arrays and currency mismatches should fail construction; valid shapes should always succeed. That is where tests earn their keep; the domain stops re-checking.

8. **Stay honest about TS limits.** You cannot express every dependent invariant. Combine brands, products, unions, non-empty, and indexed generics for the 80% that removes real bugs; leave the rest to Result + tests.

## Examples

**Situation:** Multi-account customer UI assumes `accounts[0]` is primary; empty array from a flaky API blanks the page.

**Application:** Domain type `CustomerAccounts = { primary: Account; others: Account[] }` or non-empty tuple. Boundary schema requires at least one account and maps first to primary (or uses an explicit primary flag from ACL). UI always receives a primary.

**Illustrative result:** Empty payload fails parse once at the edge with a clear error. Domain and UI delete null guards on head access.

---

**Situation:** Billing adds USD and EUR amounts; library throws "currency mismatch" in production under load.

**Application:** `Money<"USD">` vs `Money<"EUR">` (or branded currency types). `add` only accepts matching `C`. Conversion is an explicit function `convert(rate, money): Money<Target>` producing a new currency type, not a silent same-type add.

**Illustrative result:** Mixed-currency add does not compile. You no longer need a unit test whose only job is "throws when currencies differ" for the pure add path.

---

**Situation:** Feature flags arrive as `string[]`; code does `flags.find(f => f === "beta")` and treats missing as false inconsistently.

**Application:** If the domain needs a default flag set, parse to `NonEmptyArray<Flag>` or a product of required flags plus optional extras. If flags are a closed set, prefer a product of booleans or a union of known flag names, not an open array.

**Illustrative result:** Configuration errors surface at startup parse, not mid-request when a code path finally looks for the head.

---

**Situation:** Metrics pipeline mixes Celsius and Fahrenheit in one `number` field.

**Application:** `Temperature<"C" | "F">` product with unit parameter. Arithmetic only within the same unit; conversion functions change the parameter. Indexed access `Temperature<U>["unit"]` keeps helpers aligned.

**Illustrative result:** Chart code cannot sum mixed units without an explicit convert step the type system tracks.

## Anti-Patterns (tactical)

**Don't:** Leave critical "must have one" data as plain `Array` and re-validate in every feature.
**Why:** That is shotgun validation for collections. One empty case in a new module and you ship a production null deref. Non-empty at the boundary is Parse, Don't Validate for lists.

**Don't:** Encode invariants only as runtime throws on half-typed products.
**Why:** `function add(a: Money, b: Money)` that throws is a type signature that lies until the throw. Callers and LLMs believe any two Money values compose. Put the rule in `C`.

**Don't:** Use `as NonEmptyArray` to silence the compiler after a vibe check.
**Why:** Forgeable non-empty is worse than honest `Array` because it spreads false confidence. Construction must go through schema or smart constructor.

**Don't:** Parameterize everything with five type arguments "for maximum safety."
**Why:** Unreadable types do not ship. Parameterize the axes that have real business rules (currency, unit, non-empty). Leave the rest as ordinary fields.

**Don't:** Gate the technique on dependent-type theory or proving things in Agda.
**Why:** Enterprise TS teams need "primary account always exists" and "don't add USD to EUR." Tuple types and generics deliver that. Teaching Idris first is gatekeeping, not engineering.
