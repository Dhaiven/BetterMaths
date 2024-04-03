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


class Expression:
    def setOption(self, options: dict) -> None: ...

    def result(self) -> float: ...
    def split(self, separator: str) -> "list[Expression]": ...

    def __add__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __add__(self, other: "Expression") -> "Expression": ...
    def __radd__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __radd__(self, other: "Expression") -> "Expression": ...
    def __sub__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __sub__(self, other: "Expression") -> "Expression": ...
    def __rsub__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __rsub__(self, other: "Expression") -> "Expression": ...
    def __mul__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __mul__(self, other: "Expression") -> "Expression": ...        
    def __rmul__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __rmul__(self, other: "Expression") -> "Expression": ...
    def __pow__(self, other: _SupportsFloatOrIndex, mod: int = None) -> "Expression": ...
    def __pow__(self, other: "Expression", mod: int = None) -> "Expression": ...
    def __rpow__(self, other: _SupportsFloatOrIndex, mod: int = None) -> "Expression": ...
    def __rpow__(self, other: "Expression", mod: int = None) -> "Expression": ...
    def __floordiv__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __floordiv__(self, other: "Expression") -> "Expression": ...
    def __rfloordiv__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __rfloordiv__(self, other: "Expression") -> "Expression": ... 
    def __truediv__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __truediv__(self, other: "Expression") -> "Expression": ...
    def __rtruediv__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __rtruediv__(self, other: "Expression") -> "Expression": ...
    def __mod__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __mod__(self, other: "Expression") -> "Expression": ...
    def __rmod__(self, other: _SupportsFloatOrIndex) -> "Expression": ...
    def __rmod__(self, other: "Expression") -> "Expression": ...
    def __divmod__(self, other: _SupportsFloatOrIndex) -> 'tuple[int, int]': ...
    def __divmod__(self, other: "Expression") -> 'tuple[int, int]': ...
    def __rdivmod__(self, other: _SupportsFloatOrIndex) -> 'tuple[int, int]': ...
    def __rdivmod__(self, other: "Expression") -> 'tuple[int, int]': ...
    def __neg__(self) -> "Expression": ...
    def __eq__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __eq__(self, other: "Expression") -> bool: ...
    def __ne__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __ne__(self, other: "Expression") -> bool: ...
    def __lt__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __lt__(self, other: "Expression") -> bool: ...
    def __le__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __le__(self, other: "Expression") -> bool: ...
    def __gt__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __gt__(self, other: "Expression") -> bool: ...
    def __ge__(self, other: _SupportsFloatOrIndex) -> bool: ...
    def __ge__(self, other: "Expression") -> bool: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __abs__(self) -> int: ...
    def __round__(self, ndigits: SupportsIndex = None) -> int: ...
    def __ceil__(self) -> int: ...
    def __floor__(self) -> int: ...
    def __str__(self) -> str: ...


class Function(Expression):
    def result(self, value: _SupportsFloatOrIndex) -> float: ...
    def prime(self) -> "Function": ...


class Sum(Expression):
    def result(self) -> float: ...

    def toFunction(self) -> Function: ...
    def toExpression(self, value) -> Expression: ...

    def __add__(self, other: "Sum") -> "Sum": ...
    def __radd__(self, other: "Sum") -> "Sum": ...


class Prod(Expression):
    def result(self) -> float: ...

    def toFunction(self) -> Function: ...
    def toExpression(self, value) -> Expression: ...