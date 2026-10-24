'''
lab11-list-manipulation
'''

# YOUR CODE HERE

def list_manipulation(A_list, command, location, value):
    if command == 'remove' and location == 'end':
        A_list.pop()
    elif command == 'remove' and location == 'beginning':
        A_list.pop(0)
    elif command == 'add' and location == 'end':
        A_list.append(value)
    elif command == 'add' and location == 'beginning':
        A_list.insert(0, value)
    
    return A_list
 
A_list = []
for i in range(3):
    A_input = input()
    A_list.append(A_input)

command = input()
location = input()
value = input()

print(list_manipulation(A_list, command, location, value))
