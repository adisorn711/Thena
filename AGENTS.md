# AGENTS.md — Thena

Coding agent instructions for this repository.
For strategy, content, and thinking-partner work → see `CLAUDE.md`.

---

## Project Context

**Thena** is a data science project for a credit card issuer.
Core focus: Customer Tagging pipeline — turning raw transaction data into behavioral tags per customer, used for campaign targeting and personalization.

**Domain terms:**
- **Tag** — a behavioral label per customer (e.g. `frequent_diner`, `car_owner`) with a confidence score 0–1
- **Path A** — tags buildable from transaction data alone (254 tags, no enrichment needed)
- **Path B** — tags requiring Merchant Enrichment data (69 tags)
- **Score formula** — `0.4×frequency + 0.4×recency + 0.2×breadth`, threshold ≥ 0.3

---

## Repository Structure

```
lab/                          # All working files
  customer_tag_pipeline_spec.md   # Full pipeline spec — read this first
  customer_tag_library_v2_expansion.md  # 323 tag definitions (v2.1)
  path_a_rule_table.md              # Rule table for Path A tags
  customer_tag_library.md           # Tag definitions v1
  customer_tag_library_by_enrichment.md  # Path A vs B split
  dtag_framework.py                 # D-Tag aggregation logic
  build_pptx.py                     # PPT builder (base deck)
  build_memo_pptx.py                # PPT builder (memo deck)
  append_tags_pptx.py               # PPT appendix builder (tag slides)
ψ/                            # Vault — DO NOT TOUCH
CLAUDE.md                     # Claude Code config — DO NOT TOUCH
AGENTS.md                     # This file
```

---

## Coding Guidelines

- **Python 3.10+**
- Scripts in `lab/` — keep them standalone, no shared imports between scripts
- No unnecessary abstractions — if used once, write it inline
- Match existing style in the file you're editing
- No docstrings or type annotations unless already present in the file

---

## What Codex Should Work On

- Python scripts in `lab/` — new pipeline scripts, scoring logic, data processing
- Extending `dtag_framework.py` — aggregation rules, tag computation
- PPT generation scripts — `build_pptx.py`, `build_memo_pptx.py`, `append_tags_pptx.py`
- SQL query drafts for tag pipeline (save as `.sql` in `lab/`)

---

## What Codex Should NOT Touch

| Path | Reason |
|------|--------|
| `ψ/` | Vault directory — shared Oracle memory, never modify |
| `CLAUDE.md` | Claude Code config only |
| `*.pptx` | Binary files — modify only via Python scripts |
| `*.md` (non-lab) | Strategy/content docs — handled by Claude Code |

---

## Key Reference: Pipeline Spec

Before writing any tag-related code, read `lab/customer_tag_pipeline_spec.md`.
It contains: input/output schema, scoring formula, Path A/B logic, refresh schedule, and implementation notes for each tag type.
