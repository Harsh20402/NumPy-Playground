import numpy as np

# -----------------------------
# Create 2D Array
# -----------------------------
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Array:")
# Output: Array:
print(arr)
# Output:
# [[10 20 30]
#  [40 50 60]]


# -----------------------------
# Sum: np.sum() || Adds all elements in the array (10+20+30+40+50+60 = 210)
# -----------------------------
print("\nSum of all elements:")
# Output: Sum of all elements:
print(np.sum(arr))
# Output: 210


# ----------------------------- 
# Mean (Average): np.mean() || Calculates average value (Mean = 210 / 6 = 35)
# -----------------------------
print("\nMean of all elements:")
# Output: Mean of all elements:
print(np.mean(arr))
# Output: 35.0


# -----------------------------
# Minimum: || np.min()Returns smallest value
# -----------------------------
print("\nMinimum value:")
# Output: Minimum value:
print(np.min(arr))
# Output: 10


# -----------------------------
# Maximum: np.max() || Returns largest value
# -----------------------------
print("\nMaximum value:")
# Output: Maximum value:
print(np.max(arr))
# Output: 60


# -----------------------------
# Standard Deviation: np.std() || Measures how much values vary from the mean
# -----------------------------
print("\nStandard Deviation:")
# Output: Standard Deviation:
print(np.std(arr))
# Output: 17.078...


# -----------------------------
# Variance: np.var() || Square of standard deviation
# -----------------------------
print("\nVariance:")
# Output: Variance:
print(np.var(arr))
# Output: 291.666...



# -----------------------------
# Aggregation Using Axis
# -----------------------------

print("\nColumn-wise sum:")
# Output: Column-wise sum:  axis=0 → column-wise operation
print(np.sum(arr, axis=0))
# Output: [50 70 90]

print("\nRow-wise sum:")
# Output: Row-wise sum:  axis=1 → row-wise operation
print(np.sum(arr, axis=1))  
# Output: [ 60 150]
