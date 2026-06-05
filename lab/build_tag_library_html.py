"""
build_tag_library_html.py
สร้าง Tag Library HTML แบบ interactive
- Color row ตาม source (Existing / Overlap / New)
- Badge Stability (S / V / M)
- Filter bar: source, stability, path, search
"""
import re

SRC  = "/Users/adisornj/Desktop/Thena/lab/customer_tag_library_v2_expansion.md"
OUT  = "/Users/adisornj/Desktop/Thena/lab/CustomerTagging_TagLibrary.html"

# ── Parse markdown ─────────────────────────────────────────────────────────────
categories = []   # [{name, emoji, tags:[...]}]
cur_cat = None

with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")

        # Category header:  ### 🍽️ Food & Dining
        m = re.match(r"###\s+(.+)", line)
        if m:
            raw = m.group(1).strip()
            # strip markdown link syntax if any
            em = re.match(r"^([\U00010000-\U0010ffff\u2600-\u27BF\u2B50\uD83C-\uDBFF\uDC00-\uDFFF][\uFE0F]?)", raw)
            emoji = em.group(1) if em else ""
            name  = raw[len(emoji):].strip().lstrip("️").strip()
            cur_cat = {"name": name, "emoji": emoji, "tags": []}
            categories.append(cur_cat)
            continue

        # Data row: | `tag` | def | signal | A | Source | Enrichment | S |
        if cur_cat is None:
            continue
        m = re.match(
            r"\|\s*`([^`]+)`\s*\|"   # tag
            r"\s*([^|]+)\|"           # definition
            r"\s*([^|]+)\|"           # signal
            r"\s*([AB])\s*\|"         # path
            r"\s*(Existing|Overlap|New)\s*\|"  # source
            r"\s*([^|]*)\|"           # enrichment tag
            r"\s*([SVM?])\s*\|",      # stability
            line
        )
        if m:
            cur_cat["tags"].append({
                "tag":        m.group(1).strip(),
                "definition": m.group(2).strip(),
                "signal":     m.group(3).strip(),
                "path":       m.group(4).strip(),
                "source":     m.group(5).strip(),
                "enrichment": m.group(6).strip(),
                "stability":  m.group(7).strip(),
            })

total_tags = sum(len(c["tags"]) for c in categories)
print(f"Parsed: {len(categories)} categories, {total_tags} tags")

# ── HTML helpers ───────────────────────────────────────────────────────────────
def source_badge(s):
    cfg = {
        "Existing": ("badge-ex",  "Existing"),
        "Overlap":  ("badge-ov",  "Overlap"),
        "New":      ("badge-new", "New"),
    }
    cls, label = cfg.get(s, ("badge-ex", s))
    return f'<span class="badge {cls}">{label}</span>'

def stab_badge(s):
    cfg = {
        "S": ("stab-s", "S · Stable"),
        "V": ("stab-v", "V · Variable"),
        "M": ("stab-m", "M · Momentum"),
    }
    cls, label = cfg.get(s, ("stab-s", s))
    return f'<span class="stab {cls}">{label}</span>'

def path_badge(p):
    cls = "path-a" if p == "A" else "path-b"
    return f'<span class="path {cls}">Path {p}</span>'

def row_class(s):
    return {"Existing": "row-ex", "Overlap": "row-ov", "New": "row-new"}.get(s, "row-ex")

# ── Build HTML sections ────────────────────────────────────────────────────────
cat_sections = []
for cat in categories:
    if not cat["tags"]:
        continue
    s_cnt = sum(1 for t in cat["tags"] if t["source"] == "Existing")
    o_cnt = sum(1 for t in cat["tags"] if t["source"] == "Overlap")
    n_cnt = sum(1 for t in cat["tags"] if t["source"] == "New")

    rows = ""
    for t in cat["tags"]:
        rows += (
            f'<tr class="{row_class(t["source"])}" '
            f'data-source="{t["source"].lower()}" '
            f'data-path="{t["path"].lower()}" '
            f'data-stab="{t["stability"].lower()}" '
            f'data-tag="{t["tag"]}" '
            f'data-def="{t["definition"]}">'
            f'<td class="tag-cell"><code>{t["tag"]}</code></td>'
            f'<td>{t["definition"]}</td>'
            f'<td class="sig-cell">{t["signal"]}</td>'
            f'<td>{path_badge(t["path"])}</td>'
            f'<td>{source_badge(t["source"])}</td>'
            f'<td>{stab_badge(t["stability"])}</td>'
            f'</tr>\n'
        )

    cnt_pills = (
        f'<span class="cnt-pill cnt-ex">{s_cnt} Existing</span>'
        f'<span class="cnt-pill cnt-ov">{o_cnt} Overlap</span>'
        f'<span class="cnt-pill cnt-new">{n_cnt} New</span>'
    )
    cat_sections.append(f"""
<section class="cat-section" data-cat="{cat['name'].lower()}">
  <div class="cat-header">
    <span class="cat-emoji">{cat['emoji']}</span>
    <span class="cat-name">{cat['name']}</span>
    <span class="cat-total">{len(cat['tags'])} tags</span>
    <div class="cat-pills">{cnt_pills}</div>
  </div>
  <table class="tag-table">
    <thead>
      <tr>
        <th style="width:18%">Tag</th>
        <th>Definition</th>
        <th style="width:18%">Signal</th>
        <th style="width:7%">Path</th>
        <th style="width:9%">Source</th>
        <th style="width:12%">Stability</th>
      </tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
</section>""")

# ── Stats for header ───────────────────────────────────────────────────────────
all_tags = [t for c in categories for t in c["tags"]]
ex_n  = sum(1 for t in all_tags if t["source"] == "Existing")
ov_n  = sum(1 for t in all_tags if t["source"] == "Overlap")
nw_n  = sum(1 for t in all_tags if t["source"] == "New")
s_n   = sum(1 for t in all_tags if t["stability"] == "S")
v_n   = sum(1 for t in all_tags if t["stability"] == "V")
m_n   = sum(1 for t in all_tags if t["stability"] == "M")
pa_n  = sum(1 for t in all_tags if t["path"] == "A")
pb_n  = sum(1 for t in all_tags if t["path"] == "B")

# ── Full HTML ──────────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Customer Tag Library v2.2</title>
<style>
  :root {{
    --bg:      #0D1B2A;
    --bg2:     #1A2E44;
    --bg3:     #0A1520;
    --accent:  #00C2FF;
    --white:   #FFFFFF;
    --light:   #B0C4DE;
    --green:   #00E596;
    --yellow:  #FFD700;
    --orange:  #FF8C42;
    --red:     #FF6B6B;
    --ex-bg:   #0D1B2A;
    --ov-bg:   #001C2A;
    --new-bg:  #071A10;
    --ex-hl:   #152535;
    --ov-hl:   #002535;
    --new-hl:  #0A2518;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg);
    color: var(--light);
    font-size: 13px;
    line-height: 1.5;
  }}

  /* ── Top Bar ── */
  .topbar {{
    background: #060F18;
    padding: 20px 32px;
    border-bottom: 1px solid #1A3A52;
    position: sticky; top: 0; z-index: 100;
  }}
  .topbar-inner {{
    max-width: 1400px; margin: 0 auto;
    display: flex; align-items: center; gap: 20px; flex-wrap: wrap;
  }}
  .title {{ color: var(--white); font-size: 18px; font-weight: 700; flex: 0 0 auto; }}
  .title span {{ color: var(--accent); }}
  .search-box {{
    flex: 1 1 220px; min-width: 160px;
    background: #1A2E44; border: 1px solid #2A4A64;
    color: var(--white); padding: 6px 12px; border-radius: 6px;
    font-size: 13px; outline: none;
  }}
  .search-box::placeholder {{ color: #5A7A9A; }}
  .filter-group {{ display: flex; gap: 6px; flex-wrap: wrap; }}
  .filter-btn {{
    padding: 5px 12px; border-radius: 20px; border: 1px solid #2A4A64;
    background: transparent; color: var(--light); cursor: pointer;
    font-size: 12px; transition: all 0.15s;
  }}
  .filter-btn:hover, .filter-btn.active {{ border-color: var(--accent); color: var(--accent); }}
  .filter-btn.f-ex.active   {{ border-color: #5A8AB0; color: #5A8AB0; }}
  .filter-btn.f-ov.active   {{ border-color: var(--accent); color: var(--accent); }}
  .filter-btn.f-new.active  {{ border-color: var(--green); color: var(--green); }}
  .filter-btn.f-s.active    {{ border-color: var(--accent); color: var(--accent); }}
  .filter-btn.f-v.active    {{ border-color: var(--yellow); color: var(--yellow); }}
  .filter-btn.f-m.active    {{ border-color: var(--orange); color: var(--orange); }}
  .filter-btn.f-pa.active   {{ border-color: #8A7AFF; color: #8A7AFF; }}
  .filter-btn.f-pb.active   {{ border-color: #FF8C42; color: #FF8C42; }}
  .result-count {{ color: #5A7A9A; font-size: 12px; margin-left: auto; white-space: nowrap; }}

  /* ── Stats Bar ── */
  .statsbar {{
    background: #0A1520;
    border-bottom: 1px solid #1A3A52;
    padding: 10px 32px;
  }}
  .statsbar-inner {{
    max-width: 1400px; margin: 0 auto;
    display: flex; gap: 24px; flex-wrap: wrap; align-items: center;
  }}
  .stat-group {{ display: flex; gap: 12px; align-items: center; }}
  .stat-label {{ color: #5A7A9A; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; }}
  .stat-item {{ font-size: 12px; }}

  /* ── Main ── */
  .main {{ max-width: 1400px; margin: 0 auto; padding: 24px 32px; }}

  /* ── Category Section ── */
  .cat-section {{ margin-bottom: 32px; }}
  .cat-header {{
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
    padding: 10px 16px;
    background: #0A1520;
    border-left: 3px solid var(--accent);
    border-radius: 0 6px 6px 0;
    margin-bottom: 1px;
  }}
  .cat-emoji {{ font-size: 18px; }}
  .cat-name  {{ color: var(--white); font-weight: 700; font-size: 15px; }}
  .cat-total {{ color: var(--accent); font-size: 13px; font-weight: 600;
                background: #001A2A; padding: 2px 8px; border-radius: 10px; }}
  .cat-pills {{ display: flex; gap: 6px; margin-left: auto; }}
  .cnt-pill  {{ padding: 2px 8px; border-radius: 10px; font-size: 11px; }}
  .cnt-ex    {{ background: #1A2E44; color: #7A9AB0; }}
  .cnt-ov    {{ background: #001829; color: var(--accent); }}
  .cnt-new   {{ background: #071A10; color: var(--green); }}

  /* ── Tag Table ── */
  .tag-table {{
    width: 100%; border-collapse: collapse;
    font-size: 12.5px;
  }}
  .tag-table thead tr {{
    background: #060F18;
  }}
  .tag-table th {{
    padding: 7px 10px; text-align: left;
    color: #5A7A9A; font-size: 11px;
    text-transform: uppercase; letter-spacing: 0.04em;
    font-weight: 600; border-bottom: 1px solid #1A3A52;
  }}
  .tag-table td {{ padding: 7px 10px; border-bottom: 1px solid #111F2E; vertical-align: top; }}

  /* Row colors by source */
  .row-ex  {{ background: var(--ex-bg); }}
  .row-ov  {{ background: var(--ov-bg); }}
  .row-new {{ background: var(--new-bg); }}
  .row-ex:hover  {{ background: var(--ex-hl); }}
  .row-ov:hover  {{ background: var(--ov-hl); }}
  .row-new:hover {{ background: var(--new-hl); }}

  /* Hidden row */
  .tag-table tr.hidden {{ display: none; }}

  /* Tag name */
  .tag-cell code {{
    background: #0A1520; color: var(--accent);
    padding: 2px 6px; border-radius: 4px;
    font-size: 11.5px; font-family: 'SF Mono', 'Fira Code', monospace;
  }}
  .row-ov .tag-cell code  {{ color: var(--accent); }}
  .row-new .tag-cell code {{ color: var(--green); }}
  .row-ex .tag-cell code  {{ color: #7AB0CC; }}

  /* Signal cell */
  .sig-cell {{ color: #6A8A9A; font-size: 11.5px; }}

  /* Badges */
  .badge {{
    display: inline-block; padding: 2px 7px; border-radius: 4px;
    font-size: 11px; font-weight: 600;
  }}
  .badge-ex  {{ background: #1A2E44; color: #7A9AB0; }}
  .badge-ov  {{ background: #001829; color: var(--accent); border: 1px solid #003A52; }}
  .badge-new {{ background: #071A10; color: var(--green); border: 1px solid #0A3020; }}

  .stab {{
    display: inline-block; padding: 2px 7px; border-radius: 4px;
    font-size: 11px; font-weight: 700;
  }}
  .stab-s {{ background: #001829; color: var(--accent); }}
  .stab-v {{ background: #1A1400; color: var(--yellow); }}
  .stab-m {{ background: #1A0D00; color: var(--orange); }}

  .path {{
    display: inline-block; padding: 2px 6px; border-radius: 4px;
    font-size: 11px; font-weight: 600;
  }}
  .path-a {{ background: #1A1A3A; color: #8A7AFF; }}
  .path-b {{ background: #1A0D00; color: var(--orange); }}

  /* ── Legend ── */
  .legend {{
    background: #060F18; border: 1px solid #1A3A52;
    border-radius: 8px; padding: 16px 20px; margin-bottom: 24px;
    display: flex; gap: 32px; flex-wrap: wrap;
  }}
  .legend-group {{ display: flex; flex-direction: column; gap: 6px; }}
  .legend-title {{ color: #5A7A9A; font-size: 11px; text-transform: uppercase;
                   letter-spacing: 0.05em; margin-bottom: 4px; }}
  .legend-item {{ display: flex; align-items: center; gap: 8px; font-size: 12px; }}
  .legend-desc {{ color: #6A8A9A; font-size: 11px; }}
</style>
</head>
<body>

<!-- ── Top Bar ── -->
<div class="topbar">
  <div class="topbar-inner">
    <div class="title">Customer Tag Library <span>v2.2</span></div>
    <input class="search-box" id="searchBox" placeholder="Search tag or definition..." oninput="applyFilters()">
    <div class="filter-group">
      <span style="color:#5A7A9A;font-size:11px;align-self:center">SOURCE</span>
      <button class="filter-btn f-ex"  onclick="toggleFilter('source','existing')">Existing</button>
      <button class="filter-btn f-ov"  onclick="toggleFilter('source','overlap')">Overlap</button>
      <button class="filter-btn f-new" onclick="toggleFilter('source','new')">New</button>
    </div>
    <div class="filter-group">
      <span style="color:#5A7A9A;font-size:11px;align-self:center">STABILITY</span>
      <button class="filter-btn f-s" onclick="toggleFilter('stab','s')">S · Stable</button>
      <button class="filter-btn f-v" onclick="toggleFilter('stab','v')">V · Variable</button>
      <button class="filter-btn f-m" onclick="toggleFilter('stab','m')">M · Momentum</button>
    </div>
    <div class="filter-group">
      <span style="color:#5A7A9A;font-size:11px;align-self:center">PATH</span>
      <button class="filter-btn f-pa" onclick="toggleFilter('path','a')">Path A</button>
      <button class="filter-btn f-pb" onclick="toggleFilter('path','b')">Path B</button>
    </div>
    <div class="result-count" id="resultCount">{total_tags} tags</div>
  </div>
</div>

<!-- ── Stats Bar ── -->
<div class="statsbar">
  <div class="statsbar-inner">
    <div class="stat-group">
      <span class="stat-label">Source</span>
      <span class="stat-item" style="color:#7A9AB0">{ex_n} Existing</span>
      <span class="stat-item" style="color:var(--accent)">{ov_n} Overlap</span>
      <span class="stat-item" style="color:var(--green)">{nw_n} New</span>
    </div>
    <div style="width:1px;height:20px;background:#1A3A52"></div>
    <div class="stat-group">
      <span class="stat-label">Stability</span>
      <span class="stat-item" style="color:var(--accent)">{s_n} Stable</span>
      <span class="stat-item" style="color:var(--yellow)">{v_n} Variable</span>
      <span class="stat-item" style="color:var(--orange)">{m_n} Momentum</span>
    </div>
    <div style="width:1px;height:20px;background:#1A3A52"></div>
    <div class="stat-group">
      <span class="stat-label">Path</span>
      <span class="stat-item" style="color:#8A7AFF">{pa_n} Path A (no enrichment needed)</span>
      <span class="stat-item" style="color:var(--orange)">{pb_n} Path B (enrichment required)</span>
    </div>
    <div style="width:1px;height:20px;background:#1A3A52"></div>
    <div class="stat-group">
      <span class="stat-label">Total</span>
      <span class="stat-item" style="color:var(--white);font-weight:700">{total_tags} tags  ·  {len(categories)} categories</span>
    </div>
  </div>
</div>

<!-- ── Main ── -->
<div class="main">

  <!-- Legend -->
  <div class="legend">
    <div class="legend-group">
      <div class="legend-title">Source</div>
      <div class="legend-item">
        <span class="badge badge-ex">Existing</span>
        <span class="legend-desc">มีอยู่แล้ว — ไม่มี enrichment tag ตรงๆ</span>
      </div>
      <div class="legend-item">
        <span class="badge badge-ov">Overlap</span>
        <span class="legend-desc">มีอยู่แล้ว + ตรงกับ enrichment tag ของทีม</span>
      </div>
      <div class="legend-item">
        <span class="badge badge-new">New</span>
        <span class="legend-desc">เพิ่มใหม่จาก enrichment review</span>
      </div>
    </div>
    <div class="legend-group">
      <div class="legend-title">Stability</div>
      <div class="legend-item">
        <span class="stab stab-s">S · Stable</span>
        <span class="legend-desc">พฤติกรรมหลัก — tag churn &lt; 20%/เดือน</span>
      </div>
      <div class="legend-item">
        <span class="stab stab-v">V · Variable</span>
        <span class="legend-desc">event-based / seasonal — churn สูงเป็นเรื่องปกติ</span>
      </div>
      <div class="legend-item">
        <span class="stab stab-m">M · Momentum</span>
        <span class="legend-desc">transitional — เปลี่ยนได้ แต่ค่อยๆ</span>
      </div>
    </div>
    <div class="legend-group">
      <div class="legend-title">Path</div>
      <div class="legend-item">
        <span class="path path-a">Path A</span>
        <span class="legend-desc">ทำได้เลย — ไม่ต้องรอ Merchant Enrichment</span>
      </div>
      <div class="legend-item">
        <span class="path path-b">Path B</span>
        <span class="legend-desc">ต้องรอ Enrichment (direct mapping)</span>
      </div>
    </div>
    <div class="legend-group" style="margin-left:auto;text-align:right">
      <div class="legend-title">ทีม Data Science  |  เมษายน 2025</div>
      <div style="color:var(--white);font-size:14px;font-weight:700;margin-top:4px">
        {total_tags} tags  ·  {len(categories)} categories
      </div>
      <div style="color:#5A7A9A;font-size:11px;margin-top:2px">
        Click column headers to sort  ·  Use filters above to narrow
      </div>
    </div>
  </div>

  <!-- Category Sections -->
  {''.join(cat_sections)}
</div>

<!-- ── JS Filter Logic ── -->
<script>
const activeFilters = {{ source: new Set(), stab: new Set(), path: new Set() }};

function toggleFilter(dim, val) {{
  const key = dim + '_' + val;
  const set = activeFilters[dim];
  if (set.has(val)) {{
    set.delete(val);
    document.querySelector(`.filter-btn[onclick="toggleFilter('${{dim}}','${{val}}')"]`).classList.remove('active');
  }} else {{
    set.add(val);
    document.querySelector(`.filter-btn[onclick="toggleFilter('${{dim}}','${{val}}')"]`).classList.add('active');
  }}
  applyFilters();
}}

function applyFilters() {{
  const q = document.getElementById('searchBox').value.toLowerCase();
  let visible = 0;
  document.querySelectorAll('.tag-table tbody tr').forEach(row => {{
    const srcMatch  = activeFilters.source.size === 0 || activeFilters.source.has(row.dataset.source);
    const stabMatch = activeFilters.stab.size   === 0 || activeFilters.stab.has(row.dataset.stab);
    const pathMatch = activeFilters.path.size   === 0 || activeFilters.path.has(row.dataset.path);
    const textMatch = q === '' ||
      row.dataset.tag.includes(q) ||
      row.dataset.def.toLowerCase().includes(q);
    if (srcMatch && stabMatch && pathMatch && textMatch) {{
      row.classList.remove('hidden'); visible++;
    }} else {{
      row.classList.add('hidden');
    }}
  }});
  // Hide empty category sections
  document.querySelectorAll('.cat-section').forEach(sec => {{
    const anyVisible = sec.querySelectorAll('tbody tr:not(.hidden)').length > 0;
    sec.style.display = anyVisible ? '' : 'none';
  }});
  document.getElementById('resultCount').textContent = visible + ' tags';
}}
</script>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

s_cnt = sum(1 for t in all_tags if t["source"] == "Existing")
o_cnt = sum(1 for t in all_tags if t["source"] == "Overlap")
n_cnt = sum(1 for t in all_tags if t["source"] == "New")
print(f"✅  CustomerTagging_TagLibrary.html")
print(f"   {total_tags} tags  ·  {len(categories)} categories")
print(f"   Source  — Existing: {s_cnt}  Overlap: {o_cnt}  New: {n_cnt}")
print(f"   Stab    — S: {s_n}  V: {v_n}  M: {m_n}")
print(f"   Path    — A: {pa_n}  B: {pb_n}")
print(f"   → Open: lab/CustomerTagging_TagLibrary.html")
