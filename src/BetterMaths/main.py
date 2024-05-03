import math, enum, decimal
from typing import SupportsIndex

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
    expression = Expression(calcul, args=options)
    return expression.result()


def factorial(number: int) -> decimal.Decimal:
    if type(number) != int:
        raise TypeError("'float' object cannot be interpreted as an integer")
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    result = decimal.Decimal(number)
    for i in range(2, number):
        result = result * decimal.Decimal(i)
    return result


def isNumber(number):
    for i in number:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True

functions = {
    "abs": lambda value, options: abs(value),
    "floor": lambda value, options: math.floor(value),
    "ceil": lambda value, options: math.ceil(value),
    "sqrt": lambda value, options: math.sqrt(value),
    "exp": lambda value, options: math.exp(value),
    "log": lambda value, options: math.log(value, 10),
    "ln": lambda value, options: math.log(value, math.e),
    "cos": lambda value, options: cos(value, options["angles"]),
    "sin": lambda value, options: sin(value, options["angles"]),
    "tan": lambda value, options: tan(value, options["angles"]),
    "acos": lambda value, options: acos(value, options["angles"]),
    "asin": lambda value, options: asin(value, options["angles"]),
    "atan": lambda value, options: atan(value, options["angles"]),
    "atan2": lambda value, options: atan2(float(str(value).split(",")[0]), float(str(value).split(",")[1]), options["angles"]),
    "cosh": lambda value, options: math.cosh(value),
    "sinh": lambda value, options: math.sinh(value),
    "tanh": lambda value, options: math.tanh(value),
    "lcm": lambda value, options: math.lcm(*list(map(round, map(float, str(value).split(","))))),
    "gcd": lambda value, options: math.gcd(*list(map(round, map(float, str(value).split(","))))),
    "gcf": lambda value, options: math.gcd(*list(map(round, map(float, str(value).split(","))))),
    "min": lambda value, options: min(str(value).split(",")),
    "max": lambda value, options: max(str(value).split(",")),
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

class Expression:
    """
    Represents a mathematical expression.

    Attributes:
        expression (str): The expression in program-readable format.
        humanExpression (str): The expression in human-readable format.
        options (dict): Options for evaluating the expression.

    Methods:
        __init__(self, expression: str, **args): Initializes a new Expression object.
        setOption(self, options: dict): Sets the options for the expression.
        toHumanRedeable(self): Converts the expression to human-readable format.
        toProgramRedeable(self) -> str: Converts the expression to program-readable format.
        result(self) -> float: Evaluates the expression and returns the result.
        split(self, separator) -> list[Expression]: Splits the expression into multiple expressions based on the separator.
        __transformOther__(self, other) -> tuple[str, dict[Option]]: Transforms the other expression or value into a tuple of expression and options.
        __add__(self, other) -> Expression: Adds the other expression or value to the current expression.
        __radd__(self, other) -> Expression: Adds the current expression to the other expression or value.
        __sub__(self, other) -> Expression: Subtracts the other expression or value from the current expression.
        __rsub__(self, other) -> Expression: Subtracts the current expression from the other expression or value.
        __mul__(self, other) -> Expression: Multiplies the current expression with the other expression or value.
        __rmul__(self, other) -> Expression: Multiplies the other expression or value with the current expression.
        __pow__(self, other, mod: int = None) -> Expression: Raises the current expression to the power of the other expression or value.
        __rpow__(self, other, mod: int = None) -> Expression: Raises the other expression or value to the power of the current expression.
        __floordiv__(self, other) -> Expression: Performs floor division of the current expression by the other expression or value.
        __rfloordiv__(self, other) -> Expression: Performs floor division of the other expression or value by the current expression.
        __truediv__(self, other) -> Expression: Performs true division of the current expression by the other expression or value.
        __rtruediv__(self, other) -> Expression: Performs true division of the other expression or value by the current expression.
        __mod__(self, other) -> Expression: Performs modulo operation of the current expression by the other expression or value.
        __rmod__(self, other) -> Expression: Performs modulo operation of the other expression or value by the current expression.
        __divmod__(self, other) -> tuple[int, int]: Performs divmod operation of the current expression by the other expression or value.
        __rdivmod__(self, other) -> tuple[int, int]: Performs divmod operation of the other expression or value by the current expression.
        __neg__(self) -> Expression: Negates the current expression.
        __eq__(self, other) -> bool: Checks if the current expression is equal to the other expression or value.
        __ne__(self, other) -> bool: Checks if the current expression is not equal to the other expression or value.
        __lt__(self, other) -> bool: Checks if the current expression is less than the other expression or value.
        __le__(self, other) -> bool: Checks if the current expression is less than or equal to the other expression or value.
    """
    
    def __init__(self, expression: str, **args):
        for froms in humanReadable:
            if froms in expression: # Just for optimisation
                expression = expression.replace(froms, humanReadable.get(froms))
        #If we have +number at the beginning
        while expression.startswith("+"):
            expression = expression[1:]
        self.humanExpression = expression
        
        self.expression = self.__toProgramRedeable__(self.humanExpression)
        self.options = {}
        if "args" in args and len(args.get("args")) != 0:
            self.options = args.get("args")
        else:
            self.options["angles"] = args.get("angles", Option.DEGREES)


    def setOption(self, options: dict):
        self.options = options

    def toHumanRedeable(self) -> str:
        return self.humanExpression
    
    def toProgramRedeable(self) -> str:
        return self.expression
    
    def __toProgramRedeable__(self, expression: str) -> str:
        programExpression = ""
        lenght = len(expression)
        for i in range(lenght):
            character = expression[i]
            if not character in ["+", "-", "/", "%", "*"] and not isNumber(character):
                if character == "^":
                    e += "**"
                    continue

                if i > 0:
                    last = expression[i - 1]
                else:
                    last = expression[i]
                if i < lenght - 1:
                    next = expression[i + 1]
                else:
                    next = expression[i]
                if character != ")" and character != "!":
                    if isNumber(last):
                        programExpression += "*"
                elif next == "(":
                    programExpression += character + "*"
                    continue
                if character != "(" and isNumber(next):
                    programExpression += character + "*"
                    continue
            programExpression += character
        if "atan*2*" in programExpression:
            programExpression = programExpression.replace("atan*2*", "atan2")
        return programExpression

    def result(self) -> float:
        try:
            return self.__resolve__(self.expression)
        except OverflowError:
            return math.inf
        
    
    def sum(self, expression: str) -> float:
        values = expression.split("+")
        result = 0
        for value in values:
            result += self.__resolve__(value)
        return result
    
    def sub(self, expression: str):
        return eval(expression)
    
    def pow(self, expression: str) -> float:
        values = expression.split("*")
        result = 1
        for value in values:
            result *= self.__resolve__(value)
        return result
    
    def power(self, expression: str) -> float:
        values = expression.split("**")
        result = 1
        while len(values) > 0:
            result = self.__resolve__(values.pop()) ** result
        return result
    
    def divide(self, expression: str) -> float:
        values = expression.split("/")
        result = self.__resolve__(values.pop(0))
        for value in values:
            result /= self.__resolve__(value)
        return result
    
    def floordivide(self, expression: str) -> float:
        values = expression.split("//")
        result = self.__resolve__(values.pop(0))
        for value in values:
            result //= self.__resolve__(value)
        return result
    
    def modulo(self, expression: str) -> float:
        values = expression.split("%")
        result = self.__resolve__(values.pop(0))
        for value in values:
            result %= self.__resolve__(value)
        return result

    def __resolve__(self, expression: str) -> float:
        if expression == "":
            return 0
        if "(" in expression:
            start = expression.find("(")
            nbrCanBePassed = 1
            end = -1
            for i in range(start + 1, len(expression)):
                element = expression[i]
                if element == "(":
                    nbrCanBePassed += 1
                elif element == ")":
                    nbrCanBePassed -= 1
                    if nbrCanBePassed == 0:
                        end = i
                        break

            inParenthese = expression[start + 1:end]
            if "," in inParenthese:
                value = ",".join([str(self.__resolve__(v)) for v in inParenthese.split(",")])
            else:
                value = self.__resolve__(inParenthese)
            
            for key in range(minNameLenght, maxNameLenght):
                func = functions.get(expression[start - key:start])
                if func != None:
                    value = func(value, self.options)
                    start -= key
                    break

            return self.__resolve__(expression[:start] + str(value) + expression[end + 1:])
        #Factorial
        start = expression.find("!")
        if start != -1:
            mustBeFactorial = ""
            for i in range(start - 1, -1, -1):
                if expression[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    mustBeFactorial = expression[i] + mustBeFactorial
                else:
                    break
            left = self.__resolve__(expression[:start - len(mustBeFactorial)])
            right = self.__resolve__(expression[start + 1:])
            return left + factorial(int(mustBeFactorial)) + right
        elif "+" in expression:
            return self.sum(expression)
        elif "-" in expression:
            return self.sub(expression)
        elif "//" in expression:
            return self.floordivide(expression)
        elif "/" in expression:
            return self.divide(expression)
        elif "%" in expression:
            return self.modulo(expression)
        elif "**" in expression:
            return self.power(expression)
        elif "*" in expression:
            return self.pow(expression)

        if "pi" in expression:
            expression = expression.replace("pi", str(math.pi))
        if "tau" in expression:
            expression = expression.replace("tau", str(math.tau))
        if "e" in expression:
            expression = expression.replace("e", str(math.e))
        return decimal.Decimal(expression)
    

    def split(self, separator) -> "list[Expression]":
        splitedExpressions = self.humanExpression.split(separator)
        result = []
        for splitedExpression in splitedExpressions:
            newExpression = Expression(splitedExpression)
            newExpression.setOption(self.options)
            result.append(newExpression)
        return result
    

    def __transformOther__(self, other) -> "tuple[str, dict[Option]]":
        otherExpression = ""
        options = self.options
        if type(other) != Expression:
            otherExpression = str(other)
        else:
            otherExpression = other.humanExpression
            for key, value in other.options.items():
                options[key] = value
        return otherExpression, options


    def __add__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression(self.humanExpression + "+" + otherExpression)
        new.setOption(options)
        return new


    def __radd__(self, other) -> "Expression":
        return self.__add__(other)


    def __sub__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)
        
        new = Expression(self.humanExpression + "-(" + otherExpression + ")")
        new.setOption(options)
        return new


    def __rsub__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)
        
        new = Expression(otherExpression + "-(" + self.humanExpression + ")")
        new.setOption(options)
        return new


    def __mul__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + otherExpression + ")*(" + self.humanExpression + ")")
        new.setOption(options)
        return new


    def __rmul__(self, other) -> "Expression":
        return self.__mul__(other)


    def __pow__(self, other, mod: int = None) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + self.humanExpression + ")**(" + otherExpression + ")")
        new.setOption(options)
        return new
    

    def __rpow__(self, other, mod: int = None) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + otherExpression + ")**(" + self.humanExpression + ")")
        new.setOption(options)
        return new


    def __floordiv__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + self.humanExpression + ")//(" + otherExpression + ")")
        new.setOption(options)
        return new


    def __rfloordiv__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + otherExpression + ")//(" + self.humanExpression + ")")
        new.setOption(options)
        return new


    def __truediv__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + self.humanExpression + ")/(" + otherExpression + ")")
        new.setOption(options)
        return new


    def __rtruediv__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + otherExpression + ")/(" + self.humanExpression + ")")
        new.setOption(options)
        return new


    def __mod__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + self.humanExpression + ")%(" + otherExpression + ")")
        new.setOption(options)
        return new


    def __rmod__(self, other) -> "Expression":
        otherExpression, options = self.__transformOther__(other)

        new = Expression("(" + otherExpression + ")%(" + self.humanExpression + ")")
        new.setOption(options)
        return new
    

    def __transformOtherResult__(self, other) -> float:
        if type(other) != Expression:
            otherResult = float(other)
        else:
            otherResult = other.result()
        return otherResult


    def __divmod__(self, other) -> 'tuple[int, int]':
        result = self.result()
        otherResult = self.__transformOtherResult__(other)
        
        return (result // otherResult, result % otherResult)
    

    def __rdivmod__(self, other) -> 'tuple[int, int]':
        result = self.result()
        otherResult = self.__transformOtherResult__(other)

        return (otherResult // result, otherResult % result)


    def __neg__(self) -> "Expression":
        new = Expression("-(" + self.humanExpression + ")")
        new.setOption(self.options)
        return new


    def __eq__(self, other) -> bool:
        return self.result() == self.__transformOtherResult__(other)


    def __ne__(self, other) -> bool:
        return self.result() != self.__transformOtherResult__(other)


    def __lt__(self, other) -> bool:
        return self.result() < self.__transformOtherResult__(other)


    def __le__(self, other) -> bool:
        return self.result() <= self.__transformOtherResult__(other)


    def __gt__(self, other) -> bool:
        return self.result() > self.__transformOtherResult__(other)


    def __ge__(self, other) -> bool:
        return self.result() >= self.__transformOtherResult__(other)
    

    def __float__(self) -> float:
        return float(self.result())


    def __int__(self) -> int:
        return int(self.result())


    def __abs__(self) -> int:
        return abs(self.result())
    

    def __round__(self, ndigits: SupportsIndex = None) -> int:
        return round(self.result(), ndigits)
    

    def __ceil__(self) -> int:
        return math.ceil(self.result())


    def __floor__(self) -> int:
        return math.floor(self.result())


    def __str__(self) -> str:
        return self.humanExpression



class UnknowExpression(Expression):
    def __init__(self, expression, name = "x", **args):
        self.name = name
        super().__init__(expression, **args)

        self.cachedResults = {}
        self.hasUnknow = self.expression.find(name) != -1


    def result(self, value: float) -> float:
        value = str(value)
        if value in self.cachedResults:
            return self.cachedResults[value]
        
        result = self.__resolve__(self.expression.replace(self.name, value) if self.hasUnknow else self.expression)
        self.cachedResults[value] = result
        return result



class Sum(UnknowExpression):
    def __init__(self, start, end, expression, unknow = "x"):
        self.start = start
        self.end = end
        
        super().__init__(expression, unknow)

        if self.hasUnknow:
            self.expression = "+".join([self.expression.replace(self.name, str(i)) for i in range(self.start, self.end + 1)])
        else:
            self.expression = str((self.end + 1) - self.start) + "*" + self.expression
    
    def result(self) -> float:
        return self.toExpression().result()

    def toExpression(self) -> Expression:
        return Expression(self.expression)


    def __add__(self, other):
        if type(other) != Sum:
            raise BaseException("Cannot sum " + str(self) + " and " + str(other))

        newExpression = None
        if other.start == self.start and other.end == self.end:
            newExpression = Sum(self.start, self.end, self.humanExpression + "+" + other.humanExpression)
        elif other.humanExpression == self.humanExpression:
            if other.start == self.end or other.end == self.start:
                newExpression = Sum(min(self.start, other.start), max(self.end, other.end) + 1, self.humanExpression)
            elif other.start - 1 == self.end or other.end + 1 == self.start:
                newExpression = Sum(min(self.start, other.start), max(self.end, other.end), self.humanExpression)
        else:
            newStart = min(self.start, other.start)
            newEnd = min(self.end, other.end)

            result = None
            if other.end > self.end:
                result = other.end / self.end
            else:
                result = self.end / other.end

            humanExpression = None
            if other.start > self.start:
                humanExpression = other.start / self.start
            else:
                humanExpression = self.start / other.start

            newExpression = Sum(newStart, newEnd, str(humanExpression) + "+" + str(result))
        
        if newExpression != None and newExpression.result() == (self.result() + other.result()):
            newExpression.setOption(self.options)
            return newExpression
        raise BaseException("Cannot sum " + str(self) + " and " + str(other))


    def __radd__(self, other) -> "Expression":
        return self.__add__(other)



class Prod(UnknowExpression):
    def __init__(self, start, end, expression, unknow = "x"):
        self.start = start
        self.end = end

        super().__init__(expression, unknow)

        if self.hasUnknow:
            self.expression = "*".join(["(" + self.expression.replace(self.name, str(i)) + ")" for i in range(self.start, self.end + 1)])
        else:
            self.expression =  "(" + self.expression + ")**" + str((self.end + 1) - self.start)

    def result(self) -> float:
        try:
            return self.__resolve__(self.expression)
        except OverflowError:
            return math.inf

    def toExpression(self) -> Expression:
        return Expression(self.expression)


class Equation(UnknowExpression):
    def __init__(self, equation: str, unknow: str = "x"):
        super().__init__(equation, unknow)

        for s in ["<=", ">=", "<", ">", "="]:
            if s in self.expression:
                self.separator = s
                break

    
    def isGood(self, value: str) -> bool:
        split = self.toProgramRedeable().replace(self.name, str(value)).split(self.separator)

        match (self.separator):
            case "<=":
                return resolve(split[0]) <= resolve(split[1])
            case ">=":
                return resolve(split[0]) >= resolve(split[1])
            case "<":
                return resolve(split[0]) < resolve(split[1])
            case ">":
                return resolve(split[0]) > resolve(split[1])
            case "=":
                return resolve(split[0]) == resolve(split[1])
    
    def __getOcuurences__(self, start) -> str:
        end = len(self.toProgramRedeable())
        for i in range(start + 1, len(self.toProgramRedeable())):
            if not self.expression[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                end = i
                break

        return self.toProgramRedeable()[start+1:end]
    
    def __getPowOcuurences__(self, start) -> str:
        end = 0
        for i in range(start - 1, -1, -1):
            if not self.expression[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*"]:
                end = i
                break

        return self.toProgramRedeable()[end:start-1]

    def find(self) -> float:
        left, right = self.expression.split(self.separator)
        lst = [left, right]
        while left != self.name:
            element = lst.pop()
            if "+" in element:
                occurences = self.__getOcuurences__(element.find("+"))
                left = left.replace("+" + occurences, "")
                right += "-(" + occurences + ")"
            if self.name in element:
                occurences = self.__getPowOcuurences__(self.expression.find(self.name))
                left = left.replace(occurences + "*", "")
                right = "(" + right + ")/(" + occurences + ")"
        return resolve(right)
    

"""
ADD:
- better name for UnknowExpression (maybe EquationBase)
- try because i think there are many bugs
- Sum(1, 100, "2x") equals to 2 * Sum(1, 100, "x") (more faster) (remove constant from sum)
"""
""" TEST
s = Sum(1, 100, "x")
se = Sum(1, 100, "2x")

start = time.time()
for i in range(10000):
    2 * s.result()
print(time.time() - start)

start = time.time()
for i in range(10000):
    se.result()
print(time.time() - start)
"""

factorial(-1.1)