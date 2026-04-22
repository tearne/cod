# Trim explanatory prose from PROCESS.md

## Intent

`PROCESS.md` has accumulated explanatory prose alongside the rules — motivation paragraphs, justifications, "why we do it this way" framings. Agents mostly need the rules to act; the reasoning is useful when judging edge cases but not when following the mainline flow.

Audit `PROCESS.md` for prose that explains *why* rather than *what to do*, and either cut it or replace it with a pointer to `PRINCIPLES.md` (which is where the reasoning already lives, or can live). The aim is a leaner PROCESS.md that reads as rules + short examples, with the principles-level reasoning reachable by link rather than inlined.
