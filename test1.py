# Define variables needed
matrix1 = []
matrix2 = []
resultMatrix = []

# Function to convert a single list a 2D matrix
# Need to add support for 2x2 matrices
def matrixConversion(matrix):
    row = []
    convertedMatrix = []
    for value in matrix:
        row.append(value)
        if len(row) == 3:
            convertedMatrix.append(row)
            row = []
    return convertedMatrix

# Function for adding 2 matrices
def matrixAdd():
    for x in range(0 , len(matrix1)):
        result = matrix1[x] + matrix2[x]
        resultMatrix.append(result)

# Function for subtracting 2 matrices
def matrixSub():
    for x in range(0 , len(matrix1)):
        result = matrix1[x] - matrix2[x]
        resultMatrix.append(result)

# Function for multiplying with a coefficient
def scalarMult():
    for x in range(0, len(matrix1)):
        result = coefficient * matrix1[x]
        resultMatrix.append(result)

# Function for Matrix multiplication
def matrixMult():
    m1 = matrixConversion(matrix1)
    m2 = matrixConversion(matrix2)
    print(m1)
    print(m2)
    row = 0
    item = row
    transList = []
    x = 0 
    while row < 2:
        print(row)
        for value in m1[row]:
            transNumber = value * m2[x][item]
            x = x + 1
            transList.append(transNumber)
        number = sum(transList)
        resultMatrix.append(number)
        row = row + 1

# Define operation and size
operationChoice = int(input("Choose the operation to be performed \n 1. Addition \n 2. Substraction \n 3. Scalar Multiplication \n 4. Matrix Multiplication \n"))
matrixSizeChoice = int(input("Choose the dimension of the matrices: \n 1. 2x2 \n 2. 3x3 \n"))
print("Input the values as they appear in rows, starting with a1")
if matrixSizeChoice == 1:
    x = 5
elif matrixSizeChoice == 2:
    x = 0
else:  
    print("Select a valid option")

# Creatre the two matrices on which to perform operations
y = x
while x < 9:    
    number = int(input("Input number: "))
    matrix1.append(number)    
    x = x + 1
if operationChoice == 3:
    coefficient = int(input("Input coefficient: "))
else:
    print("Input the values as they appear in rows, starting with a1")
    while y < 9:    
        number = int(input("Input number: "))
        matrix2.append(number)    
        y = y + 1

if operationChoice == 1:
    matrixAdd()
elif operationChoice == 2:
    matrixSub()
elif operationChoice == 3:
    scalarMult()
elif operationChoice == 4:
    matrixConversion(matrix1)
    matrixConversion(matrix2)
    matrixMult()
else:
    print("Needs to be developed")

print(matrixConversion(resultMatrix))