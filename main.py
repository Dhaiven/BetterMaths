import math
import enum

class Option(enum.Enum):
    DEGREES = 0,
    RADIAN = 1,

def cos(equation: float, type: Option)->float:
    if type == Option.DEGREES:
        equation = math.radians(equation)
    return math.cos(equation)
    
def sin(equation: float, type: Option)->float:
    if type == Option.DEGREES:
        equation = math.radians(equation)
    return math.sin(equation)

class Equation:
    def __init__(self, equation, **args):
        self.equation = self.toHumanRedeable(equation)

        self.options = {}
        print(args)
        self.options["angles"] = args.get("angle", Option.DEGREES)
    
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

    def result(self):
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
                    value = str(func(Equation(value).result()))
                    start -= len(key)
                    break

            return Equation(equation[:start] + str(Equation(value).result()) + equation[end + 1:]).result()
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
