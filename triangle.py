def area(a, h):
    """Принимает числа a и h(сторона и высота треугольника), возвращщает площадь треугольника"""
    return a * h / 2 


def perimeter(a, b, c):
    """Принимает числа a, b, c(стороны треугольника), возвращщает периметр треугольника"""
    return a + b + c


def is_equilateral(a, b, c):
    """Принимает числа a, b, c(стороны треугольника), возвращает true, если этот треугольник равносторонний"""
    return a == b == c


def is_isosceles(a, b, c):
    """Принимает числа a, b, c(стороны треугольника), возвращает true, если этот треугольник равнобедеренный"""
    return (a == b) or (a == c) or (b == c)
