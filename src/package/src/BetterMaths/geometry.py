from __init__ import *
import math

class Angle:
    def __init__(self, name: str, amount: int, type: Option = Option.DEGREES) -> None:
        self.name = name
        self.amount = amount
        self.type = type


    def toDegrees(self)->float:
        if self.type == Option.RADIAN:
            return math.degrees(self.amount)
        return self.amount


    def toRadian(self)->float:
        if self.type == Option.DEGREES:
            return math.radians(self.amount)
        return self.amount


class Triangle:
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
    def __init__(
            self,
            side,
            angle1Name,
            angle2Name,
            angle3Name
            ) -> None:
        super().__init__(side, side, angle1Name, angle2Name, angle3Name)