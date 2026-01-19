import numpy as np

# -------------------------------
# 1D Array (One-Dimensional)
# -------------------------------
arr_1d = np.array([10, 20, 30, 40, 50])

print(f'1D Array: {arr_1d}')
# Output: 1D Array: [10 20 30 40 50]

print(f'1D Array dimensions: {arr_1d.ndim}')
# Output: 1D Array dimensions: 1

print(f'1D Array shape: {arr_1d.shape}')
# Output: 1D Array shape: (5,)


# -------------------------------
# 2D Array (Two-Dimensional)
# -------------------------------
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])

print(f'\n2D Array:\n{arr_2d}')
# Output:
# 2D Array:
# [[10 20 30]
#  [40 50 60]]

print(f'2D Array dimensions: {arr_2d.ndim}')
# Output: 2D Array dimensions: 2

print(f'2D Array shape: {arr_2d.shape}')
# Output: 2D Array shape: (2, 3)


# -------------------------------
# Multi-Dimensional Array (3D)
# -------------------------------
arr_md = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[10, 11, 12], [13, 14, 15]]
])

print(f'\nMulti-Dimensional Array:\n{arr_md}')
# Output:
# Multi-Dimensional Array:
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[10 11 12]
#   [13 14 15]]]

print(f'Multi-Dimensional Array dimensions: {arr_md.ndim}')
# Output: Multi-Dimensional Array dimensions: 3

print(f'Multi-Dimensional Array shape: {arr_md.shape}')
# Output: Multi-Dimensional Array shape: (2, 2, 3)