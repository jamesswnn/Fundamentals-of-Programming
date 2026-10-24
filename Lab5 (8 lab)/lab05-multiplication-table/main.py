'''
lab05-multiplication-table
'''

# YOUR CODE HERE
x = int(input())  # สูตรคูณแม่
y = int(input())  # จำนวนตาราง
i = 1

if y <= 0:
    print("Unable to create a table")
else:
    while i <= y:
        print(f"{x}*{i}={x*i}")
        i += 1
