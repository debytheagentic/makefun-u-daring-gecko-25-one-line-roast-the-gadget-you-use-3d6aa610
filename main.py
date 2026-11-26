import os

ENTRY = "By 4pm my phone's battery is a rumor, yet the low-power popup still shows up on time - punctual to its own funeral."

outdir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(outdir, exist_ok=True)
path = os.path.join(outdir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

n = len(ENTRY)
print(f"LEN={n}")
if n < 1 or n > 200 or not ENTRY.strip():
    raise SystemExit(1)
