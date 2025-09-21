from typing import List, Union

temperatures: List[Union[float, int]] = [32.2, 34.6, 43.2, 39.0, 37.5]

total: Union[float, int] = 0

for temp in temperatures:
    total += temp
    
avg_temp: Union[float, int] = total / len(temperatures)

print(f"The average temperature is {avg_temp}.") 