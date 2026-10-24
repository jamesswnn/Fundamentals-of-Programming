'''
lab03-vector-angle-cp1681
'''

# YOUR CODE GOES HERE
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

v1 = (x2 - x1, y2 - y1)  # (a, b)
v2 = (x3 - x1, y3 - y1)  # (c, d)

# Dot Product
dot_product = v1[0] * v2[0] + v1[1] * v2[1]
# Length of Vector
length_v1 = (v1[0]**2 + v1[1]**2)**0.5
length_v2 = (v2[0]**2 + v2[1]**2)**0.5
# Cosine of Angle
cosine_angle = dot_product / (length_v1 * length_v2)

if cosine_angle > 0:
    print(round(cosine_angle, 2))
    print("ACUTE")
elif cosine_angle == 0:
    print(round(cosine_angle, 2))
    print("RIGHT")
else:
    print(round(cosine_angle, 2))
    print("OBTUSE")
