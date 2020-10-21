# GEO1000 - Assignment 4
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

from reader import read
from geometry import Rectangle, Circle, Point
from os.path import basename


def parse(geom_str):
    """Parse a string into a shape object (Point, Circle, or Rectangle)

    Formats that can be given:
    p <px> <py>
    c <cx> <cy> <r>
    r <llx> <lly> <urx> <ury>
    
    Returns - Point, Circle, or Rectangle
    """
    if geom_str.startswith('p'):
        _, x, y, *_ = geom_str.split(' ')
        return Point(float(x), float(y))

    elif geom_str.startswith('c'):
        _, cx, cy, r, *_= geom_str.split(' ')
        return Circle(Point(float(cx), float(cy)), float(r))

    elif geom_str.startswith('r'):
        _, llx, lly, urx, ury, *_ = geom_str.split(' ')
        return Rectangle(
            Point(float(llx), float(lly)),
            Point(float(urx), float(ury))
        )

def print_statistics(result):
    """Prints statistics for the resulting list of Points of a query
    
    * Number of points overlapping (i.e. number of points in the list)
    * The leftmost point and its identity given by the id function
    * The rightmost point and its identity given by the id function
    
    Returns - None
    """
    if result:
        left = right = result[0]
        for pt in result:
            if pt.x < left.x:
                left = pt
            elif pt.x == left.x and pt.y < left.y:
                left = pt
            elif pt.x > right.x:
                right = pt
            elif pt.x == right.x and pt.y > right.y:
                right = pt 

        msg = """
    +--------------+
    + Result       +
    +--------------+
    %s point(s).
    leftmost: %s id: %s
    rightmost: %s id: %s
        """ % (len(result), left, id(left), right, id(right))

    empty_msg = """
    +--------------+
    + Result       +
    +--------------+
    No points found inside shape.
    """
    
    print(msg if result else empty_msg)

def print_help():
    """Prints a help message to the user, what can be done with the program."""
    helptxt = """
Commands available:
-------------------
    General:
        help
        quit

    Reading points in a structure, defining how many strips should be used:
        open <filenm> into <number_of_strips>

    Querying:
        with a point:     p <px> <py>
        with a circle:    c <cx> <cy> <radius>
        with a rectangle: r <llx> <lly> <urx> <ury>
    """
    print(helptxt)

# =============================================================================
# Below are some commands that you may use to test your codes:
# open points2.txt into 5
# p 5.0 5.0
# c 10.0 10.0 1.0
# r 2.0 2.0 8.0 4.0
# =============================================================================
def main():
    """The main function of this program.
    """
    structure = None
    print("Welcome to {0}.".format(basename(__file__)))
    print("=" * 76)
    print_help()
    while True:
        try:
            in_str = input("your command>>>\n").lower().strip()
            if in_str.startswith("quit"):
                print("Bye, bye.")
                return
            elif in_str.startswith("help"):
                print_help()
            elif in_str.startswith("open"):
                filenm, nstrips = in_str.replace("open ", "").split(" into ")
                structure = read(filenm, int(nstrips))
                structure.print_strip_statistics()
            elif in_str.startswith("p") or in_str.startswith("c") or in_str.startswith("r"):
                if structure is None:
                    print("No points read yet, open a file first!")
                else:
                    print_statistics(structure.query(parse(in_str)))
            else: 
                print("Input not understood (use 'help')")
                
        except AssertionError:
            print('Invalid input value!')


if __name__ == "__main__":
    main()
