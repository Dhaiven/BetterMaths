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


def resolve(calcul: str, options: 'dict[Option]' = {}):
    equation = Equation(calcul, args=options)
    return equation.result()


class Equation:
    def __init__(self, equation: str, **args):
        self.humanEquation = equation
        self.toHumanRedeable()
        self.equation = equation
        self.toProgramRedeable()

        self.options = {}
        if "args" in args and len(args.get("args")) != 0:
            self.options = args.get("args")
        else:
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
    
    def toProgramRedeable(self)->str:
        self.toHumanRedeable()

        replacables = {
            "^": "**",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
            for func in ["sqrt", "abs", "exp", "log", "cos", "sin", "tan", "acos", "asin", "atan", "atan2"]:
                replacables[str(nbr) + func] = str(nbr) + "*" + func
                
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
                "abs": lambda: abs(value),
                "exp": lambda: math.exp(value),
                "log": lambda: math.log(value, math.e),
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
        #Factorial
        elif "!" in equation:
            start = equation.find("!")
            mustBeFactorial = ""
            for i in range(start - 1, -1, -1):
                if equation[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    mustBeFactorial = equation[i] + mustBeFactorial
                else:
                    break
            return resolve(equation[:start - len(mustBeFactorial)] + str(math.factorial(int(mustBeFactorial))) + equation[start + 1:], self.options)
        elif "," in equation:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            return equation
        else:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            result = eval(equation)
        return result
    

    def split(self, separator)->"list[Equation]":
        splitedEquations = self.humanEquation.split(separator)
        result = []
        for splitedEquation in splitedEquations:
            newEquation = Equation(splitedEquation)
            newEquation.setOption(self.options)
            result.append(newEquation)
        return result
    

    def __transformOther__(self, other)->"tuple[str, dict[Option]]":
        otherEquation = ""
        options = self.options
        if type(other) != Equation:
            otherEquation = str(other)
        else:
            otherEquation = other.humanEquation
            for key, value in other.options.items():
                options[key] = value
        return otherEquation, options


    def __add__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation(self.humanEquation + "+" + otherEquation)
        new.setOption(options)
        return new


    def __radd__(self, other)->"Equation":
        return self.__add__(other)


    def __sub__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)
        
        new = Equation(self.humanEquation + "-(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rsub__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)
        
        new = Equation(otherEquation + "-(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __mul__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")*(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __rmul__(self, other)->"Equation":
        return self.__mul__(other)


    def __pow__(self, other, mod: int = None)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")**(" + otherEquation + ")")
        new.setOption(options)
        return new
    

    def __rpow__(self, other, mod: int = None)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")**(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __floordiv__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")//(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rfloordiv__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")//(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __truediv__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")/(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rtruediv__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")/(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __mod__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")%(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rmod__(self, other)->"Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")%(" + self.humanEquation + ")")
        new.setOption(options)
        return new
    

    def __divmod__(self, other) -> 'tuple[int, int]':
        result = self.result()
        otherResult = 0
        if type(other) != Equation:
            otherResult = float(other)
        else:
            otherResult = other.result()
        return (result // otherResult, result % otherResult)
    

    def __rdivmod__(self, other) -> 'tuple[int, int]':
        result = self.result()
        otherResult = 0
        if type(other) != Equation:
            otherResult = float(other)
        else:
            otherResult = other.result()
        return (otherResult // result, otherResult % result)


    def __neg__(self)->"Equation":
        new = Equation("-(" + self.humanEquation + ")")
        new.setOption(self.options)
        return new
    

    def __eq__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() == otherResult
    
    def __ne__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() != otherResult
    
    def __lt__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() < otherResult


    def __le__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() <= otherResult


    def __gt__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() > otherResult


    def __ge__(self, other)->bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() >= otherResult
    

    def __float__(self)->float:
        return float(self.result())


    def __int__(self)->int:
        return int(self.result())


    def __abs__(self)->int:
        return abs(self.result())
    

    #TODO: ndigits must be SupportsIndex
    def __round__(self, ndigits: None = None)->int:
        return round(self.result(), ndigits)
    

    def __ceil__(self)->int:
        return math.ceil(self.result())


    def __floor__(self)->int:
        return math.floor(self.result())


    def __str__(self)->str:
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
    
    def prime(self)->"Function":
        variable = self.equation.find(self.name)
        result = 1
        for i in range(variable, 0, -1):
            if self.equation[i] == "*":
                result *= self.equation[i - 1]
                i -= 1
        for i in range(variable, len(self.equation), 1):
            if self.equation[i] == "*":
                result *= self.equation[i + 1]
                i += 1
        return result




class Sum(Function):
    def __init__(self, start, end, equation, unknow = "x"):
        self.start = start
        self.end = end
        super().__init__(equation, unknow)


    def resolve(self):
        result = 0
        for i in range(self.start, self.end + 1):
            result += self.result(i)
        return result

    def toFunction(self):
        equation = [self.equation for i in range(self.start, self.end + 1)]
        return Function("+".join(equation))

    def toEquation(self, value):
        equation = [self.equation.replace(self.name, str(value)) for i in range(self.start, self.end + 1)]
        return Equation("+".join(equation))


    def __add__(self, other):
        if type(other) != Sum:
            return

        if other.start == self.start and other.end == self.end:
            new = Sum(self.start, self.end, self.humanEquation + other.humanEquation)
            new.setOption(self.options)
            return new


    def __radd__(self, other)->"Equation":
        return self.__add__(other)

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