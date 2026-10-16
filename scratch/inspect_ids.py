import re
from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")
ids = re.findall(r'id="([^"]+)"', html)
print(f"Total IDs: {len(ids)}")
for i in ids:
    print(f"  - {i}")
