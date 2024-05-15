import chemparse
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

reactants = input("Enter the reactants: ")
chemicalsList = reactants.split(" ")
products = input("Enter the products: ")
productList = products.split(" ")
for i in productList:
    chemicalsList.append(i)

if "+" not in reactants or products:
    reactantString = re.sub(" ", " + ", reactants)
    productString = re.sub(" ", " + ", products)
    print("Reaction: ", reactantString, "-->", productString)
else:
    print("Reaction: ", reactants, "-->", products)

totalChemicalsDict = {}
for react in chemicalsList:
    chemicalValues = chemparse.parse_formula(react)
    for key, value in chemicalValues.items():
        if key in totalChemicalsDict:
            totalChemicalsDict[key] += value
        else:
            totalChemicalsDict[key] = value
if "+" in totalChemicalsDict:
    totalChemicalsDict.pop("+")

reaction = {}
x = 1
for molecule in chemicalsList:
    if molecule in productList:
        reaction["molecule" + str(x)] = chemparse.parse_formula(molecule)
        product = reaction["molecule" + str(x)]    
        for key, value in product.items():
            product[key] = -abs(value)
            x+=1
    else:
        reaction["molecule" + str(x)] = chemparse.parse_formula(molecule)   
        x+=1
moleculesList = []
for molecule in reaction.values():
    moleculesList.append(molecule)

matrix = []
row = []
for element in totalChemicalsDict.keys():
    for molecule in moleculesList:
        if element in molecule.keys():
            row.append(molecule[element])
        else:
            row.append(0.0)
    matrix.append(row)
    row = []

# Begin Gaussian Elimination
print("Unordered matrix: ", matrix)
matrix = rowSwap(matrix)
matrix = rowSubtracion(matrix)
print("Matrix after gaussian elimination: ", matrix)

variables = {}
variableNames = ["A", "B", "C", "D", "E", "F", "G", "H"]
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