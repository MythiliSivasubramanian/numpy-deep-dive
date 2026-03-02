"""
    python 03_array_memory_info.py
"""

import numpy as np

print("Array 1: basic memory info")
a = np.array([10, 20, 30, 40], dtype=np.int32)
print("a:", a)
print("a.dtype:", a.dtype)
print("a.itemsize (bytes per element):", a.itemsize)
print("a.size (number of elements):", a.size)
print("a.nbytes (total bytes):", a.nbytes)
print("a.ndim:", a.ndim)
print("a.shape:", a.shape)

print("\nArray 2: view and base")
b = a[1:4]
print("b:", b)
print("b.base is a:", b.base is a)
print("np.shares_memory(a, b):", np.shares_memory(a, b))

b[0] = 999
print("After b[0] = 999")
print("a:", a)
print("b:", b)

print("\nArray 3: copy and independent memory")
c = a.copy()
print("c:", c)
print("c.base:", c.base)
print("np.shares_memory(a, c):", np.shares_memory(a, c))

c[0] = -1
print("After c[0] = -1")
print("a:", a)
print("c:", c)

# Quick notes:
# - itemsize: bytes used by one element
# - nbytes: total bytes used by array elements
# - base: points to original array for a view; None for owned data
# - shares_memory: True means arrays use some common memory
