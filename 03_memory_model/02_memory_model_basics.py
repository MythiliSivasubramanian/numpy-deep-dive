"""
    python 02_memory_model_basics.py
"""

import numpy as np

print("\n1) Array Ownership")
arr = np.array([10, 20, 30, 40])
print("Array:", arr)
print("arr.flags.owndata ->", arr.flags.owndata)
print("Meaning: True means this array owns its data buffer.")

print("\n2) Views from Slicing")
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
print("original:", original)
print("view:", view)
print("np.shares_memory(original, view) ->", np.shares_memory(original, view))

view[0] = 99
print("After view[0] = 99")
print("original:", original)
print("view:", view)
print("Why changed? view and original share memory.")

print("\n3) Explicit Copies")
original = np.array([5, 6, 7, 8])
copied = original.copy()
print("original:", original)
print("copied:", copied)
print("np.shares_memory(original, copied) ->", np.shares_memory(original, copied))

copied[0] = -1
print("After copied[0] = -1")
print("original:", original)
print("copied:", copied)
print("Why not changed? copied owns a different memory buffer.")

print("\n4) reshape (Often a View)")
arr_1d = np.arange(6)
arr_2d = arr_1d.reshape(2, 3)
print("arr_1d:", arr_1d)
print("arr_2d:\n", arr_2d)
print("np.shares_memory(arr_1d, arr_2d) ->", np.shares_memory(arr_1d, arr_2d))

arr_2d[0, 0] = 100
print("After arr_2d[0, 0] = 100")
print("arr_1d:", arr_1d)
print("arr_2d:\n", arr_2d)

# 5) Points:
# 1. Slicing usually gives a view (shared memory).
# 2. copy() gives a separate array (independent memory).
# 3. reshape often returns a view when layout allows.
# 4. Use np.shares_memory(a, b) to check sharing.
