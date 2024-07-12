from BetterMaths import *
import timeit

def compareEvalAndExpression(expression, nbrOfExecution = 10000):
    if eval(expression) != Expression(expression).result():
        raise Exception("The result of " + expression + " is " + str(eval(expression)) + " for eval but is " + str(Expression(expression).result()) + " for Expression")

    t = timeit.Timer(lambda: eval(expression))
    evalTime = t.timeit(nbrOfExecution)

    t = timeit.Timer(lambda: Expression(expression).result())
    expressionTime = t.timeit(nbrOfExecution)

    if expressionTime >= evalTime:
        raise Exception("The result of " + expression + " take " + str(evalTime) + " with eval and " + str(expressionTime) + " with Expression")
    print(expression + " executed in " + str(evalTime - expressionTime) + " less eval")
    

compareEvalAndExpression("2*2", 10000)
compareEvalAndExpression("2*4*7", 10000)
compareEvalAndExpression("2**3**4", 10000)

compareEvalAndExpression("7//5", 10000)
compareEvalAndExpression("7//2//3", 10000)
compareEvalAndExpression("2/2", 10000)
compareEvalAndExpression("21/2/3", 10000)
compareEvalAndExpression("7%5", 10000)
compareEvalAndExpression("7%2%3", 10000)

compareEvalAndExpression("2+22", 10000)
compareEvalAndExpression("26+98+70", 10000)
compareEvalAndExpression("+6+9+12", 10000)


"""
Unknow value in expression must be x
"""
def compareEvalAndSum(start, end, expression: str, nbrOfExecution):
    resultEval = 0
    for i in range(start, end + 1):
        resultEval += eval(expression.replace("x", "*" + str(i)))
    if resultEval != Sum(start, end, expression).result():
        raise Exception("The result of " + expression + " is " + str(resultEval) + " for eval but is " + str(Sum(start, end, expression).result()) + " for Sum")

    def executeEval(start, end, expression: str, nbrOfExecution):
        for i in range(nbrOfExecution):
            for j in range(start, end + 1):
                eval(expression.replace("x", "*" + str(i)))

    t = timeit.Timer(lambda: executeEval(start, end, expression, nbrOfExecution))
    evalTime = t.timeit(1)

    t = timeit.Timer(lambda: Sum(start, end, expression).result())
    sumTime = t.timeit(nbrOfExecution)

    if sumTime >= evalTime:
        raise Exception("The result of " + expression + " take " + str(evalTime) + " with eval and " + str(sumTime) + " with Sum")
    print("Sum of " + expression + " executed in " + str(evalTime - sumTime) + " less eval")

compareEvalAndSum(1, 10, "2", 1000)
compareEvalAndSum(1, 10, "2x", 1000)
compareEvalAndSum(1, 10, "2x+7", 1000)



"""
Unknow value in expression must be x
"""
def compareEvalAndProd(start, end, expression: str, nbrOfExecution):
    resultEval = 1
    for i in range(start, end + 1):
        resultEval *= eval(expression.replace("x", "*" + str(i)))
    if resultEval != Prod(start, end, expression).result():
        raise Exception("The result of " + expression + " is " + str(resultEval) + " for eval but is " + str(Prod(start, end, expression).result()) + " for Prod")

    def executeEval(start, end, expression: str, nbrOfExecution):
        for i in range(nbrOfExecution):
            for j in range(start, end + 1):
                eval(expression.replace("x", "*" + str(i)))

    t = timeit.Timer(lambda: executeEval(start, end, expression, nbrOfExecution))
    evalTime = t.timeit(1)

    t = timeit.Timer(lambda: Prod(start, end, expression).result())
    sumTime = t.timeit(nbrOfExecution)

    if sumTime >= evalTime:
        raise Exception("The result of " + expression + " take " + str(evalTime) + " with eval and " + str(sumTime) + " with Prod")
    print("Prod of " + expression + " executed in " + str(evalTime - sumTime) + " less eval")


compareEvalAndProd(1, 10, "2", 1000)
compareEvalAndProd(1, 10, "2x", 1000)
compareEvalAndProd(1, 10, "2x+7", 1000)

"""
2*2 executed in 0.037685700000110955 less eval
2*4*7 executed in 0.0531063999997059 less eval
2**3**4 executed in 0.03533580000021175 less eval
7//5 executed in 0.04377870000007533 less eval
7//2//3 executed in 0.034638600000107544 less eval
2/2 executed in 0.04186089999984688 less eval
21/2/3 executed in 0.037326300000131596 less eval
7%5 executed in 0.04273270000157936 less eval
7%2%3 executed in 0.0356952000011006 less eval
2+22 executed in 0.04329280000001745 less eval
26+98+70 executed in 0.03275039999971341 less eval
+6+9+12 executed in 0.0409098999998605 less eval
Sum of 2 executed in 0.06397280000055616 less eval
Sum of 2x executed in 0.04951950000031502 less eval
Sum of 2x+7 executed in 0.03976440000042203 less eval
Prod of 2 executed in 0.06536979999964387 less eval
Prod of 2x executed in 0.0322189000007711 less eval
Prod of 2x+7 executed in 0.02540469999985362 less eval
"""