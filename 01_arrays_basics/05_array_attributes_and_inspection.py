# 01_arrays_basics/05_array_attributes_and_inspection.py
"""
04_array_attributes_and_inspection.py

Focus:
- Inspect important ndarray attributes
- Understand memory-related attributes (itemsize, nbytes)
"""

import numpy as np


def show_attrs(name, arr):
    print(f"\n{name}")
    print(arr)
    print("shape   :", arr.shape)
    print("ndim    :", arr.ndim)
    print("size    :", arr.size)       # total number of elements
    print("dtype   :", arr.dtype)
    print("itemsize:", arr.itemsize)   # bytes per element
    print("nbytes  :", arr.nbytes)     # total bytes (size * itemsize)


if __name__ == "__main__":
    a1 = np.array([1, 2, 3, 4])
    a2 = np.arange(12).reshape(3, 4)
    a3 = np.zeros((2, 3), dtype=np.int32)

    show_attrs("a1 (1D array)", a1)
    show_attrs("a2 (2D array)", a2)
    show_attrs("a3 (zeros int32)", a3)

    # Quick reminder: nbytes = size * itemsize
    print("\nCheck: nbytes == size * itemsize")
    for name, arr in [("a1", a1), ("a2", a2), ("a3", a3)]:
        print(name, "->", arr.nbytes == arr.size * arr.itemsize)
