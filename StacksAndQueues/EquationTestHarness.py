from StacksAndQueues import EquationSolver
from StacksAndQueues import Exceptions

try:
    sol = EquationSolver.EquationSolver()
    equation = str(input("Enter an equation."))
    result = sol.solve(equation)
    print("The answer is ", result, ".")
except Exceptions.StackUnderflowError as e:
    print(e.message)
