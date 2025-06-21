#project7_circle_geometry.py
#📄 Description:
#Implements geometric functions to check if a point or rectangle lies inside or overlaps a circle.
print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    for corner in rect:
        if not point_in_circle(circle, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    for corner in rect:
        if point_in_circle(circle, corner):
            return True
    return False

# Example usage
center = Point(150, 100)
circle = Circle(center, 75)
rectangle = [Point(140, 90), Point(160, 90), Point(160, 110), Point(140, 110)]

print("Point in circle:", point_in_circle(circle, Point(150, 100)))
print("Rectangle fully inside circle:", rect_in_circle(circle, rectangle))
print("Any rectangle corner in circle:", rect_circle_overlap(circle, rectangle))
