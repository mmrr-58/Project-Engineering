''' Here is an example of how we can add all the parts of a string

myString = input("String: ")
myList = myString.split()

print(myList)
print(myList[2])

result = int(myList[2]) + int(myList[4])
print(result)

'''
'''
# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))
 
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This returns None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)
'''
''' Example of how you can add the values of dictionaries
dic1 = {"name" : 3 , "age": 5 , "girlfriend": 1, "money": 2}
dic2 = {"name" : 1 , "age": 1 , "girlfriend": 1, "status": 4}
dic3 = { }
for key in dic1.keys():
    if (key in dic2.keys()):
         dic2[key] = dic2[key]+ dic1[key]
    else:
        dic2[key]= dic1[key]
print(dic2)
'''
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

# Prints the full reaction 
reactantString = re.sub(" ", " + ", react)
productString = re.sub(" ", " + ", product)
print("Reaction: ", reactantString, "-->", productString)

# For loop adds all the reactants to a dictionary
reactDicList = []
for x in reactantList:
    reactantDict = chemparse.parse_formula(reactantList[reactListNumber])
    reactDicList.append(reactantDict)
    reactListNumber = reactListNumber + 1

print(type(reactDicList[0]))
