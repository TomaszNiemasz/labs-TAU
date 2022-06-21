from math import pi


def calc_factorial(number):
    if type(number) != int:
        raise TypeError
    if number < 0:
        raise ValueError
    if number < 2:
        return 1
    return number * calc_factorial(number - 1)


def calc_area_of_circle(radius):
    if type(radius) != int:
        raise TypeError
    if radius < 0:
        raise ValueError
    return (radius ** 2) * pi


def compare_numbers(number_a, number_b):
    if type(number_a) != int or type(number_b) == bool:
        raise TypeError
    if number_a == number_b:
        return True
    else:
        return False
