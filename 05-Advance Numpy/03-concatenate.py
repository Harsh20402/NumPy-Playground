import numpy as np 

# concatenate() is used to join two or more arrays along an existing axis.
# Syntax: np.concatenate((array1, array2, ......., arrayN), axis=None)

arr_1 = np.array([10, 20, 30])
arr_2 = np.array([40, 50, 60])

print(f'Array 1: {arr_1}') 
# Output: Array 1: [10 20 30]

print(f'\nArray 2: {arr_2}') 
# Output: Array 2: [40 50 60]

# Concatenate 1D Arrays
print(f'\nConcatenate 1D arrays: {np.concatenate((arr_1, arr_2))}')
# Output: Concatenate 1D arrays: [10 20 30 40 50 60]

# Concatenate 2D Arrays (Row-wise -> Axis=0)
arr_2D_A = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

arr_2D_B = np.array([
  [7, 8, 9],
  [10, 11, 12]
])

print(f'\n2D Array A:\n{arr_2D_A}')
# Output: 2D Array A:
# [[1 2 3]
#  [4 5 6]]

print(f'\n2D Array B:\n{arr_2D_B}')
# Output: 2D Array B:
# [[ 7  8  9]
#  [10 11 12]]

print(f'\nConcatenate along rows (axis=0):\n{np.concatenate((arr_2D_A, arr_2D_B), axis=0)}')
# Output: Concatenate along rows (axis=0):
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]


print(f'\nConcatenate alon columns (axis=1):\n{np.concatenate((arr_2D_A, arr_2D_B), axis=1)}')
# Output: Concatenate alon columns (axis=1):
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]