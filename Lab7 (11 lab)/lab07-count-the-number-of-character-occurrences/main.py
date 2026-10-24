'''
lab07-count-the-number-of-character-occurrences

'''
# YOUR CODE HERE
x = []

while True:
    input_list = input()
    if input_list == "-1":
        break
    else:
        x.append(input_list)

x.sort()
char = ""
for elem in x:
    if elem != char:
        char = elem

        total = 0
        for i in x:
            if  i == elem:
                total += 1
        
        print(f"{char}={total}", end=" ")
print()



