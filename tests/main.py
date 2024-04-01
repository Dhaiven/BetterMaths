import time
from BetterMaths import *
import timeit

def compareEvalAndEquation(equation, nbrOfExecution = 10000):
    if eval(equation) != Equation(equation).result():
        raise Exception("The result of " + equation + " is " + str(eval(equation)) + " for eval but is " + str(Equation(equation).result()) + " for Equation")

    t = timeit.Timer(lambda: eval(equation))
    evalTime = t.timeit(nbrOfExecution)

    t = timeit.Timer(lambda: Equation(equation).result())
    equationTime = t.timeit(nbrOfExecution)

    if equationTime >= evalTime + 0.1:
        raise Exception("The result of " + equation + " take " + str(evalTime) + " with eval and " + str(equationTime) + " with Equation")
    print(equation + " executed in " + str(evalTime - equationTime) + " less eval")
    

compareEvalAndEquation("2**2", 10000)
compareEvalAndEquation("2*4*7", 10000)
compareEvalAndEquation("2**3**4", 10000)

compareEvalAndEquation("7//5", 10000)
compareEvalAndEquation("7//2//3", 10000)
compareEvalAndEquation("2/2", 10000)
compareEvalAndEquation("21/2/3", 10000)
compareEvalAndEquation("7%5", 10000)
compareEvalAndEquation("7%2%3", 10000)

compareEvalAndEquation("2+22", 10000)
compareEvalAndEquation("26+98+70", 10000)
compareEvalAndEquation("+6+9+12", 10000)


"""
Unknow value in equation must be x
"""
def compareEvalAndSum(start, end, equation: str, nbrOfExecution):
    resultEval = 0
    for i in range(start, end + 1):
        resultEval += eval(equation.replace("x", "*" + str(i)))
    if resultEval != Sum(start, end, equation).result():
        raise Exception("The result of " + equation + " is " + str(resultEval) + " for eval but is " + str(Sum(start, end, equation).result()) + " for Sum")

    evalTime = time.time()
    for i in range(nbrOfExecution):
        for j in range(start, end + 1):
            eval(equation.replace("x", "*" + str(i)))
    evalTime = time.time() - evalTime

    sumTime = time.time()
    for i in range(nbrOfExecution):
        Sum(start, end, equation).result()
    sumTime = time.time() - sumTime

    if sumTime >= evalTime:
        raise Exception("The result of " + equation + " take " + str(evalTime) + " with eval and " + str(sumTime) + " with Sum")


compareEvalAndSum(1, 10, "2", 1000)
compareEvalAndSum(1, 10, "2x", 1000)
compareEvalAndSum(1, 10, "2x+7", 1000)