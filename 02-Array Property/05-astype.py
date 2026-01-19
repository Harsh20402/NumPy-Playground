import numpy as np

# -----------------------------
# 1D Array
# -----------------------------
arr_1d = np.array([1, 2, 3, 4, 5.6, 6, 7, 8.1])

print('1D Array:')
# Output: 1D Array:
print(arr_1d)
# Output: [1.  2.  3.  4.  5.6 6.  7.  8.1]


# -----------------------------
# Convert to Integer
# -----------------------------
arr_1d_int = arr_1d.astype(int)
print(f'Data type changed to {arr_1d_int.dtype} and the result is {arr_1d_int}.')
# Output: Data type changed to int64 and the result is [1 2 3 4 5 6 7 8].


# -----------------------------
# Convert to Float
# -----------------------------
arr_1d_float = arr_1d.astype(float)
print(f'Data type changed to {arr_1d_float.dtype} and the result is {arr_1d_float}.')
# Output: Data type changed to float64 and the result is [1.  2.  3.  4.  5.6 6.  7.  8.1].


# -----------------------------
# Convert to String
# -----------------------------
arr_1d_str = arr_1d.astype(str)
print(f'Data type changed to {arr_1d_str.dtype} and the result is {arr_1d_str}.')
# Output: Data type changed to <U32 and the result is ['1.0' '2.0' '3.0' '4.0' '5.6' '6.0' '7.0' '8.1'].
