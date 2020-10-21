# GEO1000 - Assignment 4
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

from geometry import Point, Rectangle, Circle
from strips import StripStructure


def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.
    
    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.
    
    Returns - None or a StripStructure instance
    """
    with open(file_nm, 'r') as f:
        lines = [line for line in f.readlines() if not line.startswith('#')]

    bbox, *pts = [[float(c) for c in line.split(' ')] for line in lines]

    if len(bbox) == 4:
        extent = Rectangle(
            Point(bbox[0], bbox[1]),
            Point(bbox[2], bbox[3])
        )
        structure = StripStructure(extent, no_strips)

        for pt in pts:
            if len(pt) == 2:
                structure.append_point(Point(pt[0], pt[1]))
                
        return structure


def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.
    
    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dump_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dump_points())

