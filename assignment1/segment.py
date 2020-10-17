# GEO1000 - Assignment 1
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

import math


def distance(x1, y1, x2, y2):
    """Calculate the distance between two points."""
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def heron(a, b, c):
    """Calculate the area of a triangle."""
    s = (a+b+c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def angle(a, b, c):
    """Calculate the angle between sides a, b of triangle."""
    return math.acos((a**2 + b**2 - c**2) / (2*a*b))


def segment_point_dist(s1x, s1y, s2x, s2y, px, py):
    """Calculate distance of a point to a line segment."""
    # calculate the triangle sides
    a = distance(s2x, s2y, px, py)
    b = distance(px, py, s1x, s1y)
    c = distance(s1x, s1y, s2x, s2y)

    # check alpha angle
    if angle(b, c, a) >= math.pi/2:
        return distance(s1x, s1y, px, py)
    # check beta angle
    elif angle(c, a, b) >= math.pi/2:
        return distance(s2x, s2y, px, py)
    # if on line do the triangle height
    else:
        area = heron(a, b, c)
        return area/c*2


print(segment_point_dist(0, 0, 10, 0, 5, 10))
print(segment_point_dist(0, 0, 10, 0, 20, 0))
print(segment_point_dist(0, 0, 10, 0, -10, -10))
print(segment_point_dist(0, 0, 10, 10, 0, 10))
print('Bonus case with point on line:')
print(segment_point_dist(0, 0, 10, 10, 5, 5))