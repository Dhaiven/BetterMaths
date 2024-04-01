class Sequence:
    
    
    def __init__(self, initial_term, expression, type=0):
        self.initial_term = initial_term
        self.expression = expression
        if self.isArithmetic() != False:
            self.type=1
        elif self.isGeometric() !=False:
            self.type=2
        else:
            self.type=type
    
    def isArithmetic(self):
        """
        Checks if the sequence is arithmetic.

        Returns:
            If false:
                bool
            If true:
                tuple: (True, difference)
        """
        sequence = self.sequence(2)
        difference = sequence[1] - sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] - sequence[i - 1] != difference:
                return False
        return (True, difference)

    def isGeometric(self):
        """
        Checks if the sequence is geometric.

        Returns:
            If false:
                bool
            If true:
                tuple: (True, ratio)
        """
        sequence = self.sequence(2)
        ratio = sequence[1] / sequence[0]
        for i in range(1, len(sequence)):
            if sequence[i] / sequence[i - 1] != ratio:
                return False
        return (True, ratio)


    
    def sequence(self,n) -> "list[int]":
        """
        Return the values of the n first terms of the sequence.

        Args:
            n (int): The start of the sequence (default 0).

        Returns:
            list: The custom sequence as a list of integers.
        """
        sequence = [eval(self.expression.replace('n', str(self.initial_term)))]
        for i in range(n):
            term = eval(self.expression.replace('n', str(sequence[-1])))
            sequence.append(term)
        return sequence
    
    def variation(self,n=0) -> str:
        """
        Calculates the variation of the sequence. It can be deacreasing, increasing or constant.
        Calculate from n to n+1000 (default 0).

        Returns:
            str: The variation of the sequence.
        """
        sequence = self.sequence(1000)
        variation = 'constant'
        for i in range(1, len(sequence)):
            if sequence[i] > sequence[i - 1]:
                variation = 'increasing'
            elif sequence[i] < sequence[i - 1]:
                variation = 'decreasing'
        return variation

    def artithmeticSequence(self, n: int , k: int) -> "list[int]":
            if self.type != 1:
                raise ValueError("The sequence is not arithmetic!")
            dif=self.isArithmetic()[1]
            sequence = [self.initial_term+n*dif]
            for i in range(k):
                term = sequence[-1]+dif
                sequence.append(term)
            return sequence
    
    def geometricSequence(self, n: int, k: int) -> "list[int]":
        if self.type != 2:
            raise ValueError("The sequence is not geometric!")
        ratio=self.isGeometric()[1]
        sequence = [self.initial_term*ratio**n]
        for i in range(k):
            term = sequence[-1]*ratio
            sequence.append(term)
        return sequence