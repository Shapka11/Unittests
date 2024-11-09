import unittest
import math

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

        res = circle.area(52)
        self.assertEqual(res, math.pi * 52 * 52)

    def test_perimetr(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

        res = circle.perimeter(21)
        self.assertEqual(res, math.pi * 2 * 21)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(0, 66)
        self.assertEqual(res, 0)

        res = rectangle.area(12, 21)
        self.assertEqual(res, 252)

        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)

    def test_perimetr(self):
        res = rectangle.perimeter(12, 4)
        self.assertEqual(res, 32)

        res = rectangle.perimeter(21, 21)
        self.assertEqual(res, 84)

        res = rectangle.perimeter(100000, 20000)
        self.assertEqual(res, 240000)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

        res = square.area(15)
        self.assertEqual(res, 225)

    def test_perimetr(self):
        res = square.perimeter(8)
        self.assertEqual(res, 32)

        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_is_square(self):
        self.assertTrue(square.is_square(5, 5, 5, 5))
        self.assertFalse(square.is_square(2, 2, 1, 2))


class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(8, 10)
        self.assertEqual(res, 40)

        res = triangle.area(3, 9)
        self.assertEqual(res, 27 / 2)

    def test_perimetr(self):
        res = triangle.perimeter(1, 2, 3)
        self.assertEqual(res, 6)

        res = triangle.perimeter(11, 123, 45)
        self.assertEqual(res, 179)

    def test_is_equilateral(self):
        self.assertTrue(triangle.is_equilateral(6, 6, 6))
        self.assertFalse(triangle.is_equilateral(12, 12, 21))

    def test_is_isosceles(self):
        self.assertTrue(triangle.is_isosceles(6, 9, 6))
        self.assertFalse(triangle.is_isosceles(12, 122, 21))


if __name__ == '__main__':
    unittest.main()
