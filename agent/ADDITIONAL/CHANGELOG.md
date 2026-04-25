# Changelog

A changelog records notable changes to the project, newest at the top. It complements git history by surfacing what's worth knowing at a glance.

If the project already has an established changelog format, use that. Otherwise, choose one of the formats below.

## Dated format — `## YYYY-MM-DD[.N]`

Fits projects without formal versioned releases: continuous, append-only development where the date is a sufficient identifier.

- Each entry is an `H2` heading with a date: `## YYYY-MM-DD`.
- A `.N` suffix is added when a date already has an entry: `## 2026-04-24.1`, `.2`, etc.
- Entries are added to the top of the file.

Example:

```
## 2026-04-24

- `PROCESS.md`: Feedback and Conclusion become post-approval summaries.
```

## Semver format — `## X.Y.Z`

Fits projects that cut semantic-versioned releases (see `VERSIONING.md`). Each heading corresponds to a released version.

- Each entry is an `H2` heading with a version: `## 1.2.0`.
- Entries are added to the top of the file.
- For the major/minor/patch decision, follow `VERSIONING.md`.

Example:

```
## 1.2.0

- Added `--dry-run` mode to the build script.
```

## Writing an entry

- Trivial changes — typo fixes, minor doc wording — may not warrant a new section. Substantive changes do.
- One line per change; start with the affected file or a verb.
- Keep it brief: the reader is scanning. Detailed rationale belongs in the change document and the commit message.
- If downstream migration steps are needed, include them as a short paragraph below the bullets for that entry.
