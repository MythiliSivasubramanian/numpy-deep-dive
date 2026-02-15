import numpy as np

# Predefined array
b = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\n\nPredefined Array :\n",b)

# Accessing element 60
print("\nPrinting the element 60 :")
print((b[1,2]))


# Filter all values greater than 40
print("\n\nFiltering all values greater than 40 :")
print(b[b > 40])

# Print elements 10, 60, 80
"""
Print elements 10, 60, 80
10  -> (0,0)
60  -> (1,2)
80  -> (2,1)
"""
# Fancy indexing: array[[rows],[columns]]
print("\n\nPrinting elements 10, 60, 80 :")
print(b[[0,1,2],[0,2,1]])

# Update all values greater than 50 as 999
b[b > 50] = 999
print("\n\nUpdating all values greater than 50 as 999 :")
print(b)

# Update all values less than 30 as 0
b[b < 30] = 0
print("\n\nUpdating all values less than 30 as 0 :")
print(b)

# Conditional replacement
# Set values > 80 to 80 and values < 20 to 20
# Clipping / Outlier Handling
print("\n\nSet values > 80 to 80 and values < 20 to 20 ")
b[b > 80] = 80
b[b < 20] = 20
print(b)

# Build in np.clip(array, min,max)
b = np.clip(b, 20,80)
print("\n\n",b)

# Set values between 30 and 70 to 999
b[(b > 30) & (b < 70)] = 999
print("\n\nValues between 30 und 70 to 999 :")
print(b)