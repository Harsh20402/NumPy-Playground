import numpy as np               # Import NumPy for numerical operations
from typing import Union         # For type hinting (float or int return type)

# Class to calculate average temperature
class Temperature:
    @staticmethod                # Decorator → means we don’t need to create an object to call this method
    def temp() -> float:         # Function returns a float value
        # Define a NumPy array of temperatures
        temperatures = np.array([32.2, 34.6, 43.2, 39.0, 37.5])
        
        # Calculate and return the average temperature using NumPy's mean() function
        return np.mean(temperatures)

# Entry point of the program
if __name__ == "__main__":
    # Call the static method directly without creating an instance
    temp_avg: Union[float, int] = Temperature.temp()
    
    # Print the result formatted to 2 decimal places
    print(f"The average temperature is {temp_avg:.2f}.")
