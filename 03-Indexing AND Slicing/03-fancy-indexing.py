import numpy as np 

# Fancy indexing allows you to access multiple elements at once
# using a list or array of indices instead of a slice.

# 1D Syntax: arr[[index1, index2, ...]]
# 2D Syntax: arr[[row_indices], [column_indices]]
# 3D Syntax: arr[[layer_indices], [row_indices], [column_indices]]


# -----------------------------
# 1D Array
# -----------------------------
arr_1D = np.array([10, 20, 30, 40, 50, 60]) 

print('1D Array:') 
# Output:
# 1D Array:
print(arr_1D)
# Output:
# [10 20 30 40 50 60]

print(f'Element at index [0, 2, 4]: {arr_1D[[0, 2, 4]]}')
# Output:
# Element at index [0, 2, 4]: [10 30 50]

print(f'Element using negative indexing [-1, -3]: {arr_1D[[-1, -3]]}')
# Output:
# Element using negative indexing [-1, -3]: [60 40]


# -----------------------------
# 2D Array
# -----------------------------
arr_2D = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]) 

print('\n2D Array:') 
# Output:
# 2D Array:
print(arr_2D)
# Output:
# [[ 10  20  30  40]
#  [ 50  60  70  80]
#  [ 90 100 110 120]]

print(f'Select rows 0 and 2:\n{arr_2D[[0,2]]}')
# Output:
# Select rows 0 and 2:
# [[ 10  20  30  40]
#  [ 90 100 110 120]]

print(f'Select elements at (0, 1), (1, 2), (2, 3): \n{arr_2D[[0, 1, 2], [1, 2, 3]]}')
# Output:
# Select elements at (0, 1), (1, 2), (2, 3):
# [ 20  70 120]

print(f'Select elements at (0, 3), (1, 2), (2, 1):\n{arr_2D[[0, 1, 2], [3, 2, 1]]}')
# Output:
# Select elements at (0, 3), (1, 2), (2, 1):
# [ 40  70 100]


# -----------------------------
# 3D Array
# -----------------------------
arr_3D = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
]) 

print('\n3D Array:') 
# Output:
# 3D Array:
print(arr_3D)
# Output:
# [[[ 10  20  30]
#   [ 40  50  60]]
#
#  [[ 70  80  90]
#   [100 110 120]]]

print(f'Select layers 0 and 1:\n{arr_3D[[0, 1]]}')
# Output:
# Select layers 0 and 1:
# [[[ 10  20  30]
#   [ 40  50  60]]
#
#  [[ 70  80  90]
#   [100 110 120]]]

print(arr_3D[[1], [1], [2]])
# Output:
# [120]
