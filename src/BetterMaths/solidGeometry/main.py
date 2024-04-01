import sympy

class Vector:
    """
    Represents a vector in three-dimensional space.
    """

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


class Plane:
    """
    Represents a plane in three-dimensional space.

    Attributes:
        i (Vector): The vector representing the direction of the i-axis.
        j (Vector): The vector representing the direction of the j-axis.
        k (Vector): The vector representing the direction of the k-axis.

    Raises:
        ValueError: If the vectors i, j, and k are coplanar.

    """

    def __init__(self, i: Vector, j: Vector, k: Vector) -> None:
        if coplanar(i, j, k):
            raise ValueError("i, j and k are coplanar!")
        self.i = i
        self.j = j
        self.k = k
    
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
    k = plane.k
    solutions = solveSystem3(f"{i.x}*a+{j.x}*b+{k.x}*c-{u.x}", f"{i.y}*a+{j.y}*b+{k.y}*c-{u.y}", f"{i.z}*a+{j.z}*b+{k.z}*c-{u.z}")
    if solutions!={}:
        return True
    return False


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