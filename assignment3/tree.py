# GEO1000 - Assignment 3
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

import math

def distance(p1, p2):
    """Returns Cartesian distance (as float) between two 2D points."""
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)


def point_angle_distance(pt, beta, distance):
    """Compute new point that is distance away from pt in direction beta."""
    x = math.cos(beta)
    y = math.sin(beta)
    return (pt[0] + x*distance, pt[1] + y*distance)



def absolute_angle(p1, p2):
    """Returns the angle (in radians) between the positive x-axis 
    and the line through two given points, p1 and p2."""
    x = p2[0] - p1[0]
    y = p2[1] - p1[1] 
    return math.atan2(y, x)


def opposite_edge(p1, p2):
    """Compute edge parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    dist = distance(p1, p2)
    perp = absolute_angle(p1, p2) + math.pi/2
    p3, p4 = [point_angle_distance(pt, perp, dist) for pt in (p2, p1)]
    return (p3, p4)


def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines 
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    total_angle = absolute_angle(p1, p2) + alpha
    dist = distance(p1, p2) * math.cos(alpha)
    return point_angle_distance(p1, total_angle, dist)


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square.
    """
    points = (p1, p2, p3, p4, p1)
    coord_str = ['%.4f %.4f' % (pt[0], pt[1]) for pt in points]
    return "POLYGON ((%s))" % ', '.join(coord_str)
    

def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    p3, p4 = opposite_edge(p1, p2)
    area = distance(p1, p2) ** 2
    line = "%s; %s; %.4f\n" % (as_wkt(p1, p2, p3, p4), currentorder, area)
    with open(filename, 'a') as file:
        file.write(line)
    
    if currentorder < totalorder:
        split = split_point(p4, p3, alpha)
        draw_pythagoras_tree(p4, split, alpha, currentorder + 1, totalorder, filename)
        draw_pythagoras_tree(split, p3, alpha, currentorder + 1, totalorder, filename)
    

if __name__ == "__main__":
    
    with open('out.wkt', 'w') as fh:  # 'with' statement closes 
                                      # file automatically
        fh.write("geometry;currentorder;area\n")
   
    draw_pythagoras_tree(p1=(5,0), 
        p2=(6,0), 
        alpha=math.radians(45),
        currentorder=0,
        totalorder=6,
        filename='out.wkt')
