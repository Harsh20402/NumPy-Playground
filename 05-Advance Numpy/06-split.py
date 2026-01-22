import numpy as np 

# split() is used to divide an array into multiple sub-arrays.
# Syntax: np.split(array, number_of_splits, axis=0)

# -----------------------------
# 1D Array
# -----------------------------
arr_1D = np.array([10, 20, 30, 40, 50, 60])

print(f'Original 1D Array: {arr_1D}')
# Output: Original 1D Array: [10 20 30 40 50 60]


print(f'\nSplit array into 3 equal parts using split(): {np.split(arr_1D, 3)}')
# Output: [array([10, 20]), array([30, 40]), array([50, 60])]

print(f'\nSplit array into 3 parts using hsplit(): {np.hsplit(arr_1D, 3)}')
# Output: [array([10, 20]), array([30, 40]), array([50, 60])]

# ❌ vsplit does NOT work for 1D arrays
# print(np.vsplit(arr_1D, 3))  → Error


# -----------------------------
# 2D Array
# -----------------------------
arr_2D = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

print(f'\nOriginal 2D Array:\n{arr_2D}')
# Output:
# [[10 20]
#  [30 40]
#  [50 60]
#  [70 80]]


print(f'\nVertical split into 2 parts using vsplit():\n{np.vsplit(arr_2D, 2)}')
# Output:
# [array([[10, 20],
#         [30, 40]]),
#  array([[50, 60],
#         [70, 80]])]


print(f'\nHorizontal split into 2 parts using hsplit():\n{np.hsplit(arr_2D, 2)}')
# Output:
# [array([[10],
#         [30],
#         [50],
#         [70]]),
#  array([[20],
#         [40],
#         [60],
#         [80]])]
