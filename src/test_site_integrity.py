"""Static Code, Link, and Integrity Audit for the Research Dashboard.
Verifies file:// compatibility (no ES modules, no CSV fetches), anchor stability,
DOM element bindings, CSS brace balance, and unrendered LaTeX markers.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

html_path = ROOT / "index.html"
if not html_path.exists():
    print("[FAIL] index.html not found.")
    sys.exit(1)

html = html_path.read_text(encoding="utf-8")

# Collect JS content from root and web/js/
js_texts = []
for p in [ROOT / "app.js", ROOT / "web" / "flow.js", ROOT / "web" / "site_data.js"]:
    if p.exists():
        js_texts.append(p.read_text(encoding="utf-8"))

for p in (ROOT / "web" / "js").glob("*.js"):
    js_texts.append(p.read_text(encoding="utf-8"))

combined_js = "\n".join(js_texts)

# Collect CSS content
css_texts = []
for p in [ROOT / "styles.css", ROOT / "web" / "design_tokens.css"]:
    if p.exists():
        css_texts.append((p.name, p.read_text(encoding="utf-8")))

for p in (ROOT / "web" / "css").glob("*.css"):
    css_texts.append((p.name, p.read_text(encoding="utf-8")))

print("=== Static Code & Link Integrity Audit ===")
failures = 0

# 1. Check all anchor targets in HTML
hrefs = set(re.findall(r'href="#([a-zA-Z0-9_-]+)"', html))
ids = set(re.findall(r'id="([a-zA-Z0-9_-]+)"', html))
missing_ids = hrefs - ids
print(f"Anchors checked: {len(hrefs)}")
if missing_ids:
    print(f"  [FAIL] Missing anchor targets in HTML: {missing_ids}")
    failures += 1
else:
    print("  [PASS] All href='#id' anchors resolve to valid DOM elements.")

# 2. Check DOM element IDs referenced in JS getElementById
js_ids = set(re.findall(r'getElementById\(["\']([a-zA-Z0-9_-]+)["\']\)', combined_js))
missing_js_ids = js_ids - ids
print(f"JS getElementById references: {len(js_ids)}")
if missing_js_ids:
    print(f"  [FAIL] Missing element IDs referenced in JS: {missing_js_ids}")
    failures += 1
else:
    print("  [PASS] All JS getElementById references exist in HTML.")

# 3. Check for unrendered LaTeX markers ($...$)
latex_matches = re.findall(r'\$[^\$\n]{2,30}\$', html)
if latex_matches:
    print(f"  [FAIL] Unrendered LaTeX markers in HTML: {latex_matches}")
    failures += 1
else:
    print("  [PASS] Zero unrendered LaTeX markers found in HTML.")

# 4. Check CSS syntax basic balance
brace_fail = False
for name, ctext in css_texts:
    if ctext.count('{') != ctext.count('}'):
        print(f"  [FAIL] CSS brace mismatch in {name}: {{={ctext.count('{')}, }}={ctext.count('}')}")
        brace_fail = True
        failures += 1
if not brace_fail:
    print(f"  [PASS] All CSS files have balanced braces ({len(css_texts)} files checked).")

# 5. Check file:// Protocol Compatibility
# Rule: No <script type="module">
module_scripts = re.findall(r'<script[^>]+type=["\']module["\']', html, re.IGNORECASE)
if module_scripts:
    print("  [FAIL] ES module <script type='module'> detected! Forbidden under file:// protocol.")
    failures += 1
else:
    print("  [PASS] No ES modules detected (compatible with file:// protocol).")

# Rule: No fetch() of CSV files in JS
csv_fetches = re.findall(r'fetch\(["\'][^"\']+\.csv["\']', combined_js, re.IGNORECASE)
if csv_fetches:
    print(f"  [FAIL] fetch() of local CSV detected in JS: {csv_fetches}. Must use window.SITE_DATA.")
    failures += 1
else:
    print("  [PASS] Zero fetch() of local CSV files in JS.")

# 6. Check Local Linked Assets (CSS/JS files linked in HTML exist on disk)
asset_links = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:css|js))["\']', html)
missing_assets = []
for asset in asset_links:
    if asset.startswith("http://") or asset.startswith("https://") or asset.startswith("//"):
        continue
    asset_path = ROOT / asset
    if not asset_path.exists():
        missing_assets.append(asset)

if missing_assets:
    print(f"  [FAIL] Local assets missing on disk: {missing_assets}")
    failures += 1
else:
    print("  [PASS] All local script and link assets verified present on disk.")

if failures > 0:
    print(f"\n[FAIL] {failures} integrity issues detected!")
    sys.exit(1)

print("\n[PASS] All static integrity checks passed with 0 errors.")
sys.exit(0)
