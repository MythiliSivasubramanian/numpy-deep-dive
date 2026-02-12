"""
04_shape_mismatch_debugging.py

Focus:
- Common shape mismatch errors during assignment
- How to read the target slice shape
- How to fix errors by matching shapes
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


header("Setup")
x = np.arange(12).reshape(3, 4)
print("x:\n", x)
print("shape:", x.shape)


header("1) Target slice shape")
target = x[:, 1:3]
print("target = x[:, 1:3]\n", target)
print("target shape:", target.shape, "  (3 rows, 2 cols)")


header("2) Wrong assignment (shape mismatch)")
try:
    x[:, 1:3] = [10, 20, 30]  # length 3 does NOT fit 2 columns
except ValueError as e:
    print("Error:", e)
    print("Fix: give 2 values (for 2 columns), or use a (3,2) array.")


header("3) Correct assignment with 2 values (broadcasts to all rows)")
x = np.arange(12).reshape(3, 4)
x[:, 1:3] = [10, 20]
print("x after x[:, 1:3] = [10, 20]:\n", x)


header("4) Correct assignment with a full (3,2) array")
x = np.arange(12).reshape(3, 4)
x[:, 1:3] = np.array([[1, 2],
                      [3, 4],
                      [5, 6]])
print("x after assigning a (3,2) array:\n", x)


header("5) Column assignment must match number of rows")
x = np.arange(12).reshape(3, 4)
try:
    x[:, 0] = [9, 8]  # needs 3 values (3 rows)
except ValueError as e:
    print("Error:", e)
    print("Fix: give 3 values (one per row).")

x[:, 0] = [9, 8, 7]
print("Fixed column assignment:\n", x)
