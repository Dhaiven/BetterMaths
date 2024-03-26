import math
import enum
from typing import override

class Option(enum.Enum):
    DEGREES = 0,
    RADIAN = 1,


def cos(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the cosine of x (measured in radians).
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.cos(x)


def sin(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the sine of x (measured in radians).
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.sin(x)


def tan(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the tangent of x (measured in radians).
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.tan(x)


def acos(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the arc cosine (measured in radians) of x.

    The result is between 0 and pi.
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.acos(x)


def asin(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the arc sine (measured in radians) of x.

    The result is between -pi/2 and pi/2.
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.asin(x)


def atan(x: float, type: Option = Option.RADIAN)->float:
    """
    Return the arc tangent (measured in radians) of x.

    The result is between -pi/2 and pi/2.
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.atan(x)


def atan2(x: float, y: float, type: Option = Option.RADIAN)->float:
    """
    Return the arc tangent (measured in radians) of y/x.

    Unlike atan(y/x), the signs of both x and y are considered.
    """
    if type == Option.DEGREES:
        x = math.radians(x)
        y = math.radians(y)
    return math.atan2(x, y)


def resolve(calcul: str, options: dict[Option]):
    equation = Equation(calcul)
    equation.setOption(options)
    return equation.result()


class Equation:
    def __init__(self, equation, **args):
        self.humanEquation = equation
        self.toHumanRedeable()
        self.equation = equation
        self.toProgramRedeable()

        self.options = {}
        self.options["angles"] = args.get("angles", Option.DEGREES)
    
    def setOption(self, options: dict):
        self.options = options

    def toHumanRedeable(self):
        replacables = {
            " ": "",
            "++": "+",
            "+-": "-",
            "--": "-",
            "--": "+",
        }

        for froms, to in replacables.items():
            self.humanEquation = self.humanEquation.replace(froms, to)
        return self.humanEquation
    
    def toProgramRedeable(self):
        self.toHumanRedeable()

        replacables = {
            "^": "**",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
        replacables["atan2*("] = "atan2("

        for froms, to in replacables.items():
            self.equation = self.equation.replace(froms, to)
        return self.equation

    def result(self)->float:
        equation = self.toProgramRedeable()
        result = 0
        if "(" in equation:
            start = equation.find("(")
            end = equation.rfind(")")
            value = resolve(equation[start + 1:end], self.options)
            functions = {
                "exp": lambda: math.exp(value),
                "cos": lambda: cos(value, self.options["angles"]),
                "sin": lambda: sin(value, self.options["angles"]),
                "tan": lambda: tan(value, self.options["angles"]),
                "acos": lambda: acos(value, self.options["angles"]),
                "asin": lambda: asin(value, self.options["angles"]),
                "atan": lambda: atan(value, self.options["angles"]),
                "atan2": lambda: atan2(float(str(value).split(",")[0]), float(str(value).split(",")[1]), self.options["angles"]),
            }
            for key, func in functions.items():
                if key == equation[start - len(key):start]:
                    value = func()
                    start -= len(key)
                    break

            return resolve(equation[:start] + str(value) + equation[end + 1:], self.options)
        elif "," in equation:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            return equation
        else:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            result += float(eval(equation))
        return result
    
    def __str__(self) -> str:
        return self.humanEquation



class Function(Equation):
    def __init__(self, equation, name = "x", **args):
        self.name = name
        super().__init__(equation, **args)
    
    @override
    def toProgramRedeable(self):
        super().toProgramRedeable()

        replacables = {}
        for nbr in range(0, 10):
            replacables[str(nbr) + self.name] = str(nbr) + "*" + self.name
        
        for froms, to in replacables.items():
            self.equation = self.equation.replace(froms, to)
        return self.equation
    
    def result(self, value: float) -> float:
        return resolve(self.equation.replace(self.name, str(value)), self.options)



class EquaDiff(Function):
    def __init__(self, equation, name="x", **args):
        super().__init__(equation, name, **args)

    def result(self, value = ""):
        a = self.equation.split("+")[0]
        a = a.replace(self.name, value)
        a = resolve(a, self.options)
        b = self.equation.split("+")[1]
        self.equation = "Cexp(" + str(a) + self.name + ") + " + str(-int(b) / int(a))
        print(self.equation)
        return self.toHumanRedeable()

diff = Function("2y+2", "y")
print(diff.result(1))
print(diff)