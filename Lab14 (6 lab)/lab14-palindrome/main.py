words = input().lower()

clean_words = ""

for char in words:
    if char.isalnum():
        clean_words = clean_words + char

reverse_words = clean_words[::-1]

if clean_words == reverse_words:
    print("palindrome")
else:
    print("not palindrome")