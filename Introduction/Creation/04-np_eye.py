# Create Identity Matrix using NumPy
# Function: np.eye(n) → creates n x n identity matrix
import numpy as np

# 3x3 Identity Matrix
identity_matrix = np.eye(3)
print("3x3 Identity Matrix:")
print(identity_matrix)
# Output:
# 3x3 Identity Matrix:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 5x5 Identity Matrix
identity_matrix5 = np.eye(5)
print("\n5x5 Identity Matrix:")
print(identity_matrix5)
# Output:
# 5x5 Identity Matrix:
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
