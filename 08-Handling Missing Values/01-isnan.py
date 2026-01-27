import numpy as np 

# Create an array with missing values (NaN)
arr = np.array([10, 20, np.nan, 40, np.nan, 60, np.nan])

print(f'Original Array: {arr}')
# Output: Original Array: [10. 20. nan 40. nan 60. nan]


# -----------------------------
# Checking Missing Values
# -----------------------------
print(f'\nChecking missing values using isnan(): {np.isnan(arr)}')
# Output: [False False  True False  True False  True]

print(f'\nCount the missing values: {np.isnan(arr).sum()}')
# Output: Count the missing values: 3


# -----------------------------
# Removing Missing Values
# -----------------------------
clean_arr = arr[~np.isnan(arr)]

print('\nArray after removing missing values:')
print(clean_arr)
# Output: [10. 20. 40. 60.]
