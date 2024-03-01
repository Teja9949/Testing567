def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    
    if a <= 0 or b <= 0 or c <= 0:  # Corrected 'b <= b' to 'b <= 0'
        return 'InvalidInput'
    
    # Verify that all 3 inputs are integers  
    # Python's "isinstance(object,type)" returns True if the object is of the specified type
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
      
    # The sum of any two sides must be strictly greater than the third side
    # for the specified shape to be a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):  # Corrected the conditions
        return 'NotATriangle'
        
    # Now we know that we have a valid triangle 
    if a == b == c:
        return 'Equilateral'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:  # Changed the condition
        return 'Right'
    elif a != b and b != c and a != c:  # Corrected 'a != b' instead of 'a != b' in the condition
        return 'Scalene'
    else:
        return 'Isosceles'  # Corrected 'Isoceles' to 'Isosceles'
