# Import Library
import chemparse
import re

# reactant variables
react = input("Enter the reactants: ")
reactantList = react.split()
i = 0

# product variables
product = input("Enter the produts: ")
productList = product.split()
productListNumber = 0

# Prints the full reaction
if "+" not in react or product:
    reactantString = re.sub(" ", " + ", react)
    productString = re.sub(" ", " + ", product)
    print("Reaction: ", reactantString, "-->", productString)
else:
    print("Reaction: ", react, "-->", product)

# For loop adds all the reactants to a dictionary
reactantDict = {}
# Iterate over each reactant in the reactantList
for react in reactantList:
    reactantValues = chemparse.parse_formula(react)
    # Update the reactantDict with the parsed formula
    for key, value in reactantValues.items():
        if key in reactantDict:
            reactantDict[key] += value
        else:
            reactantDict[key] = value
if "+" in reactantDict:
    reactantDict.pop("+")
print(reactantDict)

# For loop adds all the reactants to a dictionary
productDict = {}
# Iterate over each reactant in the reactantList
for product in productList:
    productValues = chemparse.parse_formula(product)
    # Update the reactantDict with the parsed formula
    for key, value in productValues.items():
        if key in productDict:
            productDict[key] += value
        else:
            productDict[key] = value

if "+" in productDict:
    productDict.pop("+")
print(productDict)

