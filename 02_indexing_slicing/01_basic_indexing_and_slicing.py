"""
01_basic_indexing_and_slicing.py

Demonstrates:
- Basic indexing (single elements)
- Row and column slicing
- Submatrix slicing
- Negative indexing
- Step slicing
- View behavior (shared memory)
"""

import numpy as np

# Create a 2D array
x = np.arange(12).reshape(3, 4)

print("Original array:\n", x)
print("shape:", x.shape, "ndim:", x.ndim)


# 1. Basic indexing
print("\nBasic indexing (single elements)")
print("x[0, 0] =", x[0, 0])   # first row, first column
print("x[2, 3] =", x[2, 3])   # last row, last column


# 2. Row and column slicing
print("\nRow and column slicing")
print("First row:\n", x[0, :])     # row 0, all columns
print("First column:\n", x[:, 0])  # all rows, column 0


# 3. Submatrix slicing
print("\nSubmatrix slicing")

submatrix = x[0:2, 1:3]   # rows 0-1, columns 1-2
print(submatrix)

# 4. Slicing returns a VIEW
print("\nView behavior")

sub = x[:, 1:3]   # slice columns 1 and 2
sub[0, 0] = 999   # modify slice

print("Sub array:\n", sub)
print("Original array changed:\n", x)


# Reset array for clean examples
x = np.arange(12).reshape(3, 4)

# 5. Negative indexing
print("\nNegative indexing")

print("Last row:\n", x[-1])
print("Last column:\n", x[:, -1])
print("Bottom-right element:", x[-1, -1])


# 6. Step slicing
print("\nStep slicing")

print("Every 2nd column:\n", x[:, ::2])
print("Reverse rows:\n", x[::-1])

# 7. Full slice vs copy
print("\nFull slice vs copy")

a = np.arange(6)

view = a[:]       # view
copy = a.copy()   # copy

view[0] = 999

print("a after modifying view:", a)
print("copy remains unchanged:", copy)


# 8. Shape after slicing
print("\nShape after slicing")

row = x[0]
col = x[:, 0]

print("Row shape:", row.shape)
print("Column shape:", col.shape)