"""
File: Array Slice Analyzer
Create an array 10,20,30,40,50,60,70
Print basic info : Array, Shape, Number of dimensions, Data type
"""

# Import numpy as np
import numpy as np

# Create an np.array 10,20,30,40,50,60,70
numbers_array = np.arange(10,80,10)

# Print basic info : Array, Shape, No of dimensions, data type
print("\n\nArray is :", numbers_array)
print("Shape :", numbers_array.shape)
print("No of Dimensions :", numbers_array.ndim)
print("Data type :", numbers_array.dtype,"\n")

"""
Task 2 — Slicing Create a slice:so it has only 20,30,40,50
"""
# Slice [1:5] 20,30,40,50    By default indesx starts at 0
# Slicing = view only. Shared memory. 
sliced_array = numbers_array[1:5] # Stop index is not inclusive
print("\nNew array(sliced_array) after slicing from Numbers_array[1:5] :", sliced_array)

"""
Task 3 — Modify Slice : Change first element of slice: as 999.
print both original and sliced array
"""
# update 1st element of sliced array as 999
sliced_array[0] = 999
print("\nUpdating 1st element of sliced array as 999")
# Print both arrays (numbers_array and sliced array)
print("\nOriginal array :", numbers_array,"\nSliced array(after updation :",sliced_array)

"""
Task 4 — Create Real Copy with 30,40,50,60 from numbers_array. Modify 1st elemnt of copied array as 555
Print both arrays
"""

# Creating a copy of sliced array . .copy() - New memory allocated
# Since memory is shared in slicing, original will be affected
copied_array = numbers_array[2:6].copy() # Array elements 30,40,50,60 (stop index exclusive)
print("\nNumbers Array :", numbers_array)
print("\nReal Copied array from numbers_array with slicing[2:6]:", copied_array)

# Update 1st element of copied array as 555
copied_array[0] = 555

# Print both arrays (numbers_array) and (copied_array)
print("\nAfter updating 1st element of copied_array as 555 :\n\n")
print("Numbers_array :", numbers_array)
print("Copied_array :", copied_array,"\n")