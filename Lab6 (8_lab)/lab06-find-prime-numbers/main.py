'''
lab06-find-prime-numbers
'''
total = 0

while True:
    n = int(input())
    if 1 < n < 1000:
        break

for i in range(2, n + 1):
    count = 0
    
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1 
            
    if count == 1:
        print(i, end=" ")
        total += 1

print()
print(f"Total prime numbers: {total}")