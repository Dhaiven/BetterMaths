import math

class Equation:
    def __init__(self, equation):
        self.equation = self.toGoodEquation(equation)
    
    def toGoodEquation(self, equation: str):
        replacables = {
            "++": "+",
            "+-": "-",
            "--": "-",
            "--": "+",
            "^": "**",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
        
        for froms, to in replacables.items():
            equation = equation.replace(froms, to)
        return equation
    
    def result(self):
        equation = self.equation
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
                "exp": math.exp
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

diff = Equation("exp(27)")
print(diff.result())
print(diff)
print(eval("2**3"))
