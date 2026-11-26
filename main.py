import os

ENTRY = "My phone charged to 100% by 9am, yet still slides me a low-power popup by noon - apparently the percentage was more of a mood."

outdir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

n = len(ENTRY)
print(f"LEN={n}")
if n < 1 or n > 200 or not ENTRY.strip():
    raise SystemExit(1)
