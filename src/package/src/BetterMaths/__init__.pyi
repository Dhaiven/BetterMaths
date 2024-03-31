import enum
from typing import SupportsFloat, SupportsIndex
from typing_extensions import TypeAlias

class Option(enum.Enum):
    DEGREES = 0,
    RADIAN = 1,


_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

def cos(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN)-> float: ...
def sin(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...
def tan(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...
def acos(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...
def asin(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...
def atan(x: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...
def atan2(x: _SupportsFloatOrIndex, y: _SupportsFloatOrIndex, type: Option = Option.RADIAN) -> float: ...

def resolve(calcul: str, options: 'dict[Option]' = {}) -> float: ...


class Equation:
    def setOption(self, options: dict) -> None: ...

    def result(self) -> float: ...
    def split(self, separator: str) -> "list[Equation]": ...

    def __add__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __add__(self, other: "Equation") -> "Equation": ...
    def __radd__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __radd__(self, other: "Equation") -> "Equation": ...
    def __sub__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __sub__(self, other: "Equation") -> "Equation": ...
    def __rsub__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __rsub__(self, other: "Equation") -> "Equation": ...
    def __mul__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __mul__(self, other: "Equation") -> "Equation": ...        
    def __rmul__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __rmul__(self, other: "Equation") -> "Equation": ...
    def __pow__(self, other: _SupportsFloatOrIndex, mod: int = None) -> "Equation": ...
    def __pow__(self, other: "Equation", mod: int = None) -> "Equation": ...
    def __rpow__(self, other: _SupportsFloatOrIndex, mod: int = None) -> "Equation": ...
    def __rpow__(self, other: "Equation", mod: int = None) -> "Equation": ...
    def __floordiv__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __floordiv__(self, other: "Equation") -> "Equation": ...
    def __rfloordiv__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __rfloordiv__(self, other: "Equation") -> "Equation": ... 
    def __truediv__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __truediv__(self, other: "Equation") -> "Equation": ...
    def __rtruediv__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __rtruediv__(self, other: "Equation") -> "Equation": ...
    def __mod__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __mod__(self, other: "Equation") -> "Equation": ...
    def __rmod__(self, other: _SupportsFloatOrIndex) -> "Equation": ...
    def __rmod__(self, other: "Equation") -> "Equation": ...
    def __divmod__(self, other: _SupportsFloatOrIndex) -> 'tuple[int, int]': ...
    def __divmod__(self, other: "Equation") -> 'tuple[int, int]': ...
    def __rdivmod__(self, other: _SupportsFloatOrIndex) -> 'tuple[int, int]': ...
    def __rdivmod__(self, other: "Equation") -> 'tuple[int, int]': ...
    def __neg__(self) -> "Equation": ...
    def __eq__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __eq__(self, other: "Equation") -> bool: ...
    def __ne__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __ne__(self, other: "Equation") -> bool: ...
    def __lt__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __lt__(self, other: "Equation") -> bool: ...
    def __le__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __le__(self, other: "Equation") -> bool: ...
    def __gt__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __gt__(self, other: "Equation") -> bool: ...
    def __ge__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __ge__(self, other: "Equation") -> bool: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __abs__(self) -> int: ...
    def __round__(self, ndigits: SupportsIndex = None) -> int: ...
    def __ceil__(self) -> int: ...
    def __floor__(self) -> int: ...
    def __str__(self) -> str: ...


class Function(Equation):
    def result(self, value: _SupportsFloatOrIndex) -> float: ...
    def prime(self) -> "Function": ...


class Sum(Function):
    def resolve(self) -> float: ...

    def toFunction(self) -> Function: ...
    def toEquation(self, value) -> Equation: ...

    def __add__(self, other: Sum) -> Sum: ...
    def __radd__(self, other) -> Sum: ...


class EquaDiff(Function):
    def result(self, value = ""): ...