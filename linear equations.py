import re

def rowSwap(matrix):
    x = 0
    flag = 0
    for row in matrix:
        if row[x] == 1.0:
            i, j = matrix.index(row) , x
            matrix[i], matrix[j] = matrix[j], matrix[i]
            x+=1 
            flag = 1
    if flag != 1:
        row = []
        for value in matrix[0]:
            number = matrix[0][0]
            number = value/number
            row.append(number)
        matrix[0] = row
        rowSwap(matrix)
    return matrix

def rowSubtracion(matrix):
    for i in range(0, len(matrix)-1):
        previousRow = matrix[i]
        for j in range(i+1, len(matrix)):
            row = matrix[j]
            intermediate = []
            for k in range(len(previousRow)):
                value = row[i]
                value = previousRow[k]*value
                intermediate.append(value)
            for l in range(0, len(row)):
                row[l] = row[l]-intermediate[l]
            value = row[i+1]
            if value == 0:
                continue
            for m in range(i+1, len(row)):
                row[m] = row[m]/value
    return matrix

print("Enter coefficients of the equation one at a time. \nIf there is no value for the variable, add a 0 \nExample: 2x + 3z = 10 --> 2 , 0(y) , 3 , 10\nWhen finished with the equation, enter 'r'. When finished with the system, enter 'r' followed by 'e'")
coefficient = input("Enter coefficient: ")
matrix = []
while coefficient != "e":
    row = []
    while coefficient != "r":
        if coefficient.isnumeric:
            row.append(int(coefficient))
        else:
            print("Error: coefficient is not numeric")
        coefficient = input("Enter coefficient: ")
    matrix.append(row)
    coefficient = input("Enter coefficient: ")

print("Unordered matrix" , matrix)
matrix = rowSubtracion(rowSwap(matrix))
print(matrix)

solutionEquations = []
equation = []
variables = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
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
                equation.append(value+" +")
        elif number == len(thisRow)-1:
            result = "= "+ str(thisNumber)
            equation.append(result)
        else:
            continue
    if "+" in equation[-2]:
        equation[-2] = re.sub(" + ", " ", value)
    solutionEquations.append(equation)
    equation = []
for equations in solutionEquations:
    print(" ".join(equations))

print("Substituing", variables[number], "into the previous equations will yield solutions to the system of equations")