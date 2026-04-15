# Coding Style: Rust Addendum
*Applies to Rust projects only — ignore in other contexts.*

Rust-specific extensions to `STYLE.md`. The core principles apply; this addendum covers Rust's type system, ownership model, and idioms.

## 1. Module visibility as an API boundary *(extends STYLE §3)*
- Default to the most restrictive visibility — start private, widen only when needed
- Use `pub(crate)` for internal infrastructure, not public API
- Treat a module's `pub` surface as its contract; keep it minimal and stable
- No `pub` on everything to silence compiler warnings — that signals a missing abstraction boundary
- No `mod.rs` as a pass-through that re-exports everything from every submodule

## 2. Error types reflect domain, not implementation
- For libraries: define a custom error enum (e.g. `pub enum MyLibError { ... }`) with explicit variants in a dedicated `error.rs`; implement `std::error::Error` directly rather than using a derive macro
- For applications: use `color_eyre` for error aggregation and reporting
- Propagate with `?` freely — idiomatic and not an abstraction violation
- No `Box<dyn Error>` — erases information callers may need
- No single monolithic error enum spanning multiple unrelated modules
- No `unwrap()` or `expect()` in paths reachable at runtime; reserve for invariants that cannot fail by construction
- Prefer `expect("invariant description")` over `unwrap()` — name the invariant, not the symptom

## 3. Ownership signals design
- Prefer owned types in structs that clearly own their data
- Use borrows (`&`, `&mut`) at function boundaries where the callee doesn't need ownership
- `Arc<Mutex<T>>` only when shared mutable ownership is genuinely required
- Widespread `clone()` calls are a code smell — investigate before accepting
- No `Arc<Mutex<T>>` to resolve borrow conflicts without first understanding why they exist
- No cloning to avoid lifetime annotations — lifetimes communicate real constraints

## 4. Traits define behaviour, not convenience
- Define a trait when there are (or will be) multiple concrete implementations
- Default to generics (`impl Trait` / `fn foo<T: Trait>`) — zero-cost and keeps variant sets explicit
- `dyn Trait` only when the variant set is open — plugin systems, user-supplied callbacks, external inputs
- No trait for a concept with one implementation and no foreseeable variation
- No traits as a substitute for a module boundary
- "Chosen at runtime" is not sufficient justification for `dyn Trait` — a config-selected variant is still a closed set

## 5. Test support modules
- Group test-only exports in a single `#[cfg(test)] pub(crate) mod test_support { ... }` block per file
- Place alongside `mod tests` at the bottom of the file
- No individual `#[cfg(test)]` gates on items that need to be visible outside the file
- No test helpers mixed into the public API

## 6. Serde config conventions
- Apply `#[serde(deny_unknown_fields)]` to all config structs — makes unrecognised keys an error rather than a silent no-op
- Use internally-tagged enums (`#[serde(tag = "...")]`) for config variants with associated parameters
- Name the tag field after the domain concept (e.g. `"model"`, `"strategy"`)
- No untagged or adjacently-tagged enums for config without specific reason

## 7. Runtime-to-static dispatch
Where a component is selected at runtime but the variant set is closed, bridge with a single startup `match`:

```rust
match config.model {
    Model::Seir => run::<SeirModel>(config),
    Model::Sir  => run::<SirModel>(config),
}
```

- Perform the dispatch `match` once at startup, outside the hot path
- No `Box<dyn Trait>` simply because selection happens at runtime
- No repeated dispatch matches — a single match at the boundary is the point
