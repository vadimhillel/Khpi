N = ord('V') % 3 + 1 # -> 3

"""
TASK

1) Create the Point class and implement the following methods:

    Constructor that accepts x and y coordinates as parameters;
    __str__ method for representing class objects as a string.

2) Create a special exception class WrongDataError that outputs the message 
"This points create a degenerate triangle" when all points lie on the same 
line (the area of the triangle is 0)

3) Create a custom MissingParameterError exception class that will 
throw a "Missing parameter" message when a Triangle instance is 
created with only one or two arguments.

4) Create a Triangle class with the following methods:
    
    Constructor with 3 vertices as parameters. All vertices are instances of the Point class.
    
    Make sure that the generated triangle exists and is not degenerate,
that is, the area of the triangle is not equal to 0. If the triangle
degenerate, raise a WrongDataError exception.
    Make sure the triangle you create has 3 vertices. If it is not
yes, throw a MissingParameterError exception.

    area()
Returns the area of a triangle.
    perimeter()
Returns the perimeter rounded to 3 decimal places
    __str__
The method represents the objects of the class as a string.
"""

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
class WrongDataError(Exception):
    def __init__(self, message="This points create a degenerate triangle"):
        super().__init__(message)

class MissingParameterError(Exception):
    def __init__(self, message="Missing parameter"):
        super().__init__(message)

class Triangle:
    def __init__(self, a: Point = None, b: Point = None, c: Point = None):
        if not all(p and isinstance(p, Point) for p in (a, b, c)):
            raise MissingParameterError()
        self.a, self.b, self.c = a, b, c
        area = self.area()
        if abs(area) == 0:
            raise WrongDataError()
    
    @staticmethod
    def _distance(p1: Point, p2: Point) -> float:
        return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

    def perimeter(self) -> float:
        side1 = self._distance(self.a, self.b)
        side2 = self._distance(self.b, self.c)
        side3 = self._distance(self.c, self.a)
        return round(side1 + side2 + side3, 3)

    def area(self) -> float:
        return 0.5 * abs((self.b.x - self.a.x) * (self.c.y - self.a.y) - (self.c.x - self.a.x) * (self.b.y - self.a.y))

    def __str__(self) -> str:
        return "A = {}, B = {}, C = {}".format(self.a, self.b, self.c)


# triangle = Triangle(Point(-3, 6), Point(-3, 2), Point(3,2))
# triangle = Triangle(Point(-3, 6), Point(-3, 2))
triangle = Triangle(Point(-3, 6), Point(-3, 2), Point(-3, 2))
print(triangle)
print(triangle.area())
print(triangle.perimeter())
