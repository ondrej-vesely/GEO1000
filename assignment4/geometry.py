# GEO1000 - Assignment 4
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

import math


# __all__ leaves out _test method and only makes
# the classes available for "from geometry import *":
__all__ = ["Point", "Circle", "Rectangle"] 


class Point(object):
    """Point class"""

    def __init__(self, x, y):
        """Constructor. Takes the x and y coordinates to define the Point instance."""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Returns WKT String "POINT (x y)"."""
        return "POINT (%s %s)" % (self.x, self.y)

    def distance(self, other):
        """Returns cartesian distance between self and other Point"""
        assert isinstance(other, Point)
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        
    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        returns - True / False
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

        elif isinstance(other, Circle):
            return self.distance(other.center) <= other.radius

        elif isinstance(other, Rectangle):
            return other.ll.x <= self.x <= other.ur.x and other.ll.y <= self.y <= other.ur.y
        else:
            print('Invalid shape type.')
            return None

class Circle(object):

    def __init__(self, center, radius):
        """Constructor. 
        Takes the center point and radius defining the Circle.
        """
        assert radius > 0
        assert isinstance(center, Point)
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """WKT str, discretizing the boundary of the circle 
        into straight line segments.
        """
        N = 400
        step = 2 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius, 
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON (({0}))".format(coordinates)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        Returns - True / False
        """
        if isinstance(other, Point):
            return other.distance(self.center) <= self.radius

        elif isinstance(other, Circle):
            return self.radius + other.radius >= self.center.distance(other.center)

        elif isinstance(other, Rectangle):
            # center inside case
            is_inside = self.center.intersects(other)
            # touching corners case
            is_corner = any([self.intersects(corner) for corner in other.corners()])
            # touching edge case
            r = self.radius
            edge_rects = [
                            Rectangle(
                                Point(other.ll.x, other.ll.y-r), 
                                Point(other.ur.x, other.ll.y)
                            ),
                            Rectangle(
                                Point(other.ur.x, other.ll.y), 
                                Point(other.ur.x+r, other.ur.y)
                            ),
                            Rectangle(
                                Point(other.ll.x, other.ur.y), 
                                Point(other.ur.x, other.ur.y+r)
                            ),
                            Rectangle(
                                Point(other.ll.x-r, other.ll.y), 
                                Point(other.ll.x, other.ur.y))
            ]
            is_edge = any([self.center.intersects(rect) for rect in edge_rects])

            # check if any of cases is True
            return any([is_inside, is_edge, is_corner])        
        else:
            print('Invalid shape type.')
            return None


class Rectangle(object):

    def __init__(self, pt_ll, pt_ur):
        """Constructor. 
        Takes the lower left and upper right point defining the Rectangle.
        """
        assert isinstance(pt_ll, Point)
        assert isinstance(pt_ur, Point)

        # wrong corners fix
        if pt_ll.x > pt_ur.x or pt_ll.y > pt_ur.y:
            print('Warning: You should input ll and ur corner points!')
            self.ll = Point(min(pt_ll.x, pt_ur.x), 
                            min(pt_ll.y, pt_ur.y))
            self.ur = Point(max(pt_ll.x, pt_ur.x), 
                            max(pt_ll.y, pt_ur.y))                       
        else:
            self.ll = pt_ll
            self.ur = pt_ur

    def __str__(self):
        """Returns WKT String "POLYGON ((x0 y0, x1 y1, ..., x0 y0))"."""
        x_min, y_min = self.ll.x, self.ll.y
        x_max, y_max = self.ur.x, self.ur.y
        coords = [
            (x_min, y_min), 
            (x_max, y_min), 
            (x_max, y_max),
            (x_min, y_max),
            (x_min, y_min)
            ]
        coord_string = ', '.join(['%s %s' % (c[0], c[1]) for c in coords])
        return "POLYGON ((%s))" % coord_string

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        Returns - True / False
        """
        if isinstance(other, Point):
            return other.intersects(self)

        elif isinstance(other, Circle):
            return other.intersects(self)

        elif isinstance(other, Rectangle):
            return all([self.ll.x <= other.ll.x + other.width(),
                        self.ll.x + self.width() >= other.ll.x,
                        self.ll.y <= other.ll.y + other.height(),
                        self.ll.y + self.height() >= other.ll.y])     
        else:
            print('Invalid shape type.')
            return None

    def corners(self):
        """List of corner points from ll counterclockwise."""
        return [self.ll, 
                Point(self.ur.x, self.ll.y),
                self.ur,
                Point(self.ll.x, self.ur.y)]

    def width(self):
        """The width of the Rectangle.
        
        Returns - float
        """
        return self.ur.x - self.ll.x

    def height(self):
        """The height of the Rectangle.
        
        Returns - float
        """
        return self.ur.y - self.ll.y


def _test():
    """Test whether your implementation of all methods works correctly."""
    # point - point
    pt0 = Point(0, 0)
    pt1 = Point(0, 0)
    pt2 = Point(10, 10)
    assert pt0.intersects(pt1)
    assert pt1.intersects(pt0)
    assert not pt0.intersects(pt2)
    assert not pt2.intersects(pt0)

    # circle - rectagle
    c1 = Circle(Point(-1, -1), 1)
    c2 = Circle(Point(0, -1), 1)
    r1 = Rectangle(Point(0,0), Point(10,10))
    assert not c1.intersects(r1)
    assert c2.intersects(r1)

    # rectangle - rectangle
    r2 = Rectangle(Point(5,5), Point(6,6))
    r3 = Rectangle(Point(-1,-1), Point(11,11))
    r4 = Rectangle(Point(-1,-1), Point(0,0))
    assert r1.intersects(r2)
    assert r1.intersects(r3)
    assert r1.intersects(r4)
    assert not r4.intersects(r2)

if __name__ == "__main__":
    _test()

