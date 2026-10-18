'''
lab03-bubble-tea-order
'''

# YOUR CODE HERE
member = str(input())
size = str(input())
topping = str(input())

pay = 0

if size == 'M':
    pay += 50
    if topping == 'N' :
        pay -= 10
    else :
        pay += 0
else:
    pay += 60
    if topping == 'N' :
        pay -= 10
    else :
        pay += 0 


if member == 'Y':
    total = pay - ((pay / 100 ) * 10 )
else :
    total = pay - 0

print("Total price:" , str(float(total)))