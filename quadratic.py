# Module quadratic

from math import sqrt


def solve_quadratic(a, b, c):
    if a == 0:
        return None, None, None

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + sqrt(d)) / 2 / a
        x2 = (-b - sqrt(d)) / 2 / a
        return d, x1, x2
    elif d == 0:
        x = -b / 2 / a

        return d, x, x
    else:
        return d, None, None


def formula(a, b, c):
    result = "$"
    if a == 1:
        result += "x^2"
    elif a != 0:
        result += f"{a:g}x^2"

    if b == 1:
        result += "x"
    elif b != 0:
        result += f"{b:+g}x"

    if c != 0:
        result += f"{c:+g}"

    result += "=0$"
    return result