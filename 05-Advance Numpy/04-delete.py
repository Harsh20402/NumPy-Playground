import numpy as np 

# delete() is used to remove elements from a NumPy array at a specified index.
# Sysntax: np.delete(array, index, axis=None)

arr_1D = np.array([10, 20, 30, 40, 50])

print(f'Original 1D Array: {arr_1D}')
# Output: Original 1D Array: [10 20 30 40 50]

print(f'\nDelete element at index 2: {np.delete(arr_1D, 2)}')
# Output: Delete element at index 2: [10 20 40 50]

print(f'\nDelete multiple elements at index [1, 3]: {np.delete(arr_1D, [1, 3])}')
# Output: Delete multiple elements at index [1, 3]: [10 30 50]

arr_2D = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(f'\nOriginal 2D Array:\n{arr_2D}')
# Output: Original 2D Array:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

# Delete from 2D Array (Row-wise)
print(f'\nDelete row at index 1:\n{np.delete(arr_2D, 1, axis=0)}')
# Output: Delete row at index 1:
# [[10 20 30]
#  [70 80 90]]

# Delete from 2D Array (Column-wise)
print(f'\nDelete column at index 0:\n{np.delete(arr_2D, 0, axis=1)}')
# Output: Delete column at index 0:
# [[20 30]
#  [50 60]
#  [80 90]]