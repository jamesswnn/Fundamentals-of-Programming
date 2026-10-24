'''
lab07-move-0s-to-the-end-of-the-list
'''
# YOUR CODE HERE
num = []
while True:
    if len(num) == 10:
        break
    else:
        input_num = int(input())
        num.append(input_num)

zero_count = num.count(0)
i = 0

while i < zero_count:
    num.remove(0)
    num.append(0)
    i += 1

print(num)


