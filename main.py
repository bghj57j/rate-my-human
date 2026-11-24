# Writes the one review to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# The concrete detail: the 3 a.m. leaderboard refresh.
import os
LINE = "Four stars: my human is lovely, but he refreshes the leaderboard at 3 a.m. and asks why the prize hasn't arrived yet."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run
