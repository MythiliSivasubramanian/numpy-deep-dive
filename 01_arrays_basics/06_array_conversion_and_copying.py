# 01_arrays_basics/06_array_conversion_and_copying.py
"""
06_array_conversion_and_copying.py

Focus:
- Convert between Python lists and NumPy arrays
- Understand view vs copy using .copy()
- Avoid accidental changes when you need an independent array
"""

import numpy as np


if __name__ == "__main__":
    # List -> NumPy array
    lst = [1, 2, 3]
    arr = np.array(lst)

    print("List -> array")
    print("lst:", lst)
    print("arr:", arr)
    print("arr dtype:", arr.dtype)

    # NumPy array -> list
    back_to_list = arr.tolist()
    print("\nArray -> list")
    print("back_to_list:", back_to_list, "type:", type(back_to_list))

    # Full slice gives a view (shares data)
    x = np.arange(6)
    view = x[:]          # view (shares memory)
    copy = x.copy()      # copy (new memory)

    print("\nView vs copy")
    print("x   :", x)
    print("view:", view)
    print("copy:", copy)

    view[0] = 999
    print("\nAfter view[0] = 999")
    print("x   :", x, " (changed because view shares data)")
    print("view:", view)
    print("copy:", copy, " (unchanged)")

    # Copy from a slice (safe independent array)
    y = np.arange(10)
    sub_copy = y[2:6].copy()
    sub_copy[0] = -1

    print("\nCopy from a slice")
    print("y       :", y, " (unchanged)")
    print("sub_copy:", sub_copy, " (independent)")
