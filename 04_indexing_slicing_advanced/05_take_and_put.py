"""
05_take_and_put.py

Focus:
- Selecting using indices with np.take
- Updating using np.put (flat indexing)
- Good for learning "index-based" selection/update
"""

import numpy as np


def header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


header("Setup")
x = np.arange(12).reshape(3, 4)
print("x:\n", x)


header("1) np.take - take elements by indices (flat by default)")
# flat indices (0..11)
taken = np.take(x, [0, 5, 11])
print("np.take(x, [0, 5, 11]) ->", taken)
print("Meaning: x flattened, then picked elements at positions 0,5,11")


header("2) np.take with axis (take by row/col)")
rows = np.take(x, [0, 2], axis=0)
print("Take rows 0 and 2:\n", rows)

cols = np.take(x, [1, 3], axis=1)
print("Take columns 1 and 3:\n", cols)


header("3) np.put - replace values using flat indices")
y = x.copy()
print("Before np.put:\n", y)

np.put(y, [0, 5, 11], [999, 555, 111])
print("After np.put at flat indices [0,5,11]:\n", y)


header("4) np.put with repeated indices")
z = x.copy()
np.put(z, [0, 0, 0], [9, 8, 7])
print("Replace flat index 0 multiple times:\n", z)
print("Last value wins (7).")
