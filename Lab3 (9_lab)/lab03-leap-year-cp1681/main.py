'''
lab03-vector-angle-cp1681
'''

# YOUR CODE GOES HERE
year_count = int(input())

if (year_count % 4 == 0 and year_count % 100 != 0) or year_count % 400 == 0 :
    print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")

if year_count % 10 == 0:
    print("NEW DECADE")