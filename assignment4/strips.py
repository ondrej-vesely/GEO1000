# GEO1000 - Assignment 4
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

from geometry import Point, Rectangle


class Strip(object):
    def __init__(self, rectangle):
        """Constructor. Inits a Strip instance with a Rectangle describing 
        its shape and an empty points list.
        """
        self.rect = rectangle
        self.points = []


class StripStructure(object):
    def __init__(self, extent, n_strips):
        """Constructor. Inits a StripStructure instance with the correct
        number of Strip instances and makes sure that the domain is 
        correctly divided over the strips.
        """
        assert isinstance(extent, Rectangle)
        n_strips = int(n_strips)
        
        self.strips = []
        width = extent.width / n_strips

        for i in range(n_strips):
            rect = Rectangle(
                Point(extent.ll.x + (i)*width, extent.ll.y),
                Point(extent.ll.x + (i+1)*width, extent.ur.y)
            )
            self.strips.append(Strip(rect))

    def find_overlapping_strips(self, shape):
        """Returns a list of strip objects for which their rectangle intersects 
        with the shape given.
        
        Returns - list of Strips
        """
        return [strip for strip in self.strips if strip.rect.intersects(shape)]

    def query(self, shape):
        """Returns a list of points that overlaps the given shape.
        
        For this it first finds the strips that overlap the shape,
        using the find_overlapping_strips method.

        Then, all points of the selected strips are checked for intersection
        with the query shape.
        
        Returns - list of Points
        """
        points = []
        strips = self.find_overlapping_strips(shape)
        for strip in strips:
            points.extend([pt for pt in strip.points if pt.intersects(shape)])

        return points
                
    def append_point(self, pt):
        """Appends a point object to the list of points of the correct strip
        (i.e. the strip the Point intersects).

        For this it first finds the strips that overlap the point,
        using the find_overlapping_strips method.

        In case multiple strips overlap the point, the point is added
        to the strip with the left most coordinate.
        
        Returns - None
        """
        overlaps = [strip for strip in self.strips in pt.intersects(strip.rect)]
        if overlaps:
            strip = overlaps[0]
            strip.points.append(pt)

    def print_strip_statistics(self):
        """Prints:
        * how many strips there are in the structure

        And then, for all the strips in the structure:
        * an id (starting at 1),
        * the number of points in a strip, 
        * the lower left point of a strip and 
        * the upper right point of a strip.
        
        Returns - None
        """
        print('%s strips' % len(self.strips))
        for i, strip in enumerate(self.strips, start=1):
            print('#%s, with %s points, ll: %s, ur: %s' % (i,
                                                           len(strip.points),
                                                           strip.rect.ll,
                                                           strip.rect.ur))

    def dumps_strips(self):
        """Dumps the strips of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.
        
        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start=1):
            t = "{0};{1}\n".format(i, strip.rect)
            lines += t
        return lines

    def dumps_points(self):
        """Dumps the points of this structure to a str, 
        which (if saved in a text file) can be loaded as 
        delimited text layer in QGIS.
        
        Returns - str
        """
        lines = "strip;wkt\n"
        for i, strip in enumerate(self.strips, start = 1):
            for pt in strip.points:
                t = "{0};{1}\n".format(i, pt)
                lines += t
        return lines

