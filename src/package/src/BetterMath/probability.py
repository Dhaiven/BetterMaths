from main import Equation
import math

class Binomial:
    def __init__(self, n, p) -> None:
        self.n = n
        self.p = p
    
    def result(self, k):
        coeficient = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        return coeficient * self.p ** k * (1 - self.p) ** (self.n - k)
    
    def toEquation(self, k):
        n = str(self.n)
        p = str(self.p)
        return Equation(f"({n}!)/({k}!*({n}-{k})!)*{p}**{k}*(1-{p})**({n}-{k})")