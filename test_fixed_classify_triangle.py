'''  triangle classification '''
import unittest            #this makes python unittest available
import fixed_classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    ''' test cases for triangle classificaton  '''
    def test_equilateral_if_all_three_sides_are_equal(self):
        '''  equilateral triangle test'''
        try:
            self.assertEqual('equilateral', fixed_classify_triangle.classify_triangle(1, 1, 1))
            self.assertEqual('equilateral', fixed_classify_triangle.classify_triangle(11, 11, 11))
        except ValueError:
            print("Test failed")

    def test_isosceles_if_exactly_one_pair_of_sides_equal(self):
        '''  Isosceles triangle test'''
        try:
            self.assertEqual('isosceles', fixed_classify_triangle.classify_triangle(4, 5, 5))
            self.assertEqual('isosceles', fixed_classify_triangle.classify_triangle(5, 6, 5))
            self.assertEqual('isosceles', fixed_classify_triangle.classify_triangle(5, 5, 7))
            self.assertEqual('isosceles', fixed_classify_triangle.classify_triangle(11, 11, 8))
        except ValueError:
            print("Test failed")

    def test_scalene_if_no_pair_of_sides_are_equal(self):
        ''' Scalene triangle test'''
        try:
            self.assertEqual('scalene', fixed_classify_triangle.classify_triangle(7, 8, 9))
            self.assertEqual('scalene', fixed_classify_triangle.classify_triangle(4, 5, 6))
            self.assertEqual('scalene', fixed_classify_triangle.classify_triangle(17, 18, 19))
        except ValueError:
            print("Test failed")

    def test_right_if_sum_of_square_of_two_sides_equal_the_square_of_third_side(self):
        '''  right triangle test'''
        try:
            self.assertEqual('right', fixed_classify_triangle.classify_triangle(3, 4, 5))
            self.assertEqual('right', fixed_classify_triangle.classify_triangle(6, 8, 10))
            self.assertEqual('right', fixed_classify_triangle.classify_triangle(9, 12, 15))
        except ValueError:
            print("Test failed")
    def test_illegal_triangles_throw_exceptions_1(self):
        '''  illegal triangle test '''
        try:
            self.assertEqual('NotATriangle', fixed_classify_triangle.classify_triangle(-1, - 1, -1))
        except ValueError:
            print("Test failed")
    def test_illegal_triangles_throw_exceptions_2(self):
        '''  illegal triangle test '''
        try:
            self.assertEqual('NotATriangle', fixed_classify_triangle.classify_triangle(0, 0, 0))
        except ValueError:
            print("Test failed")
    def test_illegal_triangles_throw_exceptions_3(self):
        '''  illegal triangle test '''
        try:
            self.assertEqual('NotATriangle', fixed_classify_triangle.classify_triangle(8, 6, -10))
        except ValueError:
            print("Test failed")
    def test_illegal_triangles_throw_exceptions_4(self):
        '''  illegal triangle test '''
        try:
            self.assertEqual('NotATriangle', fixed_classify_triangle.classify_triangle(9, 2, 5))
        except ValueError:
            print("Test failed")

if __name__ == '__main__':
    unittest.main(exit=False)

#fixed_classify_triangle.classify_triangle(2, 3, 4)
#test_fixed_classify_triangle.test_equilateral_triangles_have_equal_sides
