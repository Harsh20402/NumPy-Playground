# -------------------------------
# Using Separate Variables
# -------------------------------

# Individual marks stored in separate variables
mark_01 = 76
mark_02 = 89
mark_03 = 65
mark_04 = 85
mark_05 = 92

# Manual calculation of total and average
total = mark_01 + mark_02 + mark_03 + mark_04 + mark_05
average = total / 5

# Display results
print("Separate Variables")
print(f"Total: {total}")
print(f"Average: {average}")


# -------------------------------
# Using NumPy Array
# -------------------------------

# Import NumPy library
import numpy as np

# Store all marks in a NumPy array
marks = np.array([76, 89, 65, 85, 92])

# Calculate total and average using NumPy functions
total = np.sum(marks)
average = np.mean(marks)

# Display results
print("\nNumPy Array")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average}")
