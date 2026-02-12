"""
06_unique_and_counts_with_masks.py

Focus:
- np.unique to understand values and counts
- useful with boolean masks (filter first, then analyze)
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


header("Setup: small data")
data = np.array([1, 2, 2, 3, 3, 3, 5, 5, 9, 9, 9, 9])
print("data:", data)


header("1) Unique values")
u = np.unique(data)
print("unique:", u)


header("2) Unique values with counts")
u, counts = np.unique(data, return_counts=True)
print("unique:", u)
print("counts:", counts)


header("3) Use a mask first, then unique")
mask = data >= 3
filtered = data[mask]
print("mask (data >= 3):", mask)
print("filtered:", filtered)

u2, c2 = np.unique(filtered, return_counts=True)
print("unique (filtered):", u2)
print("counts (filtered):", c2)


header("4) Simple frequency print")
for val, cnt in zip(u2, c2):
    print(f"value {val} appears {cnt} times")
