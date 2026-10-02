# Re-derive the counts in data/gap-benchmark-counts-*.json from the public dataset.
# pip install datasets ; python3 scripts/gap_counts.py
from datasets import load_dataset
ds = load_dataset("acartag7/gap-benchmark", split="train")
gap = [r for r in ds if r["gap"]]
print("gap rows", len(gap))                                                          # 1002
print("runtime guard attached", sum(1 for r in gap if r["mode"] in "EO"))             # 879
print("enforce mode", sum(1 for r in gap if r["mode"] == "E"))                        # 490
print("enforce, denied", sum(1 for r in gap if r["mode"] == "E" and r["denied_events"] > 0))   # 180
print("enforce, let through", sum(1 for r in gap if r["mode"] == "E" and r["denied_events"] == 0))  # 310
print("observe mode", sum(1 for r in gap if r["mode"] == "O"))                        # 389
print("unguarded", sum(1 for r in gap if r["mode"] == "U"))                           # 123
print("refusal graded strong", sum(1 for r in gap if r["refusal_strength"] == "strong"))  # 997
