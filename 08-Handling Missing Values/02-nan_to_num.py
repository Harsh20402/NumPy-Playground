import numpy as np 

arr = np.array([10, 20, np.nan, 40, np.nan, 60, np.nan])

print(f'Original Array: {arr}')
# Output: Original Array: [10. 20. nan 40. nan 60. nan]


print(f'\nReplace NaN values with default number:')
print(np.nan_to_num(arr))
# Output: [10. 20.  0. 40.  0. 60.  0.]


print(f'\nReplace NaN values using a particular number (99):')
print(np.nan_to_num(arr, nan=99))
# Output: [10. 20. 99. 40. 99. 60. 99.]
