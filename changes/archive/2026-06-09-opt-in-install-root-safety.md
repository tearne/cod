# Opt-in install-root safety

**Mode:** Formal

## Intent

When `opt-in.py` runs, it installs the framework at the git **toplevel**, which can be an ancestor of the directory the user actually invoked it from. In a brand-new project folder that hasn't been `git init`'d, the toplevel resolves to some enclosing repo, so `CLAUDE.md`, `changes/`, and `.gitignore` silently land there instead of in the intended project. From inside the project the user sees no install and no `.gitignore`, and a later `git add` can sweep `changes/agent` into staging.

A fresh, unconfigured directory should not silently adopt an ancestor repo as its install target. When the resolved git toplevel is not the directory opt-in was invoked from, the user should be told before anything is written, so framework files never install at an unexpected root.

## Approach

### Detect the mismatch before writing

Compare the invocation directory (`Path.cwd()`) against the resolved git toplevel, immediately after `git_root()` and before any file is copied. Equal — proceed as today. Different — the user is likely not at their intended project root.

### Warn and confirm, don't hard-stop

On a mismatch, print both paths and ask the user to confirm before continuing; default to no. A hard-stop would wrongly block the legitimate case of installing from a subdirectory of one's own repo, whereas confirmation prevents the silent mis-install while letting deliberate installs through.

When there is no tty (CI, piped input), the prompt can't be answered, so opt-in aborts with the same guidance rather than assuming consent. No bypass flag — COD's usage doesn't need unattended installs.

### Guide the likely fix

The warning names the common remedy — `git init` in the current directory to make it the install root — alongside the option to proceed into the shown toplevel.

## Plan

- [x] Add an install-root guard, called in `main()` after `git_root()` and before `copy_framework_files`, that gates proceeding when invocation dir and git toplevel differ
- [x] When `Path.cwd()` differs from the git toplevel, print both paths and prompt to confirm (default no); abort on no
- [x] When stdin is not a tty, skip the prompt and abort with the same guidance
- [x] Manually verify: run from a git subdirectory and decline, confirm, and a piped/no-tty invocation

## Conclusion

`git_root()` resolves to the toplevel, so running from an un-init'd folder inside an enclosing repo silently installs there. Fixed with `confirm_install_root()`, which prompts before writing when the invocation directory differs from the toplevel and aborts when there's no tty. Shipped as `opt-in.py` `1.2.2`.

No framework `CHANGELOG.md` entry: `opt-in.py` is the installer, not a shipped framework file, so its changes don't affect consumer installs or the dated version.

## Log

- Verifying the interactive decline/confirm branches needed a pseudo-tty harness, since the build shell's stdin is not a tty (the no-tty branch otherwise short-circuits the prompt). All four branches confirmed: equal-root proceeds; mismatch + n aborts with no writes; mismatch + y installs at root; mismatch + no-tty aborts with guidance.
- Dropped the `git init`-here remedy from both messages (user preferred not to suggest nesting a repo inside a repo); the confirmation prompt carries the safety. Patch bumped 1.2.1 → 1.2.2.
