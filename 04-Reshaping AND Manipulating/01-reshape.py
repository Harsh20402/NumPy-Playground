import numpy as np 

# Syntax: reshape(row, column) to specify new shape || if dimension match 

arr_1D = np.array([1, 2, 3, 4, 5, 6])

print('Original 1D Array:')
# Output:
# Original 1D Array:
print(arr_1D)
# Output:
# [1 2 3 4 5 6]

print('Reshape to 2 rows and 3 columns:')
# Output:
# Reshape to 2 rows and 3 columns:
print(arr_1D.reshape(2, 3))
# Output:
# [[1 2 3]
#  [4 5 6]]

print('Reshape to 1 layer, 2 rows, 3 columns:')
# Output:
# Reshape to 1 layer, 2 rows, 3 columns:
print(arr_1D.reshape(1, 2, 3))
# Output:
# [[[1 2 3]
#   [4 5 6]]]

arr_2D = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print('\nOriginal 2D Array:')
# Output:
# Original 2D Array:
print(arr_2D)
# Output:
# [[10 20 30]
#  [40 50 60]]

print('Reshape to 3 rows and 2 columns:')
# Output:
# Reshape to 3 rows and 2 columns:
print(arr_2D.reshape(3, 2))
# Output:
# [[10 20]
#  [30 40]
#  [50 60]]

print('Reshape using -1 (automatic calculation):')
# Output:
# Reshape using -1 (automatic calculation):
print(arr_1D.reshape(3, -1))
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

arr_2D_new = arr_2D.reshape(-1)

print('Flattened Array:')
# Output:
# Flattened Array:
print(arr_2D_new)
# Output:
# [10 20 30 40 50 60]
