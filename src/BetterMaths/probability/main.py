from BetterMaths.main import Expression
import math

class Event:
    def __init__(self, probability) -> None:
        self.probability = probability

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
        return coeficient * (self.p ** k) * ((1 - self.p) ** (self.n - k))
    
    def toExpression(self, k):
        """
        Converts the binomial distribution to an expression.

        Args:
            k (int): The number of successes.

        Returns:
            Expression: The expression representing the binomial distribution.
        """
        n = str(self.n)
        p = str(self.p)
        return Expression(f"({n}!)/({k}!*({n}-{k})!)*{p}**{k}*(1-{p})**({n}-{k})")

    def expectedValue(self):
        """
        Calculates the expected value of the binomial distribution.

        Returns:
            float: The expected value of the binomial distribution.
        """
        return self.n * self.p
    
    def variance(self):
        """
        Calculates the variance of the binomial distribution.

        Returns:
            float: The variance of the binomial distribution.
        """
        return self.expectedValue() * (1 - self.p)
    
    def standardDeviation(self):
        """
        Calculates the standard variation of the binomial distribution.
                   
        Returns:
            float: The standard variation of the binomial distribution.
        """
        return math.sqrt(self.variance())
    
    def confidenceInterval(self,confidence:float) -> tuple:
        """
        Calculates the interval for the confidence.

        Returns:
            tuple: The confidence interval (a,b).
        """
        if not 0<=confidence<=100:
            raise ValueError("The confidence level must be between 0 and 100%")
        under=0
        under_total=0
        a=((100-confidence)/2)/100
        while under_total <= a:
            under_total+=self.result(under)
            under+=1
            if under>self.n:
                raise ValueError("Confidence too high!")
        top=under-1
        b=confidence/100+a
        while under_total<b:
            under_total+=self.result(top)
            top+=1
        return (under-1, top)

__all__ = [
  "Event",
  "Binomial"
]