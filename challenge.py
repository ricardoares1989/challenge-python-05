import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return side**2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (diagonal_1 * diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return ((base_major+base_minor) / 2 ) * height


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (perimeter * apothem) / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return math.pi * radius**2


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):
        
        def setUp(self):
            # Initialize the needed values for the tests
            self.sides = [4,8,9]
            self.base_and_height = [[8,4],[6,2],[10,2]]
            self.diagonals = [[5,8],[8,8],[7,20],[20,50]]
            self.trapezoid_properties = [[15,10,3],[7,3,1.5],[22,18,10]]
            self.perimeter_apothem = [[120, 5], [15,1.2], [20,5]]
            self.radius = [8,7,12,15,23]

        def test_square_area(self):
            # Make this test first...
            for value in self.sides:
                self.assertEqual(value**2, square_area(value))

        def test_rectangle_area(self):
            # Make this test first...
            for rectangle in self.base_and_height:
                self.assertEqual(rectangle[0]*rectangle[1], 
                    rectangle_area(rectangle[0],rectangle[1]))
            
        def test_triangle_area(self):
            # Make this test first...
            for triangle in self.base_and_height:
                area = (triangle[0] * triangle[1]) /2
                self.assertEqual(area, triangle_area(triangle[0], triangle[1]))

        def test_rhombus_area(self):
            # Make this test first...
            for rhombus  in self.diagonals:
                area = (rhombus[1] * rhombus[0]) / 2
                self.assertEqual(area, rhombus_area(rhombus[1], rhombus[0]))

        def test_trapezoid_area(self):
            # Make this test first...
            for prop in self.trapezoid_properties:
                area = ((prop[0] + prop[1]) / 2) * prop[2]
                self.assertEqual(area, trapezoid_area(*prop))
            
        def test_regular_polygon_area(self):
            # Make this test first...
            for prop in self.perimeter_apothem:
                area = (prop[1] * prop[0]) / 2
                self.assertEqual(area , regular_polygon_area(*prop))

        def test_circumference_area(self):
            # Make this test first...
            for radius in self.radius:
                area = math.pi * radius**2
                self.assertEqual(area, circumference_area(radius))
        def tearDown(self):
            # Delete the needed values for the tests
            del(self.sides)
            del(self.base_and_height)
            del(self.diagonals)
            del(self.trapezoid_properties)
            del(self.perimeter_apothem)
            del(self.radius)

    unittest.main()
