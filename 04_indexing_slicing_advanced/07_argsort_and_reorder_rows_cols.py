"""
07_argsort_and_reorder_rows_cols.py

Focus:
- argsort gives the index order for sorting
- reordering rows/columns using fancy indexing
- common in data analysis (sort by a column)
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


header("Setup")
x = np.array([
    [10,  3, 100],
    [ 5,  9, 200],
    [ 7,  1, 150],
    [12,  4, 120]
])
print("x:\n", x)
print("Columns: [col0, col1, col2]")


header("1) Sort rows by column 1 (second column)")
order = np.argsort(x[:, 1])  # indices that would sort column 1
print("argsort order:", order)

sorted_rows = x[order]
print("Rows sorted by column 1:\n", sorted_rows)


header("2) Sort rows by column 2 (third column)")
order2 = np.argsort(x[:, 2])
print("argsort order:", order2)

sorted_rows2 = x[order2]
print("Rows sorted by column 2:\n", sorted_rows2)


header("3) Reorder columns")
# swap columns: [col2, col0, col1]
reordered_cols = x[:, [2, 0, 1]]
print("Columns reordered [2,0,1]:\n", reordered_cols)


header("4) Important note")
print("- x[order] is fancy indexing -> usually a copy")
print("- It is great for reordering data safely")
