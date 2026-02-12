"""
03_broadcasting_with_indexing.py

Focus:
- Assigning values using indexing + slicing
- Broadcasting rules in assignment
- Common patterns used in data cleaning and ML preprocessing

Key idea:
When assigning to a slice, NumPy tries to "broadcast" the right-hand side
to match the shape of the left-hand side.
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



# 1) Setup
header("1) Setup array")

x = np.arange(12).reshape(3, 4)
print("x:\n", x)
print("shape:", x.shape)


# ------------------------------------------------------------
# 2) Assign a scalar to a slice (broadcasts automatically)
# ------------------------------------------------------------
header("2) Assign scalar to a slice (broadcasting)")

a = x.copy()
a[:, 1] = 0  # set entire column 1 to zero
print("Set column 1 to 0:\n", a)

b = x.copy()
b[1, :] = -1  # set entire row 1 to -1
print("\nSet row 1 to -1:\n", b)


# ------------------------------------------------------------
# 3) Assign a 1D array to a row (shapes must match)
# ------------------------------------------------------------
header("3) Assign 1D array to a row")

c = x.copy()
c[2, :] = [100, 200, 300, 400]  # length 4 matches columns
print("Row 2 replaced with [100,200,300,400]:\n", c)


# ------------------------------------------------------------
# 4) Assign a 1D array to a column (shapes must match)
# ------------------------------------------------------------
header("4) Assign 1D array to a column")

d = x.copy()
d[:, 0] = [9, 8, 7]  # length 3 matches rows
print("Column 0 replaced with [9,8,7]:\n", d)


# ------------------------------------------------------------
# 5) Assign to a submatrix with broadcasting
# ------------------------------------------------------------
header("5) Assign to a submatrix")

e = x.copy()
e[:, 1:3] = 5  # scalar broadcasts to shape (3,2)
print("Set columns 1:3 to 5:\n", e)

f = x.copy()
f[:, 1:3] = [10, 20]  # broadcasts across rows (matches 2 columns)
print("\nSet columns 1:3 to [10,20] (broadcast by rows):\n", f)


# ------------------------------------------------------------
# 6) Mask + broadcasting
# ------------------------------------------------------------
header("6) Mask + broadcasting")

g = x.copy()
g[g > 5] = -99  # replace all values > 5
print("Replace values > 5 with -99:\n", g)

h = x.copy()
h[x % 2 == 0] = h[x % 2 == 0] * 10  # multiply evens by 10
print("\nMultiply even values by 10:\n", h)


# ------------------------------------------------------------
# 7) Common mistake: shape mismatch
# ------------------------------------------------------------
header("7) Common mistake: shape mismatch (example)")

i = x.copy()
try:
    i[:, 1:3] = [1, 2, 3]  # ERROR: slice has 2 columns, but values have length 3
except ValueError as err:
    print("Error:", err)
    print("Reason: slice shape is (3,2) but you gave 3 values (length 3).")


# ------------------------------------------------------------
# 8) Quick summary
# ------------------------------------------------------------
header("8) Summary")

print("- Assigning a scalar to a slice works (broadcasting).")
print("- Assigning a 1D array must match the target shape along that axis.")
print("- Assigning to x[:, 1:3] expects 2 columns -> length 2 array works.")
print("- Boolean masks are powerful for conditional updates.")
