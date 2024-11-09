def area(a):
    """Принимает число a(сторона квадрата), возвращает площадь квадрата"""
    return a * a


def perimeter(a):
    """Принимает число a(сторона квадрата), возвращает периметр квадрата"""
    return 4 * a


def is_square(a, b, c, d):
    """Принимает числа a, b, c, d(стороны прямоугольника), возвращает true, если это квадрат"""
    return a == b == c == d
