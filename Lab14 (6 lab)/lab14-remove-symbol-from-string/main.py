words = input()
result = ""

for char in words:
    if char.isalnum():
        result += char
        
if result == "":
    print("empty")
else:
    print(result)
        
        
        