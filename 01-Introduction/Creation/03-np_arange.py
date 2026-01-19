import numpy as np
# Purpose: Create sequences with a fixed step
# Syntax: np.arange(start, stop, step)

# Sequence from 0 to 9
seq_1 = np.arange(10)
print(f"Sequence 0 to 9: {seq_1}")
# Output: Sequence 0 to 9: [0 1 2 3 4 5 6 7 8 9]

# Sequence from 5 to 15
seq2 = np.arange(5, 16)
print(f"\nSequence 5 to 15: {seq2}")
# Output: Sequence 5 to 15: [ 5  6  7  8  9 10 11 12 13 14 15]

# Sequence from 0 to 20 with step 4
seq3 = np.arange(0, 21, 4)
print(f"\nSequence 0 to 20 with step 4: {seq3}")
# Output: Sequence 0 to 20 with step 4: [ 0  4  8 12 16 20]