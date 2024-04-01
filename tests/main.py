import time
from BetterMaths import Equation

def compareEvualAndEquation(equation, nbrOfExecution):
    if eval(equation) != Equation(equation).result():
        raise Exception("The result of " + equation + " is " + str(eval(equation)) + " for eval but is " + str(Equation(equation).result()) + " for Equation")

    evalTime = time.time()
    for i in range(nbrOfExecution):
        eval(equation)
    evalTime = time.time() - evalTime

    equationTime = time.time()
    t = Equation(equation)
    for i in range(nbrOfExecution):
        t.result()
    equationTime = time.time() - equationTime

    if equationTime >= evalTime:
        raise Exception("The result of " + equation + " take " + str(evalTime) + " with eval and " + str(equationTime) + " with Equation")
    


compareEvualAndEquation("2**2", 100000)
compareEvualAndEquation("2+2", 100000)