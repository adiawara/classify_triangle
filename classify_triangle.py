" this assignment is about classifying triangle"

# equilateral triangles have all three sides with the same length
# isosceles triangles have two sides with the same length
# scalene triangles have three sides with different lengths
# right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2

def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        #print("ThisNotATriangle")
        exit()
    elif a + b + c <= 2 * max(a, b, c):
        #print ("ThisNotATriangle")
        exit()
    if a == b and a == c and b==c:
        print( 'equilateral')   
    elif a == b or b == c or c == a:
        print( 'isosceles')
    if (a**2 +b**2 == c**2) or (c**2 +b**2 == a**2) or (a**2 +c**2 == b**2):
        print ('   right')   
    elif a != b and a != c and b!=c:
        print ('scalene')
    
""" desabled below to because the "main" routine can just invoke classify_triangle()with values.
This approach allows you to easily invoke classify_triangle() from your test framework."""

#try:
    #arg1 = input('What is the length of the first side ?\n')
    #arg2 = input('What is the length of the second side ?\n')
    #arg3 = input('What is the length of the third side?\n')
#except: print(" This is Not a triangle ")
#if  not arg1.isdigit() or not arg2.isdigit() or not arg3.isdigit():
    #print(" Please enter only positve integer")
    #exit()
#arg1=int(arg1)
#arg2=int(arg2)
#arg3=int(arg3)

#if ((not type(arg1) is int) or (not type(arg2) is int) or (not type(arg3) is int)):
    #print("NotATriangleNot")
    #exit()
#classify_triangle(int(arg1), int(arg2), int(arg3))

