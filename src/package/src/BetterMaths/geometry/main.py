from BetterMaths.main import Option
from math import degrees, radians

class Angle:
    """
    Represents an angle.

    Attributes:
        name (str): The name of the angle.
        amount (int): The amount of the angle.
        type (Option): The type of the angle (degrees or radians).

    Methods:
        toDegrees(): Converts the angle to degrees.
        toRadian(): Converts the angle to radians.
    """

    def __init__(self, name: str, amount: int, type: Option = Option.DEGREES) -> None:
        self.name = name
        self.amount = amount
        self.type = type


    def toDegrees(self) -> float:
        """
        Converts the angle to degrees.

        Returns:
            float: The angle in degrees.
        """
        if self.type == Option.RADIAN:
            return degrees(self.amount)
        return self.amount


    def toRadian(self) -> float:
        """
        Converts the angle to radians.

        Returns:
            float: The angle in radians.
        """
        if self.type == Option.DEGREES:
            return radians(self.amount)
        return self.amount


class Triangle:
    """
    Represents a triangle with given side lengths and angles.
    
    Args:
        side1 (float): Length of the first side of the triangle.
        side2 (float): Length of the second side of the triangle.
        side3 (float): Length of the third side of the triangle.
        angle1 (float): Measure of the first angle of the triangle in degrees.
        angle2 (float): Measure of the second angle of the triangle in degrees.
        angle3 (float): Measure of the third angle of the triangle in degrees.
    """
    def __init__(
            self,
            side1,
            side2,
            side3,
            angle1,
            angle2,
            angle3
            ) -> None:
        pass



class IsoscelesTriangle(Triangle):
    """
    Represents an isosceles triangle, a type of triangle with two equal sides.
    
    Args:
        Triangle: The triangle to test.
    
    Attributes:
        Inherits all attributes from the Triangle class.
    """
    def __init__(
            self,
            isosceleSide,
            otherSide,
            angle1Name,
            angle2Name,
            angle3Name
            ) -> None:
        super().__init__(isosceleSide, isosceleSide, otherSide, Angle(angle1Name, 60), Angle(angle2Name, 60), Angle(angle3Name, 60))



class RightAngledIsoscelesTriangle(IsoscelesTriangle):
    """
    Represents a right-angled isosceles triangle.

    Inherits from the IsoscelesTriangle class.

    Args:
        IsoscelesTriangle: The isosceles triangle to test.

    Attributes:
        Inherits all attributes from the IsoscelesTriangle class.

    """
    def __init__(
            self,
            isosceleSide,
            hypotenuse,
            angle1Name,
            angle2Name,
            angle3Name
            ) -> None:
        super().__init__(isosceleSide, hypotenuse, Angle(angle1Name, 90), Angle(angle2Name, 45), Angle(angle3Name, 45))


class EquilateralTriangle(IsoscelesTriangle):
    """
    Represents an equilateral triangle, a type of isosceles triangle where all sides are equal.

    Args:
        IsoscelesTriangle: The isosceles triangle to test.
    
    Attributes:
        Inherits all attributes from the IsoscelesTriangle class.
    """
    def __init__(
            self,
            side,
            angle1Name,
            angle2Name,
            angle3Name
            ) -> None:
        super().__init__(side, side, angle1Name, angle2Name, angle3Name)


__all__ = [
  "Angle", "Triangle", "IsoscelesTriangle", "RightAngledIsoscelesTriangle", "EquilateralTriangle"
]