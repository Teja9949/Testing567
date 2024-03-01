import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle1(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangle2(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangle3(self): 
        self.assertEqual(classifyTriangle(8,6,10),'Right','9,10,11 is a Right triangle')
    
    def testRightTriangle4(self): 
        self.assertNotEqual(classifyTriangle(21,6,10),'Right','7,8,9 is a Not Right triangle')
    
    #Testing Equilateral Triangles
    def testEquilateralTriangle1(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangle2(self): 
        self.assertEqual(classifyTriangle(30,30,30),'Equilateral','30,30,30 should be equilateral')

    def testEquilateralTriangle3(self): 
        self.assertEqual(classifyTriangle(16,16,16),'Equilateral','16,16,16 should be equilateral')

    def testEquilateralTriangle4(self): 
        self.assertNotEqual(classifyTriangle(10,1,10),'Equilateral','10,1,10 should not be equilateral')
    
    #Testing Scalene Triangles
    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(9,8, 11), 'Scalene')

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(7, 6, 5), 'Scalene')

    def testScaleneTriangle3(self):
        self.assertEqual(classifyTriangle(100, 110, 112), 'Scalene')

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(2, 25, 1), 'Scalene')
   
    # Testing Isosceles Triangles
    def testIsoscelesTriangle1(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles')

    def testIsoscelesTriangle2(self):
        self.assertEqual(classifyTriangle(4, 6, 6), 'Isosceles')

    def testIsoscelesTriangle3(self):
        self.assertEqual(classifyTriangle(8, 8, 7), 'Isosceles')

    def testIsoscelesTriangle4(self):
        self.assertEqual(classifyTriangle(6, 6, 4), 'Isosceles')

    # Testing Not a Triangle

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(2, 2, 8), 'NotATriangle')
    
    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(12, 19, 5), 'NotATriangle')
    
    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(19, 1, 5), 'NotATriangle')

    def testNotATriangle4(self):
        self.assertEqual(classifyTriangle(15, 1, 9), 'NotATriangle')
if __name__ == '__main__':

    print('Running unit tests')
    unittest.main()