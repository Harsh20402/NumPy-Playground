prices = [100, 200, 300]

after_price_discount = []

discount_ammount = 5

for price in prices:
  after_discount = price - ((price / 100) * discount_ammount) 
  after_price_discount.append(after_discount) 
  
  
print(after_price_discount)