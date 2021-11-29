"""
This code
 -*- coding: utf-8 -*-
"""
def classify_triangle(height, base, hypt):
    """
    Your correct code goes here...
    Fix the faulty logic below until the code passes all of
    you test cases. This function returns a string with the
    type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
    If all three sides are equal, return 'Equilateral'
    If exactly one pair of sides are equal, return 'Isoceles'
    If no pair of  sides are equal, return 'Scalene'
    If not a valid triangle, then return 'NotATriangle'
    If the sum of any two sides equals the squate of the third side,
    then return 'Right'
    BEWARE: there may be a bug or two in this code
    """
    # simplification
    x_x = height ** 2
    y_y = base ** 2
    z_z = hypt ** 2
    # require that the input values be >= 0 and <= 200
    if height > 200 or base > 200 or hypt > 200:
        response = "InvalidInput"
    if height <= 0 or base <= 0 or hypt <= 0:
        response = "InvalidInput"
    if not (isinstance(height, int) and isinstance(base, int) and isinstance(hypt, int)):
        response = "InvalidInput"
    if (height >= (base + hypt)) or (base >= (height + hypt)) or (hypt >= (height + base)):
        response = "NotATriangle"
    if height == base and base == hypt:
        response = "Equilateral"
    if x_x + y_y == z_z or x_x + z_z == y_y or z_z + y_y == x_x:
        response = "Right"
    if (height != base) and (base != hypt) and (height != hypt):
        response = "Scalene"
    else:
        response = "Isosceles"
    return response
