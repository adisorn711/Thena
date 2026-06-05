---
name: Column mutation verification — table scripts
description: Always spot-check first output of any script that modifies structured table columns
type: feedback
---

Always spot-check script output before declaring success when manipulating markdown table columns.

**Why:** `add_stability_column.py` used `rstrip(" |")` before appending stability value, which destroyed the trailing cell boundary — stability ended up inside the last column instead of as a new column. Bug was not caught until the next diagnostic step.

**How to apply:**
- After running any script that modifies table structure, print 3 sample rows to stdout and visually verify column count before moving on.
- Never use `rstrip()` on pipe-delimited lines before appending — it removes cell boundaries. Use regex group capture instead: `re.match(r"^(.*\|)\s*$", line)` to get the clean end, then append `" newvalue |"`.
- If `grep -c` returns a count near total line count, the regex is almost certainly matching everything (e.g., `\|` in basic grep is alternation, not literal pipe). Switch to Python or `grep -P`.
