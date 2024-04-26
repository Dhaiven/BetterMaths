import BetterMaths.main as bm
import math

class Sequence(bm.Function):
    """
    Represents a mathematical sequence.

    Args / Attributes:
    - initial_term (int): The initial term of the sequence.
    - expression (str): The expression used to generate the terms of the sequence (Un+1, example: 2*Un).
    - type (int, optional): The type of the sequence. Defaults to 0.

    Methods:
    - isArithmetic(): Checks if the sequence is arithmetic.
    - isGeometric(): Checks if the sequence is geometric.
    - sequence(n): Returns the values of the n first terms of the sequence.
    - variation(n): Calculates the variation of the sequence.
    - artithmeticSequence(n, k): Generates an arithmetic sequence.
    - geometricSequence(n, k): Generates a geometric sequence.
    - term(n): Returns the nth term of the sequence.
    - arithmeticSum(p, n): Calculates the sum of an arithmetic sequence.
    - geometricSUm(p, n): Calculates the sum of a geometric sequence.
    - infLimit(): Returns the limit of the sequence when n tends to infinity

    """

    def __init__(self, initial_term, expression, type=0):
        super().__init__(expression, "Un")

        self.initial_term = initial_term
        if self.isArithmetic() != False:
            self.type = 1
        elif self.isGeometric() != False:
            self.type = 2
        else:
            self.type = type
    
    def isArithmetic(self) -> bool:
        """
        Checks if the sequence is arithmetic.
        """
        for separator in ["+", "-"]:
            if separator in self.expression:
                for part in self.expression.split(separator):
                    if part != "Un" and not bm.isNumber(part):
                        return False
                return True
        return False

    def isGeometric(self) -> bool:
        """
        Checks if the sequence is geometric.
        """
        newExpression = self.expression
        if "*" in newExpression:
            newExpression = newExpression.replace("*", "")
        newExpression = newExpression.replace("Un", "")
        return bm.isNumber(newExpression)

    def reason(self) -> float:
        result = 0
        if self.isArithmetic():
            for separator in ["+", "-"]:
                if separator in self.expression:
                    for part in self.expression.split(separator):
                        if part != "Un":
                            result = self.__resolve__(str(result) + separator + part)
        elif self.isGeometric():
            result = 1
            for part in self.expression.split("*"):
                if part != "Un":
                    result *= self.__resolve__(part)
        return result


    def sequence(self,n) -> "list[int]":
        """
        Return the values of the n first terms of the sequence.

        Args:
        - n (int): Numbers of terms.

        Returns:
        - list: The custom sequence as a list of integers.
        """
        sequence = [eval(self.expression.replace('Un', str(self.initial_term)))]
        for i in range(n):
            term = eval(self.expression.replace('Un', str(sequence[-1])))
            sequence.append(term)
        return sequence
    
    def variation(self) -> str:
        """
        Calculates the variation of the sequence. It can be deacreasing, increasing or constant.
        Only for arithmetics and geometrics.

        Returns:
        - str: The variation of the sequence.
        """

        result = "constant"
        reason = self.reason()
        if self.isArithmetic():
            if reason > 0:
                result = "increasing"
            elif reason < 0:
                result = "decreasing"
        elif self.isGeometric():
            if reason > 1:
                result = "increasing"
            elif reason < 1:
                result = "decreasing"
        return result

    def artithmeticSequence(self, n: int , k: int) -> "list[int]":
        """
        Generates an arithmetic sequence starting from the initial term of the sequence.

        Args:
        - n (int): The first term of the sequence (ex: 17 for U17).
        - k (int): The number of additional terms to generate after the initial term.

        Returns:
        - list[int]: The arithmetic sequence generated.

        Raises:
        - ValueError: If the sequence is not arithmetic.

        """
        if self.type != 1:
            raise ValueError("The sequence is not arithmetic!")
        dif = self.reason()
        sequence = [self.initial_term + n * dif]
        for i in range(k):
            term = sequence[-1] + dif
            sequence.append(term)
        return sequence
    
    def geometricSequence(self, n: int, k: int) -> "list[int]":
        """
        Generates a geometric sequence starting from the initial term of the sequence.

        Args:
        - n (int): The first term of the sequence (ex: 17 for U17).
        - k (int): The number of additional terms to generate after the initial term.

        Returns:
        - list[int]: A list containing the generated terms of the geometric sequence.

        Raises:
        - ValueError: If the sequence is not geometric.

        """
        if self.type != 2:
            raise ValueError("The sequence is not geometric!")
        ratio = self.reason()
        sequence = [self.initial_term * ratio ** n]
        for i in range(k):
            term = sequence[-1] * ratio
            sequence.append(term)
        return sequence
    
    def term(self, n):
        """
        Returns the nth term of the sequence.

        Parameters:
        - n (int): The position of the term in the sequence.

        Returns:
        - The nth term of the sequence.

        """
        if self.type == 1:
            return self.artithmeticSequence(n, 0)[-1]
        elif self.type == 2:
            return self.geometricSequence(n, 0)[-1]
        return self.sequence(n)[-1]
    
    def sum(self, p: int, n: int) -> float:
        """
        Returns the sum of the terms from p to n.

        Parameters:
        - p (int): The postition of the first term in the sequence.
        - n (int): The position of the second term in the sequence (must be greater than p).

        Returns:
        - The sum of the sequence.
        """
        if p < 0:
            raise ValueError("p must be greater or equal to 0!")
        elif n < p:
            raise ValueError("n must be grater than p!")
        
        if self.isArithmetic():
            return (n - p + 1) * ((self.term(p) + self.term(n)) / 2)
        elif self.isGeometric():
            ratio = self.reason()
            return self.term(p) * ((1 - ratio ** (n - p + 1)) / (1 - ratio))
        raise ValueError("Sequance must be arithmetic or geometric")


    def infLimit(self) -> float:
        """
        Returns the limit of the sequence when n tends to infinity (for now, only do smth with arithmetic and geometric).

        Returns:
        - The limit of the sequence (if it exists, else None).
        """
        if self.isArithmetic():
            if self.reason() > 0:
                return math.inf
            else:
                return -math.inf
        elif self.isGeometric():
            reason = self.reason()
            if reason > 1:
                if self.initial_term > 0:
                    return math.inf
                else:
                    return -math.inf
            elif -1 < reason < 1:
                return 0
        return None
    
    def __repr__(self):
        return f"Sequence({self.initial_term}, {self.expression}, {self.type})"

all = [
    "Sequence"
]