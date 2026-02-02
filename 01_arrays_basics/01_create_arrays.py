"""
01_create_arrays.py

- how to create arrays
- how to check shape, ndim, dtype
- list vs NumPy array behavior
"""

import numpy as np

def show_info(name, arr):
    """Print the array and basic info about it."""
    print("\n" + name)
    print(arr)
    print("shape:", arr.shape)
    print("ndim :", arr.ndim)
    print("dtype:", arr.dtype)


if __name__ == "__main__":

    # ---------------------------
    # List vs NumPy array
    # ---------------------------
    print("\nList vs NumPy array : ")

    lst = [1, 2, 3]
    arr = np.array(lst)

    print("lst * 2  -> : ", lst * 2)     # list repeats (not math)
    print("arr * 2  -> : ", arr * 2)     # NumPy does element-wise math

    # ---------------------------
    # Creating arrays
    # ---------------------------
    print("\nCreating NumPy arrays : ")

    a1 = np.array([1, 2, 3])                 # 1D array
    a2 = np.array([[1, 2, 3], [4, 5, 6]])     # 2D array (2 rows, 3 columns)

    a3 = np.zeros((3, 4))                     # 2D array filled with 0
    a4 = np.ones((2, 3))                      # 2D array filled with 1

    a5 = np.empty((2, 3))                     # values are not guaranteed (garbage possible)
    a6 = np.arange(0, 10, 2)                  # 0 to 10 (not including 10), step 2
    a7 = np.linspace(0, 1, 5)                 # 5 values from 0 to 1 (including 1)

    a8 = np.eye(3)                            # identity matrix
    a9 = np.diag([1, 2, 3])                   # diagonal matrix

    a10 = np.zeros((2, 2), dtype=np.int32)    # same as zeros, but dtype is int32

    # Show all arrays + info
    show_info("a1 (np.array 1D)", a1)
    show_info("a2 (np.array 2D)", a2)
    show_info("a3 (np.zeros)", a3)
    show_info("a4 (np.ones)", a4)
    show_info("a5 (np.empty)  NOTE: values can be anything", a5)
    show_info("a6 (np.arange)", a6)
    show_info("a7 (np.linspace)", a7)
    show_info("a8 (np.eye)", a8)
    show_info("a9 (np.diag)", a9)
    show_info("a10 (zeros with dtype=int32)", a10)

    # ---------------------------
    # dtype example
    # ---------------------------
    print("\ndtype example")
    b1 = np.array([1, 2, 3])      # int
    b2 = np.array([1, 2, 3.0])    # float
    print("b1 dtype:", b1.dtype)
    print("b2 dtype:", b2.dtype)

    # ---------------------------
    # Mental model (short)
    # ---------------------------
    print("\nMental model (short)")
    print("- shape tells the size in each direction (axes)")
    print("- ndim tells how many directions (axes)")
    print("- dtype tells the type of values inside the array")
