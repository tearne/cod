# Align test-build versions with the shipped version

## Intent

`PROCESS.md`'s build-mode rule says to bump versioning by the smallest increment whenever a build is handed to the user for review or test. During cardplayer's `m4a-support` this produced a divergence: the user flashed and tested `0.6.1`, but Conclusion proposed `0.7.0` for the shipped version. What was numerically tested is not what gets recorded in the changelog. The rule should be unambiguous on whether test-handover versions are disposable markers or should pre-figure the shipped version.

## Approach

### Plan records the kind of bump, not the exact version

Plan says "minor bump" or "patch bump" (or the date-based equivalent), not `0.7.0`. Plans can sit idle while other versions ship; resolving the kind against the current latest at Build start keeps the bump correct.

### Test handover uses the resolved shipped version

The first test handover lands at that resolved version — `0.7.0` is flashed during test and ships as `0.7.0`. Refinements during test bump patch (`0.7.0` → `0.7.1` → `0.7.2`); the final tested version is what ships, with a single changelog entry covering the final accumulated state. The Conclusion confirms or revises the bump kind if scope shifted mid-build.

## Plan

- [x] Replace `PROCESS.md`'s Build-mode versioning paragraph with the new rule: Plan records the kind of bump, Build resolves it against current latest, refinements bump patch, final tested version is what ships, Conclusion confirms or revises the bump kind if scope shifted.
- [x] Add to `PROCESS.md`'s Plan stage that for projects with versioning, the Plan includes a task to bump version by the planned kind.

## Conclusion

Completed.

### Proposed changelog entry

```
## 2026-04-28

- `PROCESS.md`: replaced the "smallest increment" versioning rule. Plan now records the kind of bump (major/minor/patch or date-based equivalent) and Build resolves it against the current latest at start — keeps the bump correct when plans sit idle. Refinements during test bump patch; the final tested version is what ships, in a single changelog entry. Conclusion confirms or revises the bump kind if scope shifted.
```
