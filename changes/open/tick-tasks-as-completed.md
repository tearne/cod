# Tick plan tasks as completed, not all at the end

## Intent

Agents aren't following `PROCESS.md`'s Executing rule that each plan task is ticked as it completes — they tick everything at the end of the build. That defeats the purpose: partial builds can't be cleanly resumed without re-reading the change to figure out what's done, and progress isn't visible mid-build.
