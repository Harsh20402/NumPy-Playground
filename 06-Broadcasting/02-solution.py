import numpy as np 

prices = np.array([100, 200, 300])
discount_amount = 5 

final_price = prices - ((prices / 100) * discount_amount) 

print(final_price)