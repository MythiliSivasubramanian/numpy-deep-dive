"""
    python 04_ravel_vs_flatten.py
"""

import numpy as np

print("Original 2D array")
a = np.array([[1, 2, 3], [4, 5, 6]])
print("a:\n", a)

print("\nUsing ravel()")
r = a.ravel()
print("r:", r)
print("np.shares_memory(a, r):", np.shares_memory(a, r))

r[0] = 99
print("After r[0] = 99")
print("a:\n", a)
print("r:", r)

print("\nUsing flatten()")
f = a.flatten()
print("f:", f)
print("np.shares_memory(a, f):", np.shares_memory(a, f))

f[1] = -1
print("After f[1] = -1")
print("a:\n", a)
print("f:", f)

# Quick notes:
# - ravel() often returns a view when possible (memory can be shared)
# - flatten() always returns a copy (independent memory)
