import numpy as np

# -----------------------------
# 1D Array
# -----------------------------
arr_1d = np.array([1, 2, 3, 4, 5])

print("1D Array:")
# Output: 1D Array:
print(arr_1d)
# Output: [1 2 3 4 5]
print("1D Array shape:", arr_1d.shape)
# Output: 1D Array shape: (5,)  || Only one dimension | Length of that dimension is 5 ||


# -----------------------------
# 2D Array
# -----------------------------
arr_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print("\n2D Array:")
# Output: 2D Array:
print(arr_2d)
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]
print("2D Array shape:", arr_2d.shape)
# Output: 2D Array shape: (2, 4) || 2 rows | 4 columns ||


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
print("Multi-Dimensional Array shape:", arr_multi.shape)
# Output: Multi-Dimensional Array shape: (2, 4, 4) || 2 blocks (layers) | Each block has 4 rows | Each row has 4 columns ||
