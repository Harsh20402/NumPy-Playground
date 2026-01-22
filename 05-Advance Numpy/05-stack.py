import numpy as np 

# Stacking is used to join arrays along a new axis. 

     # Types of Stack
# Function	      Description
# stack()	     Stack along a new axis
# hstack()	   Horizontal stacking (columns)
# vstack()	   Vertical stacking (rows)
# dstack()	   Depth stacking (3rd axis)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# np.stack()
print(f'Stack along axis=0: {np.stack((a, b), axis=0)}')
# Output: Stack along axis=0: [[1 2 3]
#  [4 5 6]]

print(f'\nStack along axis=1: {np.stack((a, b), axis=1)}')
# Output: Stack along axis=1: [[1 4]
#  [2 5]
#  [3 6]]

# np.hstack() (Horizontal Stack)
print(f'\nHorizontal Stack: {np.hstack((a, b))}')
# Output: Horizontal Stack: [1 2 3 4 5 6]

# np.vstack() (Vertical Stack)
print(f'\nVertical Stack: {np.vstack((a, b))}')
# Output: Vertical Stack: [[1 2 3]
#  [4 5 6]]

# np.dstack() (Depth Stack)
print(f'\nDepth Stack: {np.dstack((a,b))}')
# Output: Depth Stack: [[[1 4]
  # [2 5]
  # [3 6]]]