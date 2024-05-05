import chemparse
import re

# Get the reaction from the user
reactants = input("Enter the reactants: ")
chemicalsList = reactants.split(" ")
products = input("Enter the products: ")
productList = products.split(" ")
for i in productList:
    chemicalsList.append(i)

# Print reaction
if "+" not in reactants or products:
    reactantString = re.sub(" ", " + ", reactants)
    productString = re.sub(" ", " + ", products)
    print("Reaction: ", reactantString, "-->", productString)
else:
    print("Reaction: ", reactants, "-->", products)

# Create a dictionary of all the values of the reaction
totalChemicalsDict = {}
for react in chemicalsList:
    print(productList)
    print(react)
    if react in productList:
        print("Enters the if")
        chemicalValues = chemparse.parse_formula(react)
        for key, value in chemicalValues.items():
            if key in totalChemicalsDict:
                totalChemicalsDict[key] -= value
            else:
                totalChemicalsDict[key] = -abs(value)
    else:
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
    reaction["molecule" + str(x)] = chemparse.parse_formula(molecule)
    x+=1
moleculesList = []
for molecule in reaction.values():
    moleculesList.append(molecule)

# Converting to a matrix
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
print(matrix)

for row in matrix:
    if row[0] == 1.0:
        i, j = matrix.index(row) , 0
        matrix[i], matrix[j] = matrix[j], matrix[i]
    else:
        continue
print(matrix)
