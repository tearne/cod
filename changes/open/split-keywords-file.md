# Split Keywords section into its own file

## Intent

The `## Keywords` section of `PROCESS.md` (covering `process:` and `aside:`) describes session-level mechanisms that are orthogonal to the plan/build lifecycle. Keeping them in `PROCESS.md` makes that file broader than its name suggests and adds length to the document agents read most.

Move the Keywords section to its own file (e.g. `agent/KEYWORDS.md`), loaded from `README.md` alongside the other framework documents. `PROCESS.md` would then focus purely on the change lifecycle.

The main tradeoff: keywords become slightly less discoverable if they're not in the document agents open first. Mitigate by keeping a one-line pointer in `PROCESS.md` and ensuring `README.md`'s opening references the new file.
