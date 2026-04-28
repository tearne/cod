# Split Keywords section into its own file

## Intent

The `## Keywords` section of `PROCESS.md` (covering `process:` and `aside:`) describes session-level mechanisms that are orthogonal to the plan/build lifecycle. Keeping them in `PROCESS.md` makes that file broader than its name suggests and adds length to the document agents read most.

## Approach

### Move Keywords to `agent/KEYWORDS.md`

Extract the `## Keywords` section into a new sibling framework document, loaded via `@KEYWORDS.md` pointer in `agent/README.md` alongside `@PROCESS.md`, `@STYLE.md`, `@MAP-GUIDANCE.md`. Mirrors how the framework is already split.

### One-line pointer left in `PROCESS.md`

A short note at the bottom of `PROCESS.md` points to `KEYWORDS.md` so agents reading the lifecycle document don't lose track of the keyword mechanisms.

## Plan

- [x] Create `agent/KEYWORDS.md` containing the Keywords section content (verbatim) under a top-level `# Keywords` heading.
- [x] Strip the `## Keywords` section from `PROCESS.md`, leaving a one-line pointer at the bottom.
  - Pointer placed under its own `## Session keywords` heading so it doesn't read as nested under Gates and permissions.
- [x] Add `@KEYWORDS.md` to the `@` pointer list at the end of `agent/README.md`.
- [x] Bump version (date-based: next entry, resolved at Build start). → `2026-04-28.2`

## Conclusion

Completed.

### Proposed changelog entry

```
## 2026-04-28.2

- Keywords section moved out of `PROCESS.md` into a new `agent/KEYWORDS.md`. `PROCESS.md` keeps a short pointer under its own `Session keywords` heading; `agent/README.md` adds `@KEYWORDS.md` to the framework `@` pointer list. `PROCESS.md` now focuses purely on the change lifecycle.
```
