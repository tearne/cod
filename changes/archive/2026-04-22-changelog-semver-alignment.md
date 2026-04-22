# Changelog headings follow versioning scheme (with framework dogfooding)

## Intent

Two linked gaps:

1. **Project changelogs have no stated convention.** `ADDITIONAL/VERSIONING.md` prescribes semver for projects, but nothing says the project's changelog headings should match (e.g. `## 1.2.3` rather than a date).

2. **The COD framework doesn't dogfood its own semver guidance.** `agent/CHANGELOG.md` uses `## YYYY-MM-DD[.N]`. If we're telling users their projects should use semver, the framework should too.

State the rule for project changelogs and convert the framework to follow it.

## Approach

### Rule: project changelog headings match the versioning scheme

Add a short paragraph to `ADDITIONAL/VERSIONING.md` stating that if the project maintains a changelog, its headings should match the versioning scheme — `## 1.2.3` for semver. Cheap to state, makes the convention explicit.

### Convert `agent/CHANGELOG.md` to semver

Rewrite every existing `## YYYY-MM-DD[.N]` heading as semver. Dates are dropped — git history is authoritative for "when".

Starting point `0.1.0` — COD is pre-stable, matching the VERSIONING.md guidance ("start at 0.1.0 if the project is not yet stable").

**Proposed retrofit mapping:**

| New heading | Was | Entry summary |
|---|---|---|
| `## 0.1.0` | 2026-04-18 | Initial versioned release |
| `## 0.1.1` | 2026-04-19 | rename process.md; opt-in reads version from CHANGELOG; Completing adds Changelog entry step; opt-in stops seeding process-feedback.md |
| `## 0.1.2` | 2026-04-19.1 | opt-in.py moved to repo root |
| `## 0.1.3` | 2026-04-22 | Approach guidance tightened |
| `## 0.1.4` | 2026-04-22.1 | only-child rule relaxed to preference |
| `## 0.1.5` | 2026-04-22.2 | Approach bullet for map-duplication |
| `## 0.1.6` | 2026-04-22.3 | Changelog entry folded into Conclusion; Build-mode patch-bump rule |
| `## 0.1.7` | (this change) | Changelog headings switched to semver |

All retrofits treated as patch bumps — the framework is still pre-1.0 iteration; fine-grained minor/major distinction isn't yet meaningful.

### Update `opt-in.py`

- `VERSION_HEADING_PATTERN` regex switches to semver (`^##\s+(\d+\.\d+\.\d+)\s*$`).
- `changes/agent/<version>/` directory naming follows the semver string (e.g. `changes/agent/0.1.7/`).
- Existing dated install directories in users' projects are left in place; cleanup is manual, consistent with prior move policies.

### Update `PROCESS.md` Completing section

Current text says "add a new `## YYYY-MM-DD[.N]` section". Update to refer to the next semver version per `ADDITIONAL/VERSIONING.md`, and drop the dated-heading mechanics (the `.N` suffix rule, the "version name is the source of truth for the next `opt-in.py` install" note — that last fact stays true but the heading-is-directory-name phrasing adjusts).

### Changelog

At Conclusion, the changelog entry is the first in the new semver format — `## 0.1.7` — noting the format migration.

## Plan

- [x] Add a paragraph to `agent/ADDITIONAL/VERSIONING.md` stating that if the project maintains a changelog, its headings should follow the versioning scheme (e.g. `## 1.2.3` for semver).
- [x] Rewrite `agent/CHANGELOG.md`: convert all existing `## YYYY-MM-DD[.N]` headings to semver (`0.1.0` through `0.1.6`) per the retrofit mapping. Drop the dates. Update the lead paragraph if its phrasing depended on the dated format.
- [x] Update `opt-in.py` `VERSION_HEADING_PATTERN` regex to match semver (`^##\s+(\d+\.\d+\.\d+)\s*$`).
- [x] Update `opt-in.py` directory-naming logic so installs land under `changes/agent/<semver>/` (e.g. `changes/agent/0.1.7/`). *(No code change needed — the existing logic already uses the captured version string as the directory name; the regex change alone suffices.)*
- [x] Update `agent/PROCESS.md` `### Completing` section: drop `YYYY-MM-DD[.N]` / `.N` mechanics and dated-heading phrasing; refer to `ADDITIONAL/VERSIONING.md` for the next version's number.
- [x] At Conclusion: add a `## 0.1.7` entry to `agent/CHANGELOG.md` describing the format migration.

## Conclusion

Plan executed cleanly. One task turned out to be a no-op: `opt-in.py` directory-naming already used the captured version string verbatim, so the regex update alone was sufficient — no separate code change needed.

