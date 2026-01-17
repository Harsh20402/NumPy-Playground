def temp_avg():
    # List of temperatures
    tempreatures = [32.6, 29.0, 18.7, 10.3, 42.4]
    
    # Variable to store total temperature
    total_temp = 0
    
    # Loop through each temperature and add to total
    for item in tempreatures:
        total_temp += item
        
    # Calculate average temperature
    avg_temp = total_temp / len(tempreatures)
    
    # Return the average value
    return avg_temp


if __name__ == "__main__":
    # Print the average temperature rounded to 1 decimal place
    print(f'The average tempreature is {round(temp_avg(), 1)}.')
