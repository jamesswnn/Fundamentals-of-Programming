'''
lab11-capitalize-the-first-letter
'''

# YOUR CODE HERE

def capitialize(text) :
    return text[0].upper() + text[1:]

text_input = input()
print(capitialize(text_input))