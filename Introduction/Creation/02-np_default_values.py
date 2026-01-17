import numpy as np

# -------------------------------
# Creating NumPy arrays using default values (zeros)
# -------------------------------

zeros_array = np.zeros(3)
print(f"\n1D Zeros Array (3 elements):\n{zeros_array}")
# Output: 1D Zeros Array (3 elements):
# [0. 0. 0.]

zeros_array = np.zeros((3, 3, 3))
print(f"\n3D Zeros Array (3 x 3 x 3):\n{zeros_array}")
# Output:
# 3D Zeros Array (3 x 3 x 3):
# [[[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
#
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
#
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]]

zeros_array = np.zeros((3, 2))
print(f"\n2D Zeros Array (3 rows x 2 columns):\n{zeros_array}")
# Output:
# 2D Zeros Array (3 rows x 2 columns):
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]


# -------------------------------
# Creating NumPy arrays using default values (ones)
# -------------------------------

ones_array = np.ones(3)
print(f"\n1D Ones Array (3 elements):\n{ones_array}")
# Output: 1D Ones Array (3 elements):
# [1. 1. 1.]

ones_array = np.ones((3, 3, 3))
print(f"\n3D Ones Array (3 x 3 x 3):\n{ones_array}")
# Output:
# 3D Ones Array (3 x 3 x 3):
# [[[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]
#
#  [[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]
#
#  [[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]]

ones_array = np.ones((3, 2))
print(f"\n2D Ones Array (3 rows x 2 columns):\n{ones_array}")
# Output:
# 2D Ones Array (3 rows x 2 columns):
# [[1. 1.]
#  [1. 1.]
#  [1. 1.]]


# -------------------------------
# Creating NumPy arrays using specific values
# -------------------------------

special_array = np.full(3, 2)
print(f"\n1D Full Array (3 elements filled with 2):\n{special_array}")
# Output: 1D Full Array (3 elements filled with 2):
# [2 2 2]

special_array = np.full((3, 3, 3), 3)
print(f"\n3D Full Array (3 x 3 x 3 filled with 3):\n{special_array}")
# Output:
# 3D Full Array (3 x 3 x 3 filled with 3):
# [[[3 3 3]
#   [3 3 3]
#   [3 3 3]]
#
#  [[3 3 3]
#   [3 3 3]
#   [3 3 3]]
#
#  [[3 3 3]
#   [3 3 3]
#   [3 3 3]]]

special_array = np.full((3, 2), 4)
print(f"\n2D Full Array (3 rows x 2 columns filled with 4):\n{special_array}")
# Output:
# 2D Full Array (3 rows x 2 columns filled with 4):
# [[4 4]
#  [4 4]
#  [4 4]]
