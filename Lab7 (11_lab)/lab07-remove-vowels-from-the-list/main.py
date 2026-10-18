'''
lab07-remove-vowels-from-the-list
'''
# YOUR CODE HERE
list_A = []
while True:
    vowel_input = input()
    if vowel_input == '0':
        break
    else:
        list_A.append(vowel_input)

i = 0
while i < len(list_A):
    if list_A[i] == 'a' or list_A[i] == 'e' or list_A[i] == 'i' or list_A[i] == 'o' or list_A[i] == 'u':
        del list_A[i]
    else:
        i += 1

print(list_A)


