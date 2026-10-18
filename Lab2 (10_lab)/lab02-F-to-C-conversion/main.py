'''
lab02-F-to-C-conversion
'''

# YOUR CODE HERE
F = round(float(input()), 2)

C = round(((F - 32) / 9) * 5, 2)

print(str(F) + "F is equal to " + str(C) + "C")
