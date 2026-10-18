'''
lab05-average-score
'''

# YOUR CODE HERE
total_score = 0
count = 0

while True:
    user_score = input()

    if user_score == "q":
        break

    user_score = int(user_score)

    if user_score > 0 and user_score <= 100:
        total_score += user_score
        count += 1

avg = total_score / count
avg = round(avg, 2)

if avg >= 50:
    print(f"{avg} Satisfactory")
else:
    print(f"{avg} Unsatisfactory")
