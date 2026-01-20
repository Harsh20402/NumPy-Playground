import numpy as np

# Filtering (Boolean Indexing) selects elements based on conditions
# Syntax:
# 1D: arr[condition]
# 2D: arr[condition]
# 3D: arr[condition]

arr_1D = np.array([10, 25, 30, 45, 50, 65])

print('1D Array:')
# Output:
# 1D Array:
print(arr_1D)
# Output:
# [10 25 30 45 50 65]

print(f'Elements greater than 30: {arr_1D[arr_1D > 30]}')
# Output:
# Elements greater than 30: [45 50 65]

print(f'Elements less than or equal to 30: {arr_1D[arr_1D <= 30]}')
# Output:
# Elements less than or equal to 30: [10 25 30]

print(f'Elements greater than 20 and less than 60: {arr_1D[(arr_1D > 20) & (arr_1D < 60)]}')
# Output:
# Elements greater than 20 and less than 60: [25 30 45 50]


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

print(f'Elements greater than 50:\n{arr_2D[arr_2D > 50]}')
# Output:
# Elements greater than 50:
# [ 60  70  80  90 100 110 120]

print(f'Rows where first column > 40:\n{arr_2D[arr_2D[:, 0] > 40]}')

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

print(f'Elements greater than 60:\n{arr_3D[arr_3D > 60]}')
# Output:
# Elements greater than 60:
# [ 70  80  90 100 110 120]
