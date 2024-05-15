import re
matrix = [[1, 1, -1, -2], [0, 1.0, -1.0, -3.0], [0.0, 0.0, 1.0, 2.0]]

solutionEquations = []
equation = []
variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w" "x", "y", "z", " "]
for row in range(0, len(matrix)):
    thisRow = matrix[row]
    for number in range(len(thisRow)):
        thisNumber = thisRow[number]
        if thisNumber != 0.0:
            if number == len(thisRow)-1:
                result = "= "+ str(thisNumber)
                equation.append(result)
            else: 
                value = str(thisNumber) + variables[number]
                equation.append(value+"+")
    if "+" in equation[-2]:
        equation[-2] = re.sub(" + ", " ", value)
    solutionEquations.append(equation)
    equation = []
print(solutionEquations)
for equations in solutionEquations:
    print(" ".join(equations))