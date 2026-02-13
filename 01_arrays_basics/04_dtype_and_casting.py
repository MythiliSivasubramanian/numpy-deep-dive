# 01_arrays_basics/04_dtype_and_casting.py
"""
03_dtype_and_casting.py

Focus:
- dtype inference
- why dtype changes (int -> float)
- converting dtype using astype
"""

import numpy as np


def show_dtype(name, arr):
    print(f"\n{name}")
    print(arr)
    print("dtype:", arr.dtype)
    print("shape:", arr.shape, "ndim:", arr.ndim)


if __name__ == "__main__":
    # dtype inference
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3.0])   # becomes float
    c = np.array([1, True, 3])  # gets upcast to a common dtype

    show_dtype("a = np.array([1,2,3])", a)
    show_dtype("b = np.array([1,2,3.0])", b)
    show_dtype("c = np.array([1, True, 3])", c)

    # dtype control at creation
    d = np.zeros((2, 2), dtype=np.int32)
    show_dtype("d = np.zeros((2,2), dtype=int32)", d)

    # converting dtype (creates a new array)
    e = b.astype(np.int32)
    show_dtype("e = b.astype(int32)", e)

    # show original not changed
    show_dtype("b (still float)", b)
