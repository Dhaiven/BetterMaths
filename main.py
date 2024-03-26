class EquaDiff:
    def __init__(self, yPrime, unknow) -> None:
        self.yPrime: str = yPrime
        self.unknow = unknow
    
    def sum(self, equation: str):
        values = equation.split("+", 1)
        return self.equation(values[0]) + self.equation(values[1])
    
    def soustraction(self, equation: str):
        values = equation.split("-", 1)
        if values[0] == "":
            v = values[1].split("-", 1)
            if len(v) == 1:
                return -float(values[1])
            return -self.equation(v[0]) - self.equation(v[1])
        return self.equation(values[0]) + self.equation("-" + values[1])

    def multiplie(self, equation: str):
        values = equation.split("*", 1)
        return self.equation(values[0]) * self.equation(values[1])
    
    def divide(self, equation: str):
        values = equation.split("/", 1)
        return self.equation(values[0]) / self.equation(values[1])
    
    def toGoodEquation(self, equation: str):
        i = 0
        good = ""
        while i < len(equation):
            element = equation[i]
            if i < len(equation) - 1 and element + equation[i + 1] == "--":
                good += "+"
                i += 1
            else:
                good += element
            i += 1
        return good

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
        if "+" in equation:
            result += self.sum(equation)
        elif "-" in equation:
            result += self.soustraction(equation)
        elif "*" in equation:
            result += self.multiplie(equation)
        elif "/" in equation:
            result += self.divide(equation)
        else:
            result += float(equation)
        return result
    
    def result(self, value = ""):
        if type(value) != str:
            value = str(value)
        if value != "":
            value = "*" + value
        #equation = self.yPrime.replace(self.unknow, str(value))
        a = self.yPrime.split("+")[0]
        a = a.replace(self.unknow, value)
        a = self.multiplie(a)
        b = self.yPrime.split("+")[1]
        return "Cexp(" + str(a) + self.unknow + ") + " + str(-int(b) / int(a))

diff = EquaDiff("2y+2", "y")
print(diff.equation("-2--7"))
print(diff.equation("2*7(1+2)"))
