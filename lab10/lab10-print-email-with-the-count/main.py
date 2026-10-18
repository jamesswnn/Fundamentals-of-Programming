'''
lab10-print-email-with-the-count
'''

n = int(input())
mail_dict = dict()

for i in range(n):
    email = input()
    count = int(input())

    mail_dict[email] = count

num = 0

for email, count in mail_dict.items():
    if count % 2 == 0:
        print(f"{email}")
        num += 1

if num == 0:
    print("Not Found")
