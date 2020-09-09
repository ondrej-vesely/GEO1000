# GEO1000 - Assignment 1
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

from math import sqrt


def abc(a, b, c):
    """Solve a quadratic equation and print results."""

    print('The roots of %s x^2 + %s x + %s are:' % (a, b, c))

    d = discriminant(a, b, c)
    if d < 0:
        print('not real')
    elif d == 0:
        x = -b/2*a
        # ridiculous check
        if x == 0:
            x = 0.0
        print('x =', x)
    else:
        x1 = (-b + sqrt(d)) / 2*a
        x2 = (-b - sqrt(d)) / 2*a
        print('x1 =', x1, ', x2 =', x2)


def discriminant(a, b, c):
    return b**2 - (4*a*c)


abc(2.0, 0.0, 0.0)
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)
