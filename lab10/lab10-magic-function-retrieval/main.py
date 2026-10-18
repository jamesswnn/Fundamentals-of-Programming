'''
lab10-magic-function-retrieval
'''

# YOUR CODE HERE

num1 = int(input())
magic_results = dict()

# magic_function
for i in range(num1):
    x = round(float(input()), 2)
    y = round(float(input()), 2)
    result = round(float(input()), 2)

    magic_results[(x, y)] = result

num2 = int(input())

for j in range(num2):
    x = round(float(input()), 2)
    y = round(float(input()), 2)
    z = round(float(input()), 2)

    position = (x, y)

    if position not in magic_results:
        print("Magic Required!!")
    elif magic_results[position] == z:
        print("Correct")
    elif magic_results[position] != z:
        print("Incorrect")