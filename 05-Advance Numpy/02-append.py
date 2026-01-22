import numpy as np 

# append() is used to add elements at the end of an array.
# Syntax: np.append(array, values, axis=None)

arr_1D = np.array([10, 20, 30, 40]) 

print(f'Original 1D Array: {arr_1D}')
# Output: Original 1D Array: [10 20 30 40]

print(f'\nAppend a single value 50: {np.append(arr_1D, 50)}') 
# Output: Append a single value 50: [10 20 30 40 50]

print(f'\nAppend multiple values [60, 70]: {np.append(arr_1D, [60, 70])}')
# Output: Append multiple values [60, 70]: [10 20 30 40 60 70]


arr_2D = np.array([
  [10, 20, 30],
  [40, 50, 60]
]) 

print(f'\nOriginal 2D array: \n{arr_2D}') 
# Output: Original 2D array:
# [[10 20 30]
#  [40 50 60]]

print(f'\nAppend value 99 (axis=None): {np.append(arr_2D, 99)}') 
# Output: Append value 99 (axis=None): [10 20 30 40 50 60 99]

# Row-wise
print(f'\nAppend a new row: \n{np.append(arr_2D, [[70, 80, 90]], axis=0)}') 
# Output: Append a new row:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Column-wise 
print(f'\nAppend a new column: \n{np.append(arr_2D, [[88], [99]], axis=1)}')
# Output: Append a new column:
# [[10 20 30 88]
#  [40 50 60 99]]