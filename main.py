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
            nbrCanBePassed = 1
            end = -1
            for i in range(start + 1, len(equation)):
                element = equation[i]
                if element == "(":
                    nbrCanBePassed += 1
                elif element == ")":
                    nbrCanBePassed -= 1
                    if nbrCanBePassed == 0:
                        end = i
                        break
            value = resolve(equation[start + 1:end], self.options)
            functions = {
                "sqrt": lambda: math.sqrt(value),
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

    def __add__(self, other)->"Equation":
        options = self.options
        for key, value in other.options.items():
            options[key] = value
        new = Equation(self.humanEquation + "+" + other.humanEquation)
        new.setOption(options)
        return new
    
    def __mul__(self, other)->"Equation":
        if type(other) != Equation:
            return super.__add__()
        options = self.options
        for key, value in other.options.items():
            options[key] = value
        new = Equation(self.humanEquation + "+" + other.humanEquation)
        new.setOption(options)
        return new

    def __str__(self) -> str:
        return self.humanEquation



class Function(Equation):
    def __init__(self, equation, name = "x", **args):
        self.name = name
        super().__init__(equation, **args)

        self.cachedResults = {}
    
    def toProgramRedeable(self):
        super().toProgramRedeable()

        replacables = {}
        for nbr in range(0, 10):
            replacables[str(nbr) + self.name] = str(nbr) + "*" + self.name
        
        for froms, to in replacables.items():
            self.equation = self.equation.replace(froms, to)
        return self.equation

    def result(self, value: float) -> float:
        value = str(value)
        if value in self.cachedResults:
            return self.cachedResults[value]
        r = resolve(self.equation.replace(self.name, str(value)), self.options)
        self.cachedResults[value] = r
        return r



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

diff = Equation("exp(sqrt(0))")
print(diff.result())
