""""  This assignment is about classifying triangle

 equilateral triangles have all three sides with the same length
 isosceles triangles have two sides with the same length
 scalene triangles have three sides with different lengths
 right triangles have three sides with lengths, a, b, and c where a**2 + b**2 = c**2

"""


def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        # print("Test Failed: ThisNotATriangle")
        exit()
    elif a + b + c <= 2 * max(a, b, c):
        # print ("Test failed: ThisNotATriangle")
        exit()
    if a == b and a == c and b == c:
        triangle = "equilateral"
        print(triangle)
    elif a == b or b == c or c == a:
        triangle = "isosceles"
        print(triangle)
    if (a ** 2 + b ** 2 == c ** 2) or (c ** 2 + b ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
        triangle = "right"
        print(triangle)
    elif a != b and a != c and b != c:
        triangle = "scalene"
        print(triangle)
    return triangle


"I desabled below code to authomate the unittest case but you can enable to run to see "
# try:
#    arg1 = input('What is the length of the first side ?\n')
#    arg2 = input('What is the length of the second side ?\n')
#    arg3 = input('What is the length of the third side?\n')
# except: print(" This is Not a triangle ")

# if ((not type(arg1) is int) or (not type(arg2) is int) or (not type(arg3) is int)):
# print("NotATriangleNot")
# exit()
# classify_triangle(int(arg1), int(arg2), int(arg3))

