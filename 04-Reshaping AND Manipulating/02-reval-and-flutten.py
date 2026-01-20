import numpy as np 

# flatten() returns a copy of the array, while ravel() returns a view whenever possible.

import numpy as np

arr_2D = np.array([[10, 20, 30],
                   [40, 50, 60]])

print('Original Array:')
print(arr_2D)
# Output:
# [[10 20 30]
#  [40 50 60]]

# Using flatten()
arr_flat = arr_2D.flatten()
print('Using flatten():', arr_flat)
# Output: [10 20 30 40 50 60]

# Using ravel()
arr_ravel = arr_2D.ravel()
print('Using ravel():', arr_ravel)
# Output: [10 20 30 40 50 60]

# Check if they are views or copies
arr_ravel[0] = 999
print('Modified ravel():', arr_ravel)
# Output: [999  20  30  40  50  60]
print('Original Array after ravel modification:', arr_2D)
# Output: [[999  20  30]
#          [ 40  50  60]]

arr_flat[0] = 111
print('Modified flatten():', arr_flat)
# Output: [111  20  30  40  50  60]
print('Original Array after flatten modification:', arr_2D)
# Output: [[999  20  30]
#          [ 40  50  60]]
