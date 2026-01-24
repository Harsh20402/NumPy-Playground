import numpy as np 

# Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array so that both arrays have compatible shapes—without copying data.

arr = np.array([10, 20, 30, 40])

print(f'Original 1D Array: {arr}') 
# Output: Original 1D Array: [10 20 30 40]

result_arr_1 = arr + 5
print(f'\nArray after adding scalar 5: {result_arr_1}') 
# Output: Array after adding scalar 5: [15 25 35 45] 

arr_2 = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

arr_1D = [10, 20, 30]

print(f'\n2D Array:\n{arr_2}') 
# Output: 2D Array:
# [[1 2 3]
#  [4 5 6]]

print(f'\n1D Array: {arr_1D}') 
# Output: 1D Array: [10, 20, 30]

final_result_2D = arr_2 + arr_1D
print(f'\nResult after Broadcasting:\n{final_result_2D}')
# Output: Result after Broadcasting:
# [[11 22 33]
#  [14 25 36]]

arr_3 = np.array([
  [1, 2, 3],
  [4, 5, 6]
])

arr_1D_col = np.array([
  [10], [20]
])

print(f'\n2D Array:\n{arr_3}') 
# Output: 2D Array:
# [[1 2 3]
#  [4 5 6]]

print(f'\n1D Array: {arr_1D_col}') 
# Output: 1D Array: [[10]
#  [20]]

final_result_2D_col = arr_3 + arr_1D_col 
print(f'\nResult after Broadcasting: {final_result_2D_col}')
# Output: Result after Broadcasting: [[11 12 13]
#  [24 25 26]]

# a = np.array([1, 2, 3])
# b = np.array([10, 20])

# print(a + b)
# ValueError: operands could not be broadcast together