# Coding Style

## 1. Orchestration functions read like prose
- Top-level functions read like pseudocode — flow is visible without reading any function body
- Name functions after *what* they accomplish, not *how*
- No implementation detail in orchestration functions
- No vague names: `process`, `handle`, `do_thing`
- No comments explaining *what* — the function name does that

## 2. One abstraction level per function
- Each function either coordinates steps or implements one — never both
- Extract operations when naming them adds clarity, even if small or single-use
- No raw computation mixed with function calls in the same body

## 3. Modules organised by domain concept
- Name modules after domain concepts: `ingestion`, `validation`, `reporting`, `auth`
- Group functions that change for the same reasons
- No catch-all modules: `utils`, `helpers`, `misc`, `common`
- No organisation by code type alone: `functions.py`, `classes.py`

## 4. Names communicate intent
- Names answer "what does this do?" or "what does this represent?"
- Use domain language — the vocabulary stakeholders use
- No abbreviations that save typing but cost reading: `usr`, `cfg`, `proc`
- No technical names (`manager`, `processor`, `handler`) where a domain name exists

## 5. Comments explain *why*, not *what*
- Comment on business rules, gotchas, trade-offs, and non-obvious decisions
- No comments that restate what the code shows
- No outdated comments — they actively mislead

## 6. Markdown
- Do not insert manual line breaks in prose — write paragraphs as single unbroken lines so text reflows correctly with soft wrap
