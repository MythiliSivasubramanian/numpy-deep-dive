"""
File        : 2d_array_slicing_and_modification.py
Topic       : NumPy Foundations
Practice    : 2D Array Indexing & Slicing

Problem:
Create a 3x3 NumPy array using values from 10 to 90 and perform multiple indexing and slicing operations.

Objectives:
1. Print array, shape, and number of dimensions
2. Extract the second row → [40, 50, 60]
3. Extract the third column → [30, 60, 90]
4. Extract submatrix block:
       50 60
       80 90
5. Modify entire first column to [999, 999, 999]

Concepts Covered:
- 2D array creation using arange() and reshape()
- Row indexing
- Column slicing
- Submatrix extraction
- Column mutation

"""

import numpy as np

# Create a 2D Array with 3*3 with given elements 10,20...90
num_array = np.arange(10,100,10).reshape(3,3)

# Print Array, shape and dimension
print("\n\n2D Array :\n",num_array,"\n\nShape :", num_array.shape,"\nDimension :", num_array.ndim,"\n")

# Extract only 2ndrow elements.40,50,60
print("2nd Row elements :", num_array[1])

# Extract only column elements 30,60,90
print("\n3rd Column elements :\n", num_array[:,2])

"""
Extract this block: 
50 60
80 90
"""

print("\nExtracting specific block from array :\n", num_array[1:3,1:3])

# Modify a Column : Change entire column 0 to: [999, 999, 999] and print updated array.
num_array[:,0] = 999

print("\nUpdating column 0 as 999 :\n", num_array)