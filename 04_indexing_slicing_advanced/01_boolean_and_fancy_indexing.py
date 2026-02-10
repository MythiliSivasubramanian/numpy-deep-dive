"""
01_boolean_and_fancy_indexing.py

Advanced indexing reference:
- Boolean indexing (filtering) + assignment
- np.where (values + indices)
- Fancy indexing (lists/arrays of indices)
- Common pitfall: pair selection vs submatrix
- Correct submatrix with np.ix_
- View vs copy: slicing vs fancy indexing

Run:
python 01_boolean_and_fancy_indexing.py
"""

import numpy as np


def header(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# 1) Setup array
# ------------------------------------------------------------
header("1) Setup array")
x = np.arange(12).reshape(3, 4)
print("x:\n", x)
print("shape:", x.shape, "ndim:", x.ndim)


# ------------------------------------------------------------
# 2) Boolean indexing (filtering)
# ------------------------------------------------------------
header("2) Boolean indexing (filtering)")
mask = x > 5
print("mask = (x > 5):\n", mask)

print("\nx[mask]  (values where mask is True):")
print(x[mask])

print("\nx[x > 5]  (shortcut):")
print(x[x > 5])

print("\nNote: Boolean indexing usually returns a COPY (1D result).")


# ------------------------------------------------------------
# 3) Boolean indexing assignment
# ------------------------------------------------------------
header("3) Boolean indexing assignment")
x = np.arange(12).reshape(3, 4)
print("before:\n", x)

x[x > 5] = 100
print("\nafter x[x > 5] = 100:\n", x)
print("\nThis modifies x directly (mask assignment).")


# ------------------------------------------------------------
# 4) np.where
# ------------------------------------------------------------
header("4) np.where")

x = np.arange(12).reshape(3, 4)
y = np.where(x > 5, 1, 0)
print("y = np.where(x > 5, 1, 0):\n", y)

idx = np.where(x > 5)
print("\nidx = np.where(x > 5) returns (row_indices, col_indices):")
print(idx)

print("\nExample positions where x > 5:")
for r, c in zip(idx[0], idx[1]):
    print(f"x[{r},{c}] = {x[r, c]}")


# ------------------------------------------------------------
# 5) Fancy indexing (rows / columns)
# ------------------------------------------------------------
header("5) Fancy indexing (rows / columns)")

x = np.arange(12).reshape(3, 4)
rows = [0, 2]
print("rows =", rows)
print("x[rows]:\n", x[rows])
print("\nNote: Fancy indexing usually returns a COPY.")

cols = [1, 3]
print("\ncols =", cols)
print("x[:, cols]:\n", x[:, cols])


# ------------------------------------------------------------
# 6) Pitfall: selecting rows and cols together (pairs)
# ------------------------------------------------------------
header("6) Pitfall: x[[rows],[cols]] selects PAIRS (not a submatrix)")

x = np.arange(12).reshape(3, 4)
rows = [0, 2]
cols = [1, 3]

print("x:\n", x)
print("\nrows =", rows, "cols =", cols)
print("x[[0,2],[1,3]] -> selects (0,1) and (2,3):")
print(x[rows, cols])  # pair selection


# ------------------------------------------------------------
# 7) Correct submatrix with np.ix_
# ------------------------------------------------------------
header("7) Correct submatrix with np.ix_")

x = np.arange(12).reshape(3, 4)
rows = [0, 2]
cols = [1, 3]

submatrix = x[np.ix_(rows, cols)]
print("rows =", rows, "cols =", cols)
print("x[np.ix_(rows, cols)] gives a submatrix:\n", submatrix)


# ------------------------------------------------------------
# 8) View vs copy test: slicing vs fancy indexing
# ------------------------------------------------------------
header("8) View vs copy: slicing vs fancy indexing")

x = np.arange(12).reshape(3, 4)
a = x[:, 1:3]      # basic slicing -> usually a VIEW
b = x[:, [1, 2]]   # fancy indexing -> usually a COPY

print("x before:\n", x)
print("\na (slice x[:, 1:3]):\n", a)
print("\nb (fancy x[:, [1,2]]):\n", b)

a[0, 0] = 999
print("\nAfter a[0,0] = 999")
print("x changed (because a is a view):\n", x)
print("b unchanged (because b is a copy):\n", b)

print("\nRule of thumb:")
print("- Basic slicing -> view (shares memory)")
print("- Boolean/fancy indexing -> copy (new array)")