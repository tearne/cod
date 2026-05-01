# Comprehension Oriented Design (COD)

A methodology for user/agent collaborative software development where the user maintains a navigable conceptual map of the system and agents render it into code. The act of maintaining the map is the structural thinking that keeps comprehension alive as systems grow.

See [PRINCIPLES.md](PRINCIPLES.md) for the full description and principles.

## Contents

- `agent/` — process files, style guides, and map guidance
- `CHANGELOG.md` — release history; its topmost heading is the next install version
- `opt-in.py` — installer script for adopting the framework in another project

## Dev repo vs consumer projects

Working in this repo is unlike consuming the framework via `opt-in.py`. Here, `agent/` is the source of truth and `CLAUDE.md` loads it directly via `@agent/README.md`. In a consumer project, `opt-in.py` copies the framework files into `changes/agent/<version>/`, and the consumer's `CLAUDE.md` points at that copy.

When reasoning about what consumers see, `opt-in.py` is authoritative — `FRAMEWORK_FILES` is the list of files that actually reach consumers. A file `@`-imported by `agent/README.md` but missing from `FRAMEWORK_FILES` will silently fail to load in any consumer project, while loading fine here.

## Changelog

This project's changelog lives at [`CHANGELOG.md`](CHANGELOG.md) and uses the dated `.N` format described in [`agent/ADDITIONAL/CHANGELOG.md`](agent/ADDITIONAL/CHANGELOG.md). `opt-in.py` reads the topmost `## YYYY-MM-DD[.N]` heading and uses it as the install directory name (`changes/agent/<version>/` in the downstream project). Adding a new heading at the top therefore cuts a new installable release.
