'''
/**
USERID: 6987012
PASSWORD: 9bd0a2
EXERCISEID: itds120-lab07-competition-cp2681
 */
'''

# YOUR CODE GOES HERE
'''itds120-lab07-competition-cp2681'''
balloon = []

while True:
    balloon_input = input()
    if balloon_input == "-1":
        break
    else:
        balloon.append(int(balloon_input))

balloon.sort()

print("-", balloon[-3])
print("-", balloon[-2])
print("-", balloon[-1])



