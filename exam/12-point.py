class Point2:

    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except:
            raise ValueError("Couldn't cast to float.")
        
    def cab_distance(self, other):
        if isinstance(other, Point2):
            return abs(self.x-other.x) + abs(self.y - other.y)
        else:
            return abs(self.x-other[0]) + abs(self.y - other[1])
    
    def __str__(self):
        return "%.4f, %.4f" % (self.x, self.y)


p, q = Point2(1,1), Point2(5,6)
print(p.cab_distance(q))


    



