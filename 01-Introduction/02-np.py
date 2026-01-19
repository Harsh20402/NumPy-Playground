import numpy as np  # Import NumPy library for numerical operations

def temp_avg():
    # Create a NumPy array of temperatures
    tempreatures = np.array([32.6, 29.0, 18.7, 10.3, 42.4])

    # Calculate the average temperature using NumPy
    average_temp = np.mean(tempreatures)
    
    # Return the calculated average temperature
    return average_temp


if __name__ == "__main__":
    # Call the function and print the average temperature
    # The value is rounded to 1 decimal place
    print(f'The average tempreature is {round(temp_avg(), 1)}.')
