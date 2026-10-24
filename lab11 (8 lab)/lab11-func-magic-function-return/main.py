'''
lab11-func-magic-function-return
'''
import math

num1 = int(input())
magic_results = dict()


def magic_function(x1, y1):
    x_d = (x1 * 0.0174) - 0.2400
    y_d = (y1 * 0.0174) - 1.7456

    D = round(12742 * math.asin(math.sqrt(
        math.sin(x_d / 2) ** 2
        + math.cos(0.24) * math.cos(x1 * 0.0174)
        * math.sin(y_d / 2) ** 2
    )), 2)

    return D


for i in range(num1):
    x1 = round(float(input()), 2)
    y1 = round(float(input()), 2)
    result = round(float(input()), 2)

    magic_results[(x1, y1)] = result

num2 = int(input())

for j in range(num2):
    x = round(float(input()), 2)
    y = round(float(input()), 2)
    z = round(float(input()), 2)

    position = (x, y)

    if position in magic_results:
        if magic_results[position] == z:
            print("Precisely")
        else:  # magic_results[position] == z:
            difference = round(magic_results[position] - z, 2)
            print(f"Diff by: {difference}")
    else:
        result = magic_function(x, y)
        print(f"New target {result} km away")
        magic_results[position] = result
