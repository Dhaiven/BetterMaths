import math
import enum

class Option(enum.Enum):
    DEGREES = 0,
    RADIAN = 1,


def cos(x: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the cosine of a given angle.

    Args:
        x (float): The angle in radians or degrees, depending on the value of `type`.
        type (Option, optional): The type of angle. Defaults to Option.RADIAN.

    Returns:
        float: The cosine of the angle.

    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.cos(x)


def sin(x: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the sine of a given angle.

    Args:
        x (float): The angle in radians or degrees, depending on the `type` parameter.
        type (Option, optional): The type of the angle. Defaults to Option.RADIAN.

    Returns:
        float: The sine of the angle.

    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.sin(x)


def tan(x: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the tangent of an angle.

    Args:
        x (float): The angle in radians or degrees, depending on the value of `type`.
        type (Option, optional): The type of the angle. Defaults to Option.RADIAN.

    Returns:
        float: The tangent of the angle.

    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.tan(x)


def acos(x: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the arc cosine of a number.

    Args:
        x (float): The value for which to calculate the arc cosine.
        type (Option, optional): The type of the input value. Defaults to Option.RADIAN.

    Returns:
        float: The arc cosine of the input value.
    
    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.acos(x)


def asin(x: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the arcsine of a number.

    Args:
        x (float): The number to calculate the arcsine of.
        type (Option, optional): The type of the input value. Defaults to Option.RADIAN.

    Returns:
        float: The arcsine of the input number.

    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.asin(x)


def atan(x: float, type: Option = Option.RADIAN) -> float:
    """
    Compute the arctangent of x.

    Args:
        x (float): The value for which to compute the arctangent.
        type (Option, optional): The type of the input value. Defaults to Option.RADIAN.

    Returns:
        float: The arctangent of x.

    """
    if type == Option.DEGREES:
        x = math.radians(x)
    return math.atan(x)


def atan2(x: float, y: float, type: Option = Option.RADIAN) -> float:
    """
    Calculate the arctangent of y/x in the specified type.

    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
        type (Option, optional): The type of the result. Defaults to Option.RADIAN.

    Returns:
        float: The arctangent value in the specified type.
    """
    if type == Option.DEGREES:
        x = math.radians(x)
        y = math.radians(y)
    return math.atan2(x, y)


def resolve(calcul: str, options: 'dict[Option]' = {}):
    """
    Resolve the given calculation string using the specified options.

    Args:
        calcul (str): The calculation string to be resolved.
        options (dict[Option], optional): The options to be used for resolving the calculation.
            Defaults to an empty dictionary.

    Returns:
        The result of the resolved calculation.
    """
    equation = Equation(calcul, args=options, mustCheck=False)
    return equation.result()



functions = {
    "sqrt": lambda value, options: math.sqrt(value),
    "abs": lambda value, options: abs(value),
    "exp": lambda value, options: math.exp(value),
    "log": lambda value, options: math.log(value, math.e),
    "cos": lambda value, options: cos(value, options["angles"]),
    "sin": lambda value, options: sin(value, options["angles"]),
    "tan": lambda value, options: tan(value, options["angles"]),
    "acos": lambda value, options: acos(value, options["angles"]),
    "asin": lambda value, options: asin(value, options["angles"]),
    "atan": lambda value, options: atan(value, options["angles"]),
    "atan2": lambda value, options: atan2(float(str(value).split(",")[0]), float(str(value).split(",")[1]), options["angles"]),
}
minNameLenght = math.inf
maxNameLenght = -1
for key in functions:
    if len(key) < minNameLenght:
        minNameLenght = len(key)
    elif len(key) > maxNameLenght:
        maxNameLenght = len(key)
# Because last index in range is exclude
maxNameLenght += 1



humanReadable = {
    " ": "",
    "++": "+",
    "+-": "-",
    "-+": "-",
    "--": "+",
}

programReadable = {
    "^": "**",
}
for nbr in range(0, 10):
    programReadable[str(nbr) + "("] = str(nbr) + "*("
    for func in functions:
        programReadable[str(nbr) + func] = str(nbr) + "*" + func
programReadable["atan2*("] = "atan2("

class Equation:
    """
    Represents a mathematical equation.

    Attributes:
        equation (str): The equation in program-readable format.
        humanEquation (str): The equation in human-readable format.
        options (dict): Options for evaluating the equation.

    Methods:
        __init__(self, equation: str, **args): Initializes a new Equation object.
        setOption(self, options: dict): Sets the options for the equation.
        toHumanRedeable(self): Converts the equation to human-readable format.
        toProgramRedeable(self) -> str: Converts the equation to program-readable format.
        result(self) -> float: Evaluates the equation and returns the result.
        split(self, separator) -> list[Equation]: Splits the equation into multiple equations based on the separator.
        __transformOther__(self, other) -> tuple[str, dict[Option]]: Transforms the other equation or value into a tuple of equation and options.
        __add__(self, other) -> Equation: Adds the other equation or value to the current equation.
        __radd__(self, other) -> Equation: Adds the current equation to the other equation or value.
        __sub__(self, other) -> Equation: Subtracts the other equation or value from the current equation.
        __rsub__(self, other) -> Equation: Subtracts the current equation from the other equation or value.
        __mul__(self, other) -> Equation: Multiplies the current equation with the other equation or value.
        __rmul__(self, other) -> Equation: Multiplies the other equation or value with the current equation.
        __pow__(self, other, mod: int = None) -> Equation: Raises the current equation to the power of the other equation or value.
        __rpow__(self, other, mod: int = None) -> Equation: Raises the other equation or value to the power of the current equation.
        __floordiv__(self, other) -> Equation: Performs floor division of the current equation by the other equation or value.
        __rfloordiv__(self, other) -> Equation: Performs floor division of the other equation or value by the current equation.
        __truediv__(self, other) -> Equation: Performs true division of the current equation by the other equation or value.
        __rtruediv__(self, other) -> Equation: Performs true division of the other equation or value by the current equation.
        __mod__(self, other) -> Equation: Performs modulo operation of the current equation by the other equation or value.
        __rmod__(self, other) -> Equation: Performs modulo operation of the other equation or value by the current equation.
        __divmod__(self, other) -> tuple[int, int]: Performs divmod operation of the current equation by the other equation or value.
        __rdivmod__(self, other) -> tuple[int, int]: Performs divmod operation of the other equation or value by the current equation.
        __neg__(self) -> Equation: Negates the current equation.
        __eq__(self, other) -> bool: Checks if the current equation is equal to the other equation or value.
        __ne__(self, other) -> bool: Checks if the current equation is not equal to the other equation or value.
        __lt__(self, other) -> bool: Checks if the current equation is less than the other equation or value.
        __le__(self, other) -> bool: Checks if the current equation is less than or equal to the other equation or value.
    """
    
    def __init__(self, equation: str, **args):
        for froms, to in humanReadable.items():
            if froms in equation: # Just for optimisation
                equation = equation.replace(froms, to)
        #If we have +number at the beginning
        while equation.startswith("+"):
            equation = equation[1:]
        self.humanEquation = equation
        
        self.equation = self.humanEquation
        for froms, to in self.__getProgramReadable__().items():
            if froms in self.equation: # Just for optimisation
                self.equation = self.equation.replace(froms, to)

        self.options = {}
        if "args" in args and len(args.get("args")) != 0:
            self.options = args.get("args")
        else:
            self.options["angles"] = args.get("angles", Option.DEGREES)


    def setOption(self, options: dict):
        self.options = options

    def toHumanRedeable(self) -> str:
        return self.humanEquation
    
    def toProgramRedeable(self) -> str:
        return self.equation
    
    def __getProgramReadable__(self) -> dict:
        return programReadable

    def result(self) -> float:
        try:
            return self.__resolve__(self.equation)
        except OverflowError:
            return math.inf
        
    
    def sum(self, equation: str) -> float:
        values = equation.split("+")
        result = 0
        while len(values) > 0:
            result += self.__resolve__(values.pop())
        return result
    
    def sub(self, equation: str):
        return eval(equation)
    
    def pow(self, equation: str) -> float:
        values = equation.split("*")
        result = 1
        while len(values) > 0:
            result *= self.__resolve__(values.pop())
        return result
    
    def power(self, equation: str) -> float:
        values = equation.split("**")
        result = self.__resolve__(values.pop())
        while len(values) > 0:
            result = self.__resolve__(values.pop()) ** result
        return result
    
    def divide(self, equation: str) -> float:
        values = equation.split("/")
        result = self.__resolve__(values.pop(0))
        while len(values) > 0:
            result /= self.__resolve__(values.pop(0))
        return result
    
    def floordivide(self, equation: str) -> float:
        values = equation.split("//")
        result = self.__resolve__(values.pop(0))
        while len(values) > 0:
            result //= self.__resolve__(values.pop(0))
        return result
    
    def modulo(self, equation: str) -> float:
        values = equation.split("%")
        result = self.__resolve__(values.pop(0))
        while len(values) > 0:
            result %= self.__resolve__(values.pop(0))
        return result

    def __resolve__(self, equation: str) -> float:
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
            value = self.__resolve__(equation[start + 1:end])
            
            for key in range(minNameLenght, maxNameLenght):
                func = functions.get(equation[start - key:start])
                if func != None:
                    value = func(value, self.options)
                    start -= key
                    break
            
            return self.__resolve__(equation[:start] + str(value) + equation[end + 1:])
        #Factorial
        elif "!" in equation:
            start = equation.find("!")
            mustBeFactorial = ""
            for i in range(start - 1, -1, -1):
                if equation[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    mustBeFactorial = equation[i] + mustBeFactorial
                else:
                    break
            return self.__resolve__(equation[:start - len(mustBeFactorial)] + str(math.factorial(int(mustBeFactorial))) + equation[start + 1:])
        elif "," in equation:
            if "pi" in equation:
                equation = equation.replace("pi", str(math.pi))
            return equation
        elif "+" in equation:
            return self.sum(equation)
        elif "-" in equation:
            return self.sub(equation)
        elif "//" in equation:
            return self.floordivide(equation)
        elif "/" in equation:
            return self.divide(equation)
        elif "%" in equation:
            return self.modulo(equation)
        elif "**" in equation:
            return self.power(equation)
        elif "*" in equation:
            return self.pow(equation)

        if "pi" in equation:
            equation = equation.replace("pi", str(math.pi))
        return float(equation)
    

    def split(self, separator) -> "list[Equation]":
        splitedEquations = self.humanEquation.split(separator)
        result = []
        for splitedEquation in splitedEquations:
            newEquation = Equation(splitedEquation)
            newEquation.setOption(self.options)
            result.append(newEquation)
        return result
    

    def __transformOther__(self, other) -> "tuple[str, dict[Option]]":
        otherEquation = ""
        options = self.options
        if type(other) != Equation:
            otherEquation = str(other)
        else:
            otherEquation = other.humanEquation
            for key, value in other.options.items():
                options[key] = value
        return otherEquation, options


    def __add__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation(self.humanEquation + "+" + otherEquation)
        new.setOption(options)
        return new


    def __radd__(self, other) -> "Equation":
        return self.__add__(other)


    def __sub__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)
        
        new = Equation(self.humanEquation + "-(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rsub__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)
        
        new = Equation(otherEquation + "-(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __mul__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")*(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __rmul__(self, other) -> "Equation":
        return self.__mul__(other)


    def __pow__(self, other, mod: int = None) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")**(" + otherEquation + ")")
        new.setOption(options)
        return new
    

    def __rpow__(self, other, mod: int = None) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")**(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __floordiv__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")//(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rfloordiv__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")//(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __truediv__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")/(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rtruediv__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + otherEquation + ")/(" + self.humanEquation + ")")
        new.setOption(options)
        return new


    def __mod__(self, other) -> "Equation":
        otherEquation, options = self.__transformOther__(other)

        new = Equation("(" + self.humanEquation + ")%(" + otherEquation + ")")
        new.setOption(options)
        return new


    def __rmod__(self, other) -> "Equation":
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


    def __neg__(self) -> "Equation":
        new = Equation("-(" + self.humanEquation + ")")
        new.setOption(self.options)
        return new
    

    def __eq__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() == otherResult
    
    def __ne__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() != otherResult
    
    def __lt__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() < otherResult


    def __le__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() <= otherResult


    def __gt__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() > otherResult


    def __ge__(self, other) -> bool:
        otherResult = ""
        if type(other) != Equation:
            otherResult = resolve(str(other))
        else:
            otherResult = other.result()

        return self.result() >= otherResult
    

    def __float__(self) -> float:
        return float(self.result())


    def __int__(self) -> int:
        return int(self.result())


    def __abs__(self) -> int:
        return abs(self.result())
    

    #TODO: ndigits must be SupportsIndex
    def __round__(self, ndigits: None = None) -> int:
        return round(self.result(), ndigits)
    

    def __ceil__(self) -> int:
        return math.ceil(self.result())


    def __floor__(self) -> int:
        return math.floor(self.result())


    def __str__(self) -> str:
        return self.humanEquation



class Function(Equation):
    def __init__(self, equation, name = "x", **args):
        self.name = name
        super().__init__(equation, **args)

        self.cachedResults = {}
        self.hasUnknow = self.equation.find(name) != -1
    
    def __getProgramReadable__(self) -> dict:
        replacables = super().__getProgramReadable__()
        for nbr in range(0, 10):
            replacables[str(nbr) + self.name] = str(nbr) + "*" + self.name
        return replacables


    def result(self, value: float) -> float:
        value = str(value)
        if value in self.cachedResults:
            return self.cachedResults[value]
        if self.hasUnknow:
            r = resolve(self.equation.replace(self.name, value), self.options)
        else:
            r = resolve(self.equation, self.options)
        self.cachedResults[value] = r
        return r
    
    def prime(self) -> "Function":
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


    def result(self):
        return self.toEquation().result()

    def toFunction(self) -> Function:
        equation = [self.equation.replace(self.name, str(i)) for i in range(self.start, self.end + 1)]
        return Function("+".join(equation))

    def toEquation(self) -> Equation:
        if self.hasUnknow:
            equation = "+" .join([self.equation.replace(self.name, str(i)) for i in range(self.start, self.end + 1)])
        else:
            equation = str((self.end + 1) - self.start) + "*" + self.equation
        return Equation(equation)


    def __add__(self, other):
        if type(other) != Sum:
            raise BaseException("Cannot sum " + str(self) + " and " + str(other))

        newEquation = None
        if other.start == self.start and other.end == self.end:
            newEquation = Sum(self.start, self.end, self.humanEquation + "+" + other.humanEquation)
        elif other.humanEquation == self.humanEquation:
            if other.start == self.end or other.end == self.start:
                newEquation = Sum(min(self.start, other.start), max(self.end, other.end) + 1, self.humanEquation)
            elif other.start - 1 == self.end or other.end + 1 == self.start:
                newEquation = Sum(min(self.start, other.start), max(self.end, other.end), self.humanEquation)
        else:
            newStart = min(self.start, other.start)
            newEnd = min(self.end, other.end)

            result = None
            if other.end > self.end:
                result = other.end / self.end
            else:
                result = self.end / other.end

            humanEquation = None
            if other.start > self.start:
                humanEquation = other.start / self.start
            else:
                humanEquation = self.start / other.start

            newEquation = Sum(newStart, newEnd, str(humanEquation) + "+" + str(result))
        
        if newEquation != None and newEquation.result() == (self.result() + other.result()):
            newEquation.setOption(self.options)
            return newEquation
        raise BaseException("Cannot sum " + str(self) + " and " + str(other))


    def __radd__(self, other) -> "Equation":
        return self.__add__(other)

class EquaDiff(Function):
    """
    Represents an equation differential function.

    Args:
        equation (str): The equation to be solved.
        name (str, optional): The name of the variable in the equation. Defaults to "x".
        **args: Additional arguments to be passed to the parent class.

    Attributes:
        equation (str): The equation to be solved.
        name (str): The name of the variable in the equation.
        options (dict): Additional options for solving the equation.

    Methods:
        result(value=""): Computes the result of the equation for a given value.

    """

    def __init__(self, equation, name="x", **args):
        super().__init__(equation, name, **args)

    def result(self, value=""):
        """
        Computes the result of the equation for a given value.

        Args:
            value (str, optional): The value to substitute for the variable in the equation. Defaults to "".

        Returns:
            str: The result of the equation with the substituted value.

        """
        a = self.equation.split("+")[0]
        a = a.replace(self.name, value)
        a = resolve(a, self.options)
        b = self.equation.split("+")[1]
        self.equation = "Cexp(" + str(a) + self.name + ") + " + str(-int(b) / int(a))
        print(self.equation)
        return self.toHumanRedeable()