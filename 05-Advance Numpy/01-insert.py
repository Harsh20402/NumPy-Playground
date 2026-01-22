import numpy as np 

# insert() is used to add new elements at a specified index in an array.
# Syntax: np.insert(array, index, value, axix=None) 

# axis=0 → row insertion
# axis=1 → column insertion 


arr_1D = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f"Original 1D Array: {arr_1D}") 
# Output: Original 1D Array: [ 10  20  30  40  50  60  70  80  90 100]

print(f"\nInsert 99 at index 2: {np.insert(arr_1D, 2, 99)}")
# Output: Insert 99 at index 2: [ 10  20  99  30  40  50  60  70  80  90 100]

print(f'\nInsert multiple values at index 1: {np.insert(arr_1D, 1, [55, 66])}') 
# Output: Insert multiple values at index 1: [ 10  55  66  20  30  40  50  60  70  80  90 100] 


arr_2D = np.array([
  [10, 20, 30],
  [40, 50, 60]
])

print(f'\nOriginal 2D array:\n{arr_2D}') 
# Output: Original 2D array:
# [[10 20 30]
#  [40 50 60]]

# Row-wise
print(f'\nInsert a new row at index 1:\n{np.insert(arr_2D, 1, [70, 80, 90], axis=0)}')
# Output: Insert a new row at index 1:
# [[10 20 30]
#  [70 80 90]
#  [40 50 60]]

# Column-wise
print(f'\nInsert a new column at index 2:\n{np.insert(arr_2D, 2, [88, 99], axis=1)}')
# Output: Insert a new column at index 2:
# [[10 20 88 30]
#  [40 50 99 60]]