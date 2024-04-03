class Point:
    """
    Represents a point in a two-dimensional space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Figure:
    def __init__(self, points: "list[Point]"):
        self.points=points

    def __repr__(self) -> str:
        return f"Figur({self.points})"

class Rectangle:
    def __init__(self, figure: Figure) -> None:
        if len(figure.points) != 4:
            raise ValueError("A rectangle must have four points!")
        points=figure.points
        a=points[0]
        b=points[1]
        c=points[2]
        if (b.x - a.x) * (c.y - b.y) == (c.x - b.x) * (b.y - a.y):
            raise ValueError("The points do not form a rectangle!")
        self.points=points
    
    
    def __repr__(self) -> str:
        return f"Rectangle({self.points})"


class Square:
    def __init__(self, figure: Figure) -> None:
        if len(figure.points) != 4:
            raise ValueError("A square must have four points!")
        points=figure.points
        a=points[0]
        b=points[1]
        c=points[2]
        if (b.x - a.x) != (c.y - b.y) or (c.x - b.x) != (b.y - a.y):
            raise ValueError("The points do not form a square!")
        self.points=points
    
    def __repr__(self) -> str:
        return f"Square({self.points})"


class Circle:
    def __init__(self, figure: Figure) -> None:
        if len(figure.points) != 2:
            raise ValueError("A circle must have two points!")
        points=figure.points
        a=points[0]
        b=points[1]
        if a.x == b.x and a.y == b.y:
            raise ValueError("The points do not form a circle!")
        self.points=points
    
    def __repr__(self) -> str:
        return f"Circle({self.points})"


class Triangle:
    def __init__(self, figure: Figure) -> None:
        if len(figure.points) != 3:
            raise ValueError("A triangle must have three points!")
        self.points=figure.points
    
    def __repr__(self) -> str:
        return f"Triangle({self.points})"


A = Point(0, 0)
B = Point(0, 1)
C = Point(1, 1)
D = Point(1, 0)
fig = Figure([A, B, C, D])
rect = Rectangle(fig)
print(rect)
square = Square(fig)
print(square)
circle = Circle(Figure([A, B]))
triangle = Triangle(Figure([A, B, C]))
print(circle)
print(triangle)