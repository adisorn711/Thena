"""
fix_stability_column.py
แก้ไข stability column ที่ merge ผิดจาก add_stability_column.py
- header: "Enrichment Tag Stability |" → "Enrichment Tag | Stability |"
- separator: extra dashes merged → split properly
- data row: "value S |" → "value | S |"
"""
import re

TARGET = "/Users/adisornj/Desktop/Thena/lab/customer_tag_library_v2_expansion.md"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
result = []
in_tag_table = False

for line in lines:
    stripped = line.rstrip()

    # ── Fix broken header ────────────────────────────────────────────────────
    # "| ... | Enrichment Tag Stability |"  →  "| ... | Enrichment Tag | Stability |"
    if re.match(r"\|\s*Tag\s*\|", stripped) and "Enrichment Tag Stability" in stripped:
        in_tag_table = True
        line = stripped.replace("Enrichment Tag Stability", "Enrichment Tag | Stability")

    # ── Fix broken separator ─────────────────────────────────────────────────
    # After header, separator has extra dashes merged into last cell
    elif in_tag_table and re.match(r"\|[-| ]+\|$", stripped) and "`" not in stripped:
        # Split on | to get cells
        cells = stripped.split("|")
        # cells[0]='' cells[1..n-1]=dash patterns cells[-1]=''
        inner = cells[1:-1]
        # Count expected cells: 7 columns → 7 inner cells
        if len(inner) < 7:
            # Last inner cell has extra dashes merged, trim back and add new cell
            last = inner[-1]
            # Remove the extra "---" that got merged (3 chars)
            if len(last.strip()) > 16:
                inner[-1] = last[:-(len(last.strip()) - 16) - 0]  # trim to original length
            inner.append("---")
            line = "|" + "|".join(inner) + "|"
        elif len(inner) == 7:
            line = stripped  # already correct

    # ── Fix broken data rows ─────────────────────────────────────────────────
    # "| `tag` | ... | EnrichmentTag S |"  →  "| `tag` | ... | EnrichmentTag | S |"
    elif in_tag_table and re.match(r"\|\s*`", stripped):
        # Pattern: ends with " [SVMM?] |" where the stability code is merged
        m = re.match(r"^(.*\S)\s+([SVM?])\s*\|$", stripped)
        if m:
            line = m.group(1) + " | " + m.group(2) + " |"

    elif in_tag_table and not stripped.startswith("|"):
        in_tag_table = False

    result.append(line)

fixed = "\n".join(result)

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(fixed)

# ── Verify ───────────────────────────────────────────────────────────────────
with open(TARGET, "r", encoding="utf-8") as f:
    verify = f.read()

tag_lines = [l for l in verify.split("\n") if re.match(r"\|\s*`", l)]
has_stability = sum(1 for l in tag_lines if re.search(r"\|\s*[SVM]\s*\|$", l))
has_unknown   = sum(1 for l in tag_lines if re.search(r"\|\s*\?\s*\|$", l))
no_column     = sum(1 for l in tag_lines if not re.search(r"\|\s*[SVM?]\s*\|$", l))

print(f"✅  Fix applied")
print(f"   Total tag rows   : {len(tag_lines)}")
print(f"   Has S/V/M column : {has_stability}")
print(f"   Unknown (?)      : {has_unknown}")
print(f"   Missing column   : {no_column}")

if has_unknown:
    print("\n   Tags with '?' (need manual assignment):")
    for l in verify.split("\n"):
        if re.match(r"\|\s*`", l) and re.search(r"\|\s*\?\s*\|$", l):
            tag = re.match(r"\|\s*`([^`]+)`", l)
            if tag:
                print(f"     - {tag.group(1)}")
