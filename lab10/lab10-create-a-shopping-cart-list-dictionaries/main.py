'''
lab10-create-a-shopping-cart-list-of-dictionaries
'''

n = int(input())
shopping_list = []

for i in range(n):
    name = str(input())
    quantity = int(input())
    price = float(input())

    dictionary = {
        'name' : name,
        'quantity' : quantity,
        'price' : price
    }

    shopping_list.append(dictionary)

sum = 0
for result in shopping_list :
    sum += result['quantity'] * result['price']

print(shopping_list)
print(round(sum, 1))
