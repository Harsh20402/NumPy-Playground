import numpy as np 

# Vectorization means performing operations on entire arrays at once instead of using Python loops. NumPy uses optimized C code, making vectorized operations faster, cleaner, and more efficient.

arr = np.array([1, 2, 3, 4, 5])

result = []
for i in arr:
    result.append(i * 2)

print('Result using loop:')
print(result)
# Output: [2, 4, 6, 8, 10]
