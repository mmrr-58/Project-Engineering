# Import Library
import chemparse
import re

# reactant variables
react = input("Enter the reactants: ")
reactantList = react.split()
reactListNumber = 0

# product variables
product = input("Enter the produts: ")
productList = product.split()
productListNumber = 0
print(productList)

# Prints the full reaction 
reactantString = re.sub(" ", " + ", react)
productString = re.sub(" ", " + ", product)
print("Reaction: ", reactantString, "-->", productString)

# For loop adds all the reactants to a dictionary
for x in reactantList:
    reactantDict = chemparse.parse_formula(reactantList[reactListNumber])
    print(reactantDict)
    reactListNumber = reactListNumber + 1

