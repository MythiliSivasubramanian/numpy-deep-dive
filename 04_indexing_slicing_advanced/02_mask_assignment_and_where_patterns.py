"""
02_mask_assignment_and_where_patterns.py

Focus:
- Boolean masks for conditional updates
- Multiple condition filtering
- np.where patterns
- Data cleaning style operations

This file builds practical intuition for mask-based indexing.
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1) Setup array
# ------------------------------------------------------------
header("1) Setup array")

x = np.arange(12).reshape(3, 4)
print("x:\n", x)


# ------------------------------------------------------------
# 2) Replace values greater than threshold
# ------------------------------------------------------------
header("2) Replace values > 5 with 100")

y = x.copy()
y[y > 5] = 100

print("Modified array:\n", y)


# ------------------------------------------------------------
# 3) Replace values in a range
# ------------------------------------------------------------
header("3) Replace values between 3 and 8 with -1")

z = x.copy()
mask = (z >= 3) & (z <= 8)
z[mask] = -1

print("Mask:\n", mask)
print("Modified array:\n", z)


# ------------------------------------------------------------
# 4) Even / odd filtering
# ------------------------------------------------------------
header("4) Even / Odd filtering")

even = x[x % 2 == 0]
odd = x[x % 2 == 1]

print("Even values:", even)
print("Odd values :", odd)


# ------------------------------------------------------------
# 5) np.where for labeling
# ------------------------------------------------------------
header("5) np.where labeling example")

labels = np.where(x > 5, "High", "Low")
print("Labels:\n", labels)


# ------------------------------------------------------------
# 6) np.where for numeric transformation
# ------------------------------------------------------------
header("6) np.where numeric transformation")

scaled = np.where(x > 5, x * 10, x)
print("Scaled array:\n", scaled)


# ------------------------------------------------------------
# 7) Find indices of condition
# ------------------------------------------------------------
header("7) Indices where x > 8")

idx = np.where(x > 8)
print("Indices:", idx)

for r, c in zip(idx[0], idx[1]):
    print(f"x[{r},{c}] = {x[r, c]}")


# ------------------------------------------------------------
# 8) Clip values using masks
# ------------------------------------------------------------
header("8) Clipping values (limit range)")

clip = x.copy()

clip[clip < 3] = 3
clip[clip > 8] = 8

print("Clipped array:\n", clip)


# ------------------------------------------------------------
# 9) Practical example: score grading
# ------------------------------------------------------------
header("9) Score grading example")

scores = np.array([35, 50, 65, 80, 95])

grades = np.where(scores >= 75, "A",
          np.where(scores >= 60, "B",
          np.where(scores >= 50, "C", "F")))

print("Scores:", scores)
print("Grades:", grades)
