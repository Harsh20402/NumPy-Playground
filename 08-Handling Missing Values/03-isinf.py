import numpy as np 

arr = np.array([10, 20, 30, np.inf, 40, 50, -np.inf]) 

print(f'Original Array: {arr}')
# Output: Original Array: [ 10.  20.  30.  inf  40.  50. -inf]


print(f'\nFind the infinite values using isinf(): {np.isinf(arr)}')
# Output:
# [False False False  True False False  True]


print(f'\nFind the total infinite values: {np.isinf(arr).sum()}')
# Output: 2


# -----------------------------
# Replace infinite values
# -----------------------------
cleaned_arr = np.nan_to_num(arr, posinf=99, neginf=10)

print(f'\nAfter cleaning the infinite values: {cleaned_arr}')
# Output: [10. 20. 30. 99. 40. 50. 10.]
