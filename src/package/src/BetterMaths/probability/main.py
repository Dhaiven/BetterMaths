from BetterMaths.main import Equation
import math

class Binomial:
    """
    Represents a binomial distribution.

    Attributes:
        n (int): The number of trials.
        p (float): The probability of success in each trial.
    """

    def __init__(self, n, p) -> None:
        self.n = n
        self.p = p
    
    def result(self, k):
        """
        Calculates the probability of getting exactly k successes.

        Args:
            k (int): The number of successes.

        Returns:
            float: The probability of getting exactly k successes.
        """
        coeficient = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        return coeficient * self.p ** k * (1 - self.p) ** (self.n - k)
    
    def toEquation(self, k):
        """
        Converts the binomial distribution to an equation.

        Args:
            k (int): The number of successes.

        Returns:
            Equation: The equation representing the binomial distribution.
        """
        n = str(self.n)
        p = str(self.p)
        return Equation(f"({n}!)/({k}!*({n}-{k})!)*{p}**{k}*(1-{p})**({n}-{k})")


__all__ = [
  "Binomial"
]