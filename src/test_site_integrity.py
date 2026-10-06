import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

html = (ROOT / "index.html").read_text(encoding="utf-8")
app_js = (ROOT / "app.js").read_text(encoding="utf-8")
flow_js = (ROOT / "web" / "flow.js").read_text(encoding="utf-8")
site_data_js = (ROOT / "web" / "site_data.js").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
tokens_css = (ROOT / "web" / "design_tokens.css").read_text(encoding="utf-8")

print("=== Static Code & Link Integrity Audit ===")

# 1. Check all anchor targets in HTML
hrefs = set(re.findall(r'href="#([a-zA-Z0-9_-]+)"', html))
ids = set(re.findall(r'id="([a-zA-Z0-9_-]+)"', html))
missing_ids = hrefs - ids
print(f"Anchors checked: {len(hrefs)}")
print(f"Missing anchor targets in HTML: {missing_ids}")

# 2. Check DOM element IDs referenced in JS
js_ids = set(re.findall(r'getElementById\(["\']([a-zA-Z0-9_-]+)["\']\)', app_js + flow_js))
missing_js_ids = js_ids - ids
print(f"JS getElementById references: {len(js_ids)}")
print(f"Missing element IDs in HTML: {missing_js_ids}")

# 3. Check for unrendered LaTeX markers
latex_matches = re.findall(r'\$[^\$\n]{2,30}\$', html)
print(f"Unrendered LaTeX markers in HTML: {latex_matches}")

# 4. Check CSS syntax basic balance
print(f"CSS braces balance (styles.css): {css.count('{') == css.count('}')}")
print(f"CSS braces balance (design_tokens.css): {tokens_css.count('{') == tokens_css.count('}')}")

if missing_ids or missing_js_ids or latex_matches:
    print("\n[FAIL] Integrity issues detected!")
    sys.exit(1)

print("\n[PASS] All static integrity checks passed with 0 errors.")
