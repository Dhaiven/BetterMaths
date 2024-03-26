import math
import enum

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
    return math.atan2(x)


def resolve(calcul: str, options: dict[Option]):
    equation = Equation(calcul)
    equation.setOption(options)
    return equation.result()


class Equation:
    def __init__(self, equation, **args):
        self.equation = self.toHumanRedeable(equation)

        self.options = {}
        self.options["angles"] = args.get("angles", Option.DEGREES)
    
    def setOption(self, options: dict):
        self.options = options

    def toHumanRedeable(self, equation: str):
        replacables = {
            "++": "+",
            "+-": "-",
            "--": "-",
            "--": "+",
            "**": "^",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
        
        for froms, to in replacables.items():
            equation = equation.replace(froms, to)
        return equation
    
    def toProgramRedeable(self):
        replacables = {
            "^": "**",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
        
        for froms, to in replacables.items():
            self.equation = self.equation.replace(froms, to)
        return self.equation
    
    def sin(self, equation):
        return sin(equation, self.options["angles"])
    
    def cos(self, equation):
        return cos(equation, self.options["angles"])

    def result(self)->float:
        equation = self.toProgramRedeable()
        result = 0
        if "(" in equation:
            start = len(equation)
            end = 0
            for i in range(len(equation)):
                if equation[i] == "(" and i < start:
                    start = i
                elif equation[i] == ")" and i > end:
                    end = i
            value = ""
            for i in range(start + 1, end):
                value += equation[i]
            functions = {
                "exp": math.exp,
                "cos": self.cos,
                "sin": self.sin,
                "tan": math.tan
            }
            for key, func in functions.items():
                areFunction = True
                for i in range(start - len(key) + 1, start + 1):
                    if equation[start - i] != key[start - i]:
                        areFunction = False
                if areFunction:
                    value = str(func(resolve(value, self.options)))
                    start -= len(key)
                    break

            return resolve(equation[:start] + str(resolve(value, self.options)) + equation[end + 1:], self.options)
        else:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            result += float(eval(equation))
        return result
    
    def __str__(self) -> str:
        return self.equation


class EquaDiff:
    def __init__(self, yPrime, unknow) -> None:
        self.yPrime: str = yPrime
        self.unknow = unknow
    def result(self, value = ""):
        if type(value) != str:
            value = str(value)
        if value != "":
            value = "*" + value
        #equation = self.yPrime.replace(self.unknow, str(value))
        a = self.yPrime.split("+")[0]
        a = a.replace(self.unknow, value)
        a = self.equation(a)
        b = self.yPrime.split("+")[1]
        return self.toGoodEquation("Cexp(" + str(a) + self.unknow + ") + " + str(-int(b) / int(a)))

diff = Equation("cos(1)", angles=Option.RADIAN)
print(diff.result())
print(diff)
print(math.cos(1))