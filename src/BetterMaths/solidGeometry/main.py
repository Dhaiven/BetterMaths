import sympy
import math
from math import cos, acos, sin, asin

class Vector:
    """
    Represents a vector in three-dimensional space.
    """

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)


    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)


    def __init__(self, x, y, z, plane=None) -> None:
        """
        Initializes a Vector object with the given coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
            plane (object, optional): The plane in which the vector lies. Defaults to None.
        """
        self.x = x
        self.y = y
        self.z = z
        self.plane = plane

    def __repr__(self) -> str:
        """
        Returns a string representation of the Vector object.

        Returns:
            str: A string representation of the Vector object.
        """
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}\nplane: {self.plane}"

    def collinear(self, u) -> "tuple[bool, object]":
        """
        Checks if the vector is collinear with another vector.

        Args:
            u (Vector): The other vector to check collinearity with.

        Returns:
            tuple[bool, object]: A tuple containing a boolean value indicating collinearity and the collinear vector.
        """
        return collinear(self, u)

    def coplanar(self, u, v) -> bool:
        """
        Checks if the vector is coplanar with two other vectors.

        Args:
            u (Vector): The first vector.
            v (Vector): The second vector.

        Returns:
            bool: True if the vector is coplanar with u and v, False otherwise.
        """
        return coplanar(self, u, v)

    def inPlane(self, plane) -> "Vector":
        """
        Projects the vector onto a given plane.

        Args:
            plane (object): The plane onto which the vector should be projected.

        Returns:
            Vector: The projected vector.
        """
        return inPlane(self, plane)
    
    
    def norm(self):
        return norm(self)


class Point:
    """
    Represents a point in three-dimensional space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        z (float): The z-coordinate of the point.
    """

    def __init__(self, x, y, z, plane=None):
        self.x = x
        self.y = y
        self.z = z
        self.plane=plane
    

    def __repr__(self) -> str:
        return f"x: {self.x}\ny: {self.y}\nz: {self.z}\nplane: {self.plane}"
    
    
    def vector(self, point) -> Vector:
        return pointsVector(self,point)


class Plane:
    """
    Represents a plane in three-dimensional space.

    Attributes:
        i (Vector): The vector representing the direction of the i-axis.
        j (Vector): The vector representing the direction of the j-axis.

    Raises:
        ValueError: If the vectors i, j, and k are coplanar.

    """

    def __init__(self, point: Point, i: Vector, j: Vector) -> None:
        if collinear(i, j)[0]:
            raise ValueError("i and j are collinear!")
        self.origin=point
        self.i = i
        self.j = j
    
    def __repr__(self) -> str:
        i_coords = f"i: {self.i.x},{self.i.y},{self.i.z}"
        j_coords = f"j: {self.j.x},{self.j.y},{self.j.z}"
        return f"{i_coords}\n{j_coords}"


    def pointInPlane(self, point: Point):
        return pointInPlane(self, point)


class Line:
    """
    Represents a line in three-dimensional space.
    
    Attributes:
        point (Point): A point on the line.
        vector (Vector): The direction vector of the line.
    """
    
    def __init__(self, point: Point, vector: Vector) -> None:
        self.point = point
        self.vector = vector
    

    def __repr__(self) -> str:
        return f"point: {self.point}\nvector: {self.vector}"
    
    
    def point(self,point: Point) -> bool:
        return pointInLine(point, self)


class CooordinateSystem:
    """
    Represents a coordinate system in three-dimensional space.
    
    Attributes:
        point (Point): The origin point of the coordinate system.
        i (Vector): The first basis vector of the coordinate system.
        j (Vector): The second basis vector of the coordinate system.
        k (Vector): The third basis vector of the coordinate system.
    """

    def __init__(self, point: Point, i: Vector, j: Vector, k: Vector):
        if coplanar(i,j,k):
            raise ValueError("i, j and k must not be coplanar!")
        self.point=point
        self.i=i
        self.j=j
        self.k=k
    

    def __repr__(self) -> str:
        i_coords = f"i: {self.i.x},{self.i.y},{self.i.z}"
        j_coords = f"j: {self.j.x},{self.j.y},{self.j.z}"
        k_coords = f"k: {self.k.x},{self.k.y},{self.k.z}"
        return f"{i_coords}\n{j_coords}\n{k_coords}"


def collinear(u: Vector, v: Vector) -> "tuple[bool,object]":
    """
    Check if two vectors are collinear.

    Args:
        u (Vector): The first vector.
        v (Vector): The second vector.

    Returns:
        tuple[bool, object]: A tuple containing a boolean value indicating whether the vectors are collinear,
        and the scaling factor 'k' if they are collinear, or None if they are not collinear.
    """
    try:
        k = v.x / u.x
        if k == (v.y / u.y) == (v.z / u.z):
            return (True, k)
        else:
            return (False, None)
    except:
        return (False, None)


def coplanar(u: Vector, v: Vector, w: Vector) -> bool:
    """
    Check if three vectors are coplanar.

    Args:
        u (Vector): The first vector.
        v (Vector): The second vector.
        w (Vector): The third vector.

    Returns:
        bool: True if the vectors are coplanar, False otherwise.
    """
    if collinear(u,v)[0] or collinear(u,w)[0] or collinear(v,w)[0]:
        return True
    if solveSystem2(f"{u.x}*a+{v.x}*b-{w.x}",f"{u.y}*a+{v.y}*b-{w.y}",f"{u.z}*a+{v.z}*b-{w.z}")!={}:
        return False
    return True


def inPlane(u: Vector, plane: Plane):
    """
    Check if the vector is in the plane.

    Args:
        u (Vector): The vector.
        plane (Plane): The plane.

    Returns:
        Vector: The intersection point between the vector and the plane.
    """
    i = plane.i
    j = plane.j
    return coplanar(u,i,j)


def solveSystem1(eq1, eq2, eq3):
    """
    Solves a system of equations with 1 unknown.

    Parameters:
    eq1 (sympy.Expr): The first equation.
    eq2 (sympy.Expr): The second equation.
    eq3 (sympy.Expr): The third equation.

    Returns:
    dict: A dictionary containing the solutions for the unknown.
    """
    a = sympy.symbols('a')
    solutions = sympy.solve((eq1, eq2, eq3), (a))
    return solutions


def solveSystem2(eq1, eq2, eq3):
    """
    Solves a system of equations with 2 unknowns.

    Parameters:
    eq1 (sympy.Expr): The first equation.
    eq2 (sympy.Expr): The second equation.
    eq3 (sympy.Expr): The third equation.

    Returns:
    dict: A dictionary containing the solutions for the unknowns.
    """
    a, b = sympy.symbols('a b')
    solutions = sympy.solve((eq1, eq2, eq3), (a, b))
    return solutions


def solveSystem3(eq1, eq2, eq3):
    """
    Solves a system of equations with three unknowns.

    Parameters:
    eq1 (sympy.Expr): The first equation.
    eq2 (sympy.Expr): The second equation.
    eq3 (sympy.Expr): The third equation.

    Returns:
    dict: A dictionary containing the solutions for the unknowns.
    """
    a, b, c = sympy.symbols('a b c')
    solutions = sympy.solve((eq1, eq2, eq3), (a, b, c))
    return solutions


def pointsVector(pointA: Point, pointB: Point):
    """
    Calculates the vector between two points.

    Args:
        pointA (Point): The starting point.
        pointB (Point): The ending point.

    Returns:
        Vector: The vector between pointA and pointB.
    """
    x = pointB.x - pointA.x
    y = pointB.y - pointB.y
    z = pointB.z - pointB.z
    return Vector(x, y, z)


def pointInLine(point: Point, line: Line) -> bool:
    """
    Check if a point lies on a line.

    Args:
        point (Point): The point to check.
        line (Line): The line to check.

    Returns:
        bool: True if the point lies on the line, False otherwise.
    """
    xp = point.x
    yp = point.y
    zp = point.z
    xl = line.vector.x
    yl = line.vector.y
    zl = line.vector.z
    xlp = line.point.x
    ylp = line.point.y
    zlp = line.point.z
    solutions = solveSystem1(f"{xlp}+{xl}*a-{xp}", f"{ylp}+{yl}*a-{yp}", f"{zlp}+{zl}*a-{zp}")
    if solutions != {}:
        return True
    return False


def pointInPlane(point: Point, plane: Plane) -> bool:
    """
    Check if a point lies on a plane.

    Args:
        point (Point): The point to check.
        plane (Plane): The plane to check against.

    Returns:
        bool: True if the point lies on the plane, False otherwise.
    """
    x = point.x
    y = point.y
    z = point.z
    xo = plane.origin.x
    yo = plane.origin.y
    zo = plane.origin.z
    xi = plane.i.x
    yi = plane.i.y
    zi = plane.i.z
    xj = plane.j.x
    yj = plane.j.y
    zj = plane.j.z
    solutions = solveSystem2(f"{xo}+{xi}*a+{xj}*b-{x}",f"{yo}+{yi}*a+{yj}*b-{y}",f"{zo}+{zi}*a+{zj}*b-{z}")
    if solutions != {}:
        return True
    return False


def norm(u: Vector):
    return math.sqrt(u.x**2+u.y**2+u.z**2)


def coordinatesScalar(u: Vector, v: Vector) -> float:
    return u.x*v.x+u.y*v.y+u.z*v.z


def normScalar(u: Vector, v: Vector) -> float:
    return 0.5*(u.norm()**2+v.norm()**2)


def findAngle(u: Vector, v: Vector, type: int = 0) -> float:
    return acos(coordinatesScalar(u,v)/(u.norm()*v.norm()))



all=[
    "Vector",
    "Point",
    "Plane",
    "Line",
    "CooordinateSystem",
    "collinear",
    "coplanar",
    "inPlane",
    "solveSystem1",
    "solveSystem2",
    "solveSystem3",
    "pointsVector",
    "pointInLine",
    "pointInPlane",
    "norm"
]