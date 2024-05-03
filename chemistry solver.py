import chemparse
import re

react = input("Enter the reactants: ")
reactantList = react.split()
i = 0

product = input("Enter the produts: ")
productList = product.split()
productListNumber = 0


if "+" not in react or product:
    reactantString = re.sub(" ", " + ", react)
    productString = re.sub(" ", " + ", product)
    print("Reaction: ", reactantString, "-->", productString)
else:
    print("Reaction: ", react, "-->", product)
reaction = react + " " + product
print(reaction)
reactantDict = {}
for react in reactantList:
    reactantValues = chemparse.parse_formula(react)
    for key, value in reactantValues.items():
        if key in reactantDict:
            reactantDict[key] += value
        else:
            reactantDict[key] = value
if "+" in reactantDict:
    reactantDict.pop("+")

productDict = {}
for product in productList:
    productValues = chemparse.parse_formula(product)
    for key, value in productValues.items():
        if key in productDict:
            productDict[key] += value
        else:
            productDict[key] = value
if "+" in productDict:
    productDict.pop("+")
print(productDict)

reactionMatrix = []
