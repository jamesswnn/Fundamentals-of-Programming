# YOUR CODE GOES HERE

words = input().split()
new_words = []

for text in words:
    if text.endswith('.'):
        word = text[:-1]
    else:
        word = text

    if word.isalpha() and word[0].isupper() and word[1:].islower():
        new_words.append(text)

print(new_words)