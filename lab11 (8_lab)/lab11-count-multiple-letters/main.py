'''
lab11-count-multiple-letters
'''

# YOUR CODE HERE

def multiple_letter_count(text):
    text.strip()
    letters_dict = dict()

    for letter in text:
        letters_dict[letter] = text.count(letter)

    return letters_dict


text = str(input())
print(multiple_letter_count(text))
