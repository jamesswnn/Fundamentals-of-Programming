'''
lab02-hours-and-minutes
'''

# YOUR CODE HERE
minutes_count = int(input())

hours = minutes_count // 60
minutes = minutes_count % 60

print(str(hours) + ":" + str(minutes))
