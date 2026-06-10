# Subdirectory opt-in

**Mode:** TBD

## Intent

Today `opt-in.py` always installs the framework at the git repository root. We want the option to opt in from within a subdirectory of the project — the current working directory — so that several agents can work independently in separate subdirs of the same repo, each subdir self-contained.

Each opted-in subdir needs to stand on its own: its own `changes/` tree, its own `CLAUDE.md` pointer, and its own `.gitignore` so the generated artefacts are ignored locally without colliding with sibling installs or the repo root.

When the script is run from a subdirectory rather than the repo root, it should confirm with the user that they want to set up for the subdirectory before proceeding — installing in a subdir is the deliberate, less-common case and shouldn't happen silently.

## Approach

### Install root replaces git root as the install target

`main()` gains an `install_root` that everything currently anchored to `project_root` uses instead — the version dir, `CLAUDE.md`, `.claude/settings.local.json`, `changes/open`/`archive`, `.gitignore`, the self-install guard, and the legacy-layout checks. Each subdir install then produces its own self-contained tree and its own `.gitignore` for free, because the existing helpers already write paths relative to whatever root they're handed.

### Subdir detection drives the confirmation

The repo must still be a git repo, so `git_root()` stays as the precondition check. The install target is the current working directory: when cwd resolves to the git root, behaviour is unchanged and there's no prompt; when cwd sits below the root, the script reports both paths and asks the user to confirm a subdir install (default no — explicit `y` required). Declining aborts with a hint to re-run from the repo root, rather than silently falling back to a root install.

### Git operations stay repo-resolved

The uncommitted-changes guard keeps working for a subdir `CLAUDE.md`: git is invoked with `cwd=install_root` and a pathspec relative to install_root, so git locates the enclosing repo itself rather than needing the install root to be the repo root.

### Script version bump

`opt-in.py`'s own `VERSION` constant bumps minor (1.2.0 → 1.3.0) as a new feature. This is the script's `--version`, independent of the dated CHANGELOG heading that names the install directory.

### Docs

README's "Dev repo vs consumer projects" section gains a note that installs can target a subdir, and the CHANGELOG gets a new dated heading (which cuts the installable release).

## Plan

- [x] Add subdir confirmation: derive the install target from cwd, prompt when it sits below the git root, abort on decline
- [x] Anchor all install operations and guards to the chosen install root in place of git root
- [x] Bump `opt-in.py` `VERSION` to 1.3.0
- [x] Note subdir installs in README's "Dev repo vs consumer projects" section
- [x] Add a CHANGELOG entry under a new dated heading

## Conclusion

Completed as planned. The "git operations stay repo-resolved" decision needed no code beyond the rename — git resolves the enclosing repo from `cwd=install_root` on its own, so the uncommitted-changes guard works for a subdir `CLAUDE.md` unchanged.

Verified end-to-end via real `uv` runs: root install (unprompted, regression-clean), subdir install (self-contained tree + own `.gitignore`, repo root untouched), all three prompt branches, and the uncommitted-changes guard exercised from a subdir.

Out of scope but done alongside at the user's request: added `__pycache__/` to this repo's own root `.gitignore`.

Changelog entry added during build under `## 2026-06-10`.
