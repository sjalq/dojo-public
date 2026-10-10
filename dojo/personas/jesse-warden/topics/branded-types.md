---
triggers:
  - "user mixes up string IDs or other primitives that mean different domain things"
  - "user asks about branded types, wrapper types, or nominal typing in TypeScript"
  - "user describes primitive obsession or naming mismatch with Product/BA language"
  - "user parses headers/JSON as plain strings and passes wrong IDs through"
  - "user asks how Zod brand or opaque brands keep IDs distinct"
use_when:
  - "two values share a runtime representation (string, number) but must never be interchangeable"
  - "DDD ubiquitous language should appear in the type system, not only in comments"
  - "you want the compiler to reject wrong-ID call sites without unhappy-path unit tests for mixups"
fails_when:
  - "brands are forgeable with `as Email` / `as UserID` in production code paths"
  - "everything is branded without need (noise, no real mixup risk)"
  - "brands exist only in types while runtime parse still yields plain strings with no brand step"
related:
  - "parse-dont-validate.md"
  - "impossible-states.md"
  - "type-driven-development.md"
  - "result-and-errors-as-values.md"
---

# Branded Types

## When to Use

- **Primitive obsession:** IDs, emails, currency codes, account numbers, tokens are all `string` (or `number`) and the compiler happily swaps them
- **Naming Things:** Product, BA, and users say "Customer Account" but the code says `User` and bad assumptions follow (e.g. Users purchasing when only CustomerAccounts should)
- Boundary parse of headers, query params, JSON fields that are "just strings" until they enter domain functions
- You want to delete a class of tests: "what if we pass the wrong ID type?" becomes a compile error
- Gradual systems (TypeScript, Python typing) where the structural type system will not distinguish two string aliases on its own

## Fails When

- The brand is **forgeable** (`"🐮" as Email`) and anyone can mint "validated" values without a constructor or schema
- You brand every primitive for ceremony with no real confusion risk (team drowns in brand noise)
- Brands are declared but never applied at the parse boundary; interior code still takes `string`
- You need **opacity** (cannot construct outside the module) and only used a public structural brand; graduate to opaque types with unexported symbol + `makeX`
- The real bug is invalid *shape* or *format*, not mixup of two valid different concepts; pair brands with schemas and smart constructors

## Core Concept

Jesse opens the TyDD series with two basic type problems: **Naming Things** and **Primitive Obsession**.

### Naming Things (DDD)

From Domain Driven Design: the words you use for things should be the same in conversation and in code. If User, Product Owner, and Business Analyst all call it a **Customer Account**, the code should too.

Wrong word → wrong meaning → wrong logic. Example: calling everything `User`, then allowing "Users" to purchase when only **CustomerAccounts** should. Clear communication is huge; types make the shared language enforceable.

### Primitive Obsession

Developers default to primitives to "differentiate" concepts:

```ts
const customerID: string = request.headers['x-user-id']
const userID: string = request.headers['x-customer-id']
```

Even the headers are already mixed up in the example. Worse: the compiler cannot tell primitives apart. This looks fine:

```ts
purchase(customerID) // Purchase = (customerID: string) => ...
```

…when you meant the other ID. **Even good type systems** (Python, TypeScript, and even Elm and Scala) allow this if both are typed as `string`.

### Nominal via brands

**Branded types** (also called wrapper types) make the type system act **nominally**: it knows `CustomerID` and `UserID` are **different**, even if both are strings underneath.

```ts
type UserID = string & { brand: 'UserID' }
type CustomerID = string & { brand: 'CustomerID' }

type Purchase = (customerID: CustomerID) => ...
```

Now the compiler rejects mixing them. You do not need unhappy-path tests for "wrong ID type passed."

### Zod (and friends) at the boundary

When parsing unknown sources (headers, JSON), schema libraries support branding:

```ts
const Headers = z.object({
  'x-user-id': z.string().brand<'UserID'>(),
  'x-customer-id': z.string().brand<'CustomerID'>(),
})
```

Instead of plain `z.string()` for both. Parse once; interior code receives branded types it can trust (pair with [parse-dont-validate.md](parse-dont-validate.md)).

### Relation to opacity

Simple intersection brands in TypeScript are often still forgeable with assertions. For types that must only exist after validation (Email, Money, Access Token), Jesse's later Opaque Types recipe:

- Unexported `unique symbol` brand  
- Exported type  
- Exported `makeEmail(value: string): Email | undefined` or `Result<Email, E>`  

Opaque types abstract parse-don't-validate for single values and block accidental invalid construction. Brands are the family; opacity is the harder edge of the same idea.

### Multi-language strategies (talk / series stance)

- **TypeScript:** intersection brand, Zod `.brand`, or unique symbol + module boundary  
- **Python / gradual systems:** NewType-style wrappers, branded validators; same primitive-obsession story  
- **Elm / Scala:** still allow mixups if you type both as `String`; use custom types / opaque modules, not bare aliases to string  
- **General:** nominal distinction is the goal; encoding depends on whether the language is structural or nominal by default  

The compiler's job: help you distinguish two things, and make "thing" the same word Users, Design, and Business use.

### Place in the Big 3

Branded types answer **what things are separate**. Next:

- **Product types:** what belongs together (AND)  
- **Unions / DUs:** what is allowed (OR)  

Together they are Jesse's **Big 3** toolkit for making impossible states impossible ([impossible-states.md](impossible-states.md)).

## How to Apply

1. **Audit primitives that mean different domain concepts.** IDs, emails, SKUs, currency codes, user vs customer vs account identifiers.

2. **Align names with ubiquitous language.** Prefer `CustomerAccountId` over generic `UserId` if the business language is Customer Account.

3. **Introduce brands at the type level:**

```ts
type UserID = string & { readonly brand: unique symbol } // or string brand tag
// practical TS teaching form from the series:
type UserID = string & { brand: 'UserID' }
type CustomerID = string & { brand: 'CustomerID' }
```

4. **Update function signatures** to take branded types, not `string`.

5. **Brand at parse time** (Zod/ArkType/Effect schema): never pass raw header strings into domain functions.

6. **Delete obsolete tests** that only existed to catch ID mixups; keep tests for real domain behavior.

7. **When forgeability matters,** hide the brand symbol, export only the type + constructor, return `Result` or `undefined` on failure; property-test the constructor.

8. **Compose with products:** brands live *inside* product types (`{ customerId: CustomerID; ... }`) so cohesion and distinction travel together.

## Examples

**Situation:** `purchase` takes `string`; headers map user id and customer id; a swap compiles and bills the wrong party.

**Application:** Define `UserID` and `CustomerID` brands; type `Purchase = (customerID: CustomerID) => ...`; parse headers with Zod `.brand<'UserID'>()` and `.brand<'CustomerID'>()`.

**Illustrative result:** Swapped IDs fail at compile time (or at schema parse if raw strings never enter domain). No unit test for "wrong ID type."

---

**Situation:** Codebase says `User` everywhere; Product says only Customer Accounts place orders.

**Application:** Rename and retype: `CustomerAccount` product with branded `CustomerAccountId`. Purchase functions accept that type only. ACL/parse maps external "user" payloads into customer-account language at the edge.

**Illustrative result:** Communication and code share one language; illegal purchase subjects don't typecheck.

---

**Situation:** `Email` is `string`; people construct `"not-an-email" as Email`.

**Application:** Opaque pattern: unexported brand symbol, `makeEmail` returns `Email | undefined` or `Result`, blast maker with property tests. Domain functions take `Email`, never `string`.

**Illustrative result:** Invalid emails cannot be forged without going through the maker; parse-don't-validate for a single value.

---

**Situation:** Money amounts as `number` with currency as separate free string; USD and EUR add at runtime and explode.

**Application:** Brand currency or use `Money<C>` with indexed/generic currency equality (series Part 5). Pair branded currency with product type so add only typechecks for same `C`.

**Illustrative result:** Business rule lives in the type system, not only a runtime throw after half-typing.

## Anti-Patterns (tactical)

**Don't:** Type distinct domain IDs as bare `string` and rely on parameter names for safety.  
**Why:** Names are documentation; the compiler ignores them. Structural sameness wins.

**Don't:** Use different words in code than Product/BA/Users use.  
**Why:** Meaning drifts; features get built on the wrong concept (User purchases vs CustomerAccount purchases).

**Don't:** Brand only in a type alias comment (`/** UserId */ type UserId = string`) without a nominal brand.  
**Why:** Still the same type as every other string alias in structural systems.

**Don't:** Parse with `z.string()` and cast to branded types with `as`.  
**Why:** You skipped the validation/branding step; Shotgun Parsing and forgeability return.

**Don't:** Export a forgeable brand and call the system "type safe."  
**Why:** `"x" as CustomerID` reopens primitive obsession through the back door. Prefer opaque makers for critical types.

**Don't:** Brand everything on day one across a million-line repo.  
**Why:** TyDD is gradual. Start where mixups hurt (money, auth, purchases); expand with small batches.
