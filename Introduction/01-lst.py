from typing import List, Union   # Import typing for type hints

# Function to calculate and print average temperature
def temp_avg() -> float:
    # List of temperatures (can contain floats or ints)
    temperatures: List[Union[float, int]] = [32.2, 34.6, 43.2, 39.0, 37.5]

    # Variable to hold the running total
    total: Union[float, int] = 0

    # Loop through each temperature and add to total
    for temp in temperatures:
        total += temp
        
    # Calculate average (sum of all values ÷ number of values)
    avg_temp: Union[float, int] = total / len(temperatures)

    # Print the result
    print(f"The average temperature is {avg_temp}.")

# Run only if this file is executed directly
if __name__ == "__main__":
    temp_avg()
