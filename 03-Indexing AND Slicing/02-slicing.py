import numpy as np

# Slicing is used to extract a portion of an array instead of a single element.
# 1D: arr[start:stop:step]
# 2D: arr[row_start:row_end, col_start:col_end]
# 3D: arr[layer_slice, row_slice, column_slice]


# -----------------------------
# 1D Array Slicing
# -----------------------------
arr_1D = np.array([10, 20, 30, 40, 50, 60])

print('1D Array:')
# Output:
# 1D Array:
print(arr_1D)
# Output:
# [10 20 30 40 50 60]

print(f'Slice from index 1 to 4: {arr_1D[1:4]}.')
# Output:
# Slice from index 1 to 4: [20 30 40].

print(f'Slice from start to index 3: {arr_1D[:3]}.')
# Output:
# Slice from start to index 3: [10 20 30].

print(f'Slice from index 2 to end: {arr_1D[2:]}.')
# Output:
# Slice from index 2 to end: [30 40 50 60].

print(f'Reverse the array: {arr_1D[::-1]}')
# Output:
# Reverse the array: [60 50 40 30 20 10]


# -----------------------------
# 2D Array Slicing
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

print(f'First two rows: \n{arr_2D[:2, :]}')
# Output:
# First two rows:
# [[10 20 30 40]
#  [50 60 70 80]]

print(f'First two columns: \n{arr_2D[:, :3]}')
# Output:
# First two columns:
# [[ 10  20  30]
#  [ 50  60  70]
#  [ 90 100 110]]

print(f'Sub-Matrix (row 0-1, columns 1-2): \n{arr_2D[:2, 1:3]}')
# Output:
# Sub-Matrix (row 0-1, columns 1-2):
# [[20 30]
#  [60 70]]


# -----------------------------
# 3D Array Slicing
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

print("\n3D Array:")
# Output:
# 3D Array:
print(arr_3D)
# Output:
# [[[ 10  20  30]
#   [ 40  50  60]]
#
#  [[ 70  80  90]
#   [100 110 120]]]

print(f'First Layer: \n{arr_3D[0]}')
# Output:
# First Layer:
# [[10 20 30]
#  [40 50 60]]

print(f'All Layer, first row: \n{arr_3D[:, 0:1, :]}')
# Output:
# All Layer, first row:
# [[[10 20 30]]
#  [[70 80 90]]]

print(f'All Layer, column index 1:\n{arr_3D[:,:,1:2]}')
# Output:
# All Layer, column index 1:
# [[[ 20]
#   [ 50]]
#
#  [[ 80]
#   [110]]]
