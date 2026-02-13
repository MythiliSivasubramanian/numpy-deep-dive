# 01_arrays_basics/03_dimensions_shape_ndim.py
"""
03_dimensions_shape_ndim.py

Focus:
- 0D, 1D, 2D, 3D arrays
- how to check dimensions using shape and ndim
- total number of elements (size)
"""

import numpy as np


def show_dim_info(name, arr):
    print(f"\n{name}")
    print(arr)
    print("shape:", arr.shape)
    print("ndim :", arr.ndim)
    print("size :", arr.size)
    print("dtype:", arr.dtype)


if __name__ == "__main__":
    # 0D array (scalar-like)
    a0 = np.array(5)

    # 1D array
    a1 = np.array([10, 20, 30, 40])

    # 2D array (table)
    a2 = np.array([[1, 2, 3],
                   [4, 5, 6]])

    # 3D array (stack of tables)
    a3 = np.zeros((2, 3, 4))

    show_dim_info("a0 (0D array)", a0)
    show_dim_info("a1 (1D array)", a1)
    show_dim_info("a2 (2D array)", a2)
    show_dim_info("a3 (3D array)", a3)

    # Key rule
    print("\nRule check: ndim == len(shape)")
    for name, arr in [("a0", a0), ("a1", a1), ("a2", a2), ("a3", a3)]:
        print(name, "->", arr.ndim == len(arr.shape))
