from math import *


def main(x, y, z):
    f1 = (asin(y) ** 3) + 86 * ((z / 56) + (52 * x ** 3)) ** 5
    f2 = 46 * (1 - (89 * y ** 3) - 51 * z) - (exp(34 * z ** 3 - x ** 2) ** 4)
    f3 = ((1 + z ** 2) ** 4 - (26 * x + 46 * y ** 3 + 1) ** 3)

    return sqrt(f1 / f2) - f3
