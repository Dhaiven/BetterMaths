import time
from BetterMaths import Equation

def compareEvalAndEquation(equation, nbrOfExecution):
    if eval(equation) != Equation(equation).result():
        raise Exception("The result of " + equation + " is " + str(eval(equation)) + " for eval but is " + str(Equation(equation).result()) + " for Equation")

    evalTime = time.time()
    for i in range(nbrOfExecution):
        eval(equation)
    evalTime = time.time() - evalTime

    equationTime = time.time()
    for i in range(nbrOfExecution):
        Equation(equation).result()
    equationTime = time.time() - equationTime

    if equationTime >= evalTime:
        raise Exception("The result of " + equation + " take " + str(evalTime) + " with eval and " + str(equationTime) + " with Equation")
    

compareEvalAndEquation("2**2", 10000)
compareEvalAndEquation("2**3**4", 10000)
compareEvalAndEquation("2*2", 10000)
compareEvalAndEquation("2*4*7", 10000)

compareEvalAndEquation("7//5", 10000)
compareEvalAndEquation("7//2//3", 10000)
compareEvalAndEquation("2/2", 10000)
compareEvalAndEquation("21/2/3", 10000)
compareEvalAndEquation("7%5", 10000)
compareEvalAndEquation("7%2%3", 10000)

compareEvalAndEquation("2+2", 10000)
compareEvalAndEquation("2+2+7", 10000)