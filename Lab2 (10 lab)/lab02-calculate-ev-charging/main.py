'''
lab02-calculate-ev-charging
'''

# YOUR CODE HERE
capacity = float(input())
charge_rate = float(input())
charge_fee = 4.5

hours = capacity / charge_rate
price = capacity * charge_fee

print(round(hours, 2))
print(round(price, 2))
