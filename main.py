class EquaDiff:
    def __init__(self, yPrime, unknow) -> None:
        self.yPrime: str = yPrime
        self.unknow = unknow
    
    def toGoodEquation(self, equation: str):
        replacables = {
            "++": "+",
            "+-": "-",
            "--": "-",
            "--": "+",
        }
        for nbr in range(0, 10):
            replacables[str(nbr) + "("] = str(nbr) + "*("
        
        for froms, to in replacables.items():
            equation = equation.replace(froms, to)
        return equation

    def equation(self, equation: str):
        equation = self.toGoodEquation(equation)
        result = 0
        if "(" in equation:
            start = len(equation)
            end = 0
            for i in range(len(equation)):
                if equation[i] == "(" and i < start:
                    start = i
                if equation[i] == ")" and i > end:
                    end = i
            value = ""
            for i in range(start + 1, end):
                value += equation[i]
            return self.equation(equation[:start] + str(self.equation(value)) + equation[end + 1:])
        else:
            result += float(eval(equation))
        return result
    
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

diff = EquaDiff("2y+2", "y")
print(diff.equation("2*7(1+-2)"))
