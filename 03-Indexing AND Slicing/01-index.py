import numpy as np 

# To access a particular element using index.
# For 1D Array: arr[index]
# For 2D Array: arr[row, column]
# For Multi-Dimensional (3D) Array: arr[layer, row, column]

# -----------------------------
# 1D Array
# -----------------------------
arr_1D = np.array([10, 20, 30, 40, 50]) 

print('1D Array:') 
# Output: 1D Array:
print(arr_1D) 
# Output: [10 20 30 40 50]

print(f'The first element is: {arr_1D[0]}.')
# Output: The first element is: 10.

print(f'The third element is: {arr_1D[2]}.')
# Output: The third element is: 30.

print(f'The fourth element is: {arr_1D[-2]}.')
# Output: The fourth element is: 40.


# -----------------------------
# 2D Array
# -----------------------------
arr_2D = np.array([
    [10, 20, 30, 40], 
    [50, 60, 70, 80]
])

print('\n2D Array:') 
# Output: 2D Array:
print(arr_2D)
# Output:
# [[10 20 30 40]
#  [50 60 70 80]]

print(f'Element at row 0, column 1 is: {arr_2D[0, 1]}.')
# Output: Element at row 0, column 1 is: 20.

print(f'Element at row 1, column 2 is: {arr_2D[1, 2]}.')
# Output: Element at row 1, column 2 is: 70.


# -----------------------------
# Multi-Dimensional (3D) Array
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

print("3D Array:")
# Output: 3D Array:
print(arr_3D)
# Output:
# [[[ 10  20  30]
#   [ 40  50  60]]
#
#  [[ 70  80  90]
#   [100 110 120]]]

print("\nFirst layer:")
# Output: First layer:
print(arr_3D[0])
# Output:
# [[10 20 30]
#  [40 50 60]]

print("\nElement at layer 0, row 1, column 2:")
# Output: Element at layer 0, row 1, column 2:
print(arr_3D[0, 1, 2])
# Output: 60

print("\nSecond layer, first row:")
# Output: Second layer, first row:
print(arr_3D[1, 0])
# Output: [70 80 90]

print("\nLast element using negative indexing:")
# Output: Last element using negative indexing:
print(arr_3D[-1, -1, -1])
# Output: 120
