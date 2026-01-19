import numpy as np

# -----------------------------
# Create Arrays
# -----------------------------
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 6, 8])

print("Array 1:")
# Output: Array 1:
print(arr1)
# Output: [10 20 30 40]

print("\nArray 2:")
# Output: Array 2:
print(arr2)
# Output: [2 4 6 8]


# -----------------------------
# Addition
# -----------------------------
print("\nAddition:")
# Output: Addition:
print(arr1 + arr2)
# Output: [12 24 36 48]


# -----------------------------
# Subtraction
# -----------------------------
print("\nSubtraction:")
# Output: Subtraction:
print(arr1 - arr2)
# Output: [ 8 16 24 32]


# -----------------------------
# Multiplication
# -----------------------------
print("\nMultiplication:")
# Output: Multiplication:
print(arr1 * arr2)
# Output: [ 20  80 180 320]


# -----------------------------
# Division
# -----------------------------
print("\nDivision:")
# Output: Division:
print(arr1 / arr2)
# Output: [5. 5. 5. 5.]


# -----------------------------
# Power
# -----------------------------
print("\nPower:")
# Output: Power:
print(arr1 ** 2)
# Output: [ 100  400  900 1600]


# -----------------------------
# Modulus
# -----------------------------
print("\nModulus:")
# Output: Modulus:
print(arr1 % arr2)
# Output: [0 0 0 0]


arr = np.array([1, 4, 9, 16])

print("Square root:")
# Output: Square root:
print(np.sqrt(arr))
# Output: [1. 2. 3. 4.]