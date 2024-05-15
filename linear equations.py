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

print("Enter coefficients of the equation one at a time. \nIf there is no value for the variable, add a 0 \nExample: 2x + 3z = 10 --> 2 , 0(y) , 3 , 10\nWhen finished with the equation, enter 'newline'. When finished with the system, enter 'newline' followed by 'end'")
coefficient = input("Enter coefficient: ")
matrix = []
while coefficient != "end":
    row = []
    while coefficient != "newline":
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

variables = {}
variableNames = ["x", "y", "z"]
row = matrix[0]
for i in range(len(row)):
    feira = variableNames[i]
    variables[str(i)] = variableNames[i]

whatever = []
moreWhatever = []
for row in range(len(matrix)-1, -1,-1):
    thisRow = matrix[row]
    for number in range(len(thisRow)):
        juniCortes = matrix[row][number]
        if juniCortes != 0.0:
            if str(number) in variables.keys():
                var = variables[str(number)]
                maje = str(juniCortes) + var
                whatever.append(maje)
                whatever.append("+")
    if len(whatever) < 1:
        continue
    whatever.pop()
    moreWhatever.append(whatever)
    whatever = []
for item in moreWhatever:
    print(str(item), "= 0")
print("Assigning a value to", feira, "will yield a balanced equation")
