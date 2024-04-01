class Sequence:
    def __init__(self, initial_term, expression):
        self.initial_term = initial_term
        self.expression = expression
    
    def sequence(self, n) -> "list[int]":
        """
        Return the values of the n first terms of the sequence.

        Args:
            expression (str): The expression defining the sequence.
            n (int): The number of terms to generate.

        Returns:
            list: The custom sequence as a list of integers.
        """
        sequence = [eval(self.expression.replace('n', str(self.initial_term)))]
        for i in range(n):
            term = eval(self.expression.replace('n', str(sequence[-1])))
            sequence.append(term)
        return sequence
    
    def variation(self) -> str:
        """
        Calculates the variation of the sequence. It can be deacreasing, increasing or constant.

        Returns:
            str: The variation of the sequence.
        """
        sequence = self.sequence(1)
        variation = 'constant'
        for i in range(1, len(sequence)):
            if sequence[i] > sequence[i - 1]:
                variation = 'increasing'
            elif sequence[i] < sequence[i - 1]:
                variation = 'decreasing'
        return variation
    
    def isArithmetic(self) -> bool:
        """
        Checks if the sequence is arithmetic.

        Returns:
            bool: True if the sequence is arithmetic, False otherwise.
        """
        sequence = self.sequence(2)
        difference = sequence[1] - sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i - 1] != difference:
                return False
        return True
    
    def isGeometric(self) -> bool:
        """
        Checks if the sequence is geometric.

        Returns:
            bool: True if the sequence is geometric, False otherwise.
        """
        sequence = self.sequence(2)
        ratio = sequence[1] / sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] / sequence[i - 1] != ratio:
                return False
        return True
        

caca=Sequence(23, "(n+2)*2")
print(caca.sequence(5))
print(caca.variation())
print(caca.isArithmetic())
print(caca.isGeometric())