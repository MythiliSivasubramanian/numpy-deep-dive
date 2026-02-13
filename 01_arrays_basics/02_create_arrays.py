# 01_arrays_basics/01_create_arrays.py
"""
02_create_arrays.py

Basics:
- create NumPy arrays
- inspect shape, ndim, dtype
- quick list vs NumPy behavior
"""

import numpy as np


def show_info(name, arr):
    print(f"\n{name}")
    print(arr)
    print("shape:", arr.shape)
    print("ndim :", arr.ndim)
    print("dtype:", arr.dtype)


if __name__ == "__main__":
    # List vs NumPy array
    lst = [1, 2, 3]
    arr = np.array(lst)
    print("List vs NumPy array")
    print("lst * 2 ->", lst * 2)   # list repeats (not math)
    print("arr * 2 ->", arr * 2)   # NumPy does element-wise math

    # Create arrays
    a1 = np.array([1, 2, 3])                   # 1D
    a2 = np.array([[1, 2, 3], [4, 5, 6]])      # 2D

    a3 = np.zeros((3, 4))                      # zeros
    a4 = np.ones((2, 3))                       # ones
    a5 = np.empty((2, 3))                      # uninitialized (values can be anything)
    a6 = np.arange(0, 10, 2)                   # step-based range
    a7 = np.linspace(0, 1, 5)                  # count-based range

    a8 = np.eye(3)                             # identity matrix
    a9 = np.diag([1, 2, 3])                    # diagonal matrix

    a10 = np.zeros((2, 2), dtype=np.int32)     # dtype control example

    show_info("a1 (np.array 1D)", a1)
    show_info("a2 (np.array 2D)", a2)
    show_info("a3 (np.zeros)", a3)
    show_info("a4 (np.ones)", a4)
    show_info("a5 (np.empty) NOTE: values not guaranteed", a5)
    show_info("a6 (np.arange)", a6)
    show_info("a7 (np.linspace)", a7)
    show_info("a8 (np.eye)", a8)
    show_info("a9 (np.diag)", a9)
    show_info("a10 (zeros dtype=int32)", a10)
