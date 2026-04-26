# Align test-build versions with the shipped version

## Intent

`PROCESS.md`'s build-mode rule says to bump versioning by the smallest increment whenever a build is handed to the user for review or test. During cardplayer's `m4a-support` change this produced a divergence: the user flashed and tested `0.6.1`, but Conclusion proposed `0.7.0` for the shipped version (semver-appropriate for a feature). What was numerically tested is not what gets recorded in the changelog.

Resolve which way the rule should point. Either test-handover versions are deliberately disposable "are you running my latest binary" markers, orthogonal to the shipped semver — in which case the convention should make their disposable nature visible (e.g. `0.7.0-rc1`, `0.7.0-dev`). Or test handovers should pre-figure the shipped version (so a feature change's test build lands at `0.7.0` from the first handover, and patch-level dev iteration uses suffixes if more than one round is needed). `PROCESS.md` should be unambiguous on which.
