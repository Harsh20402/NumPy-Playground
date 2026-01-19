import numpy as np 

# Number of dimensions in an array
# Syntax: array.ndim

# -----------------------------
# 1D Array
# -----------------------------
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print('1D Array:')
# Output: 1D Array:
print(arr_1d)
# Output: [1 2 3 4 5 6 7 8]
print(f'No. of dimension\'s is {arr_1d.ndim}.')
# Output: No. of dimension's is 1.


# -----------------------------
# 2D Array
# -----------------------------
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print('\n2D Array:')
# Output: 2D Array:
print(arr_2d)
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]
print(f'No. of dimension\'s is {arr_2d.ndim}.')
# Output: No. of dimension's is 2.


# -----------------------------
# Multi-Dimensional (3D) Array
# -----------------------------
arr_multi = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [10, 11, 12, 13],
        [14, 15, 16, 17]
    ],
    [
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [30, 31, 32, 33],
        [34, 35, 36, 37]
    ]
])

print("\nMulti-Dimensional Array:")
# Output: Multi-Dimensional Array:
print(arr_multi)
# Output:
# [[[ 1  2  3  4]
#   [ 5  6  7  8]
#   [10 11 12 13]
#   [14 15 16 17]]
#
#  [[20 21 22 23]
#   [24 25 26 27]
#   [30 31 32 33]
#   [34 35 36 37]]]
print(f'No. of dimension\'s is {arr_multi.ndim}.')
# Output: No. of dimension's is 3.
