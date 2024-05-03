# Define variables needed
matrix1 = []
matrix2 = []
resultMatrix = []

# Function to convert a single list to a 2D matrix
def matrixConversion(matrix):
    row = []
    convertedMatrix = []
    for value in matrix:
        row.append(value)
        if len(matrix) == 4:
            if len(row) == 2:
                convertedMatrix.append(row)
                row = []   
        if len(matrix) == 9:
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

# Function for matrix multiplication
def matrixMult():
    m1 = matrixConversion(matrix1)
    m2 = matrixConversion(matrix2)
    intermediate = []
    for rowOne in m1:
        listOneRowIndex = m1.index(rowOne)
        for rowTwo in m2:
            listTwoRowIndex = m2.index(rowTwo)
            x = 0
            for columnOne in m1[listOneRowIndex]:
                res = m1[listOneRowIndex][x] * m2[x][listTwoRowIndex]
                intermediate.append(res)
                x = x + 1
            resultMatrix.append(sum(intermediate))
            intermediate = []

        
    
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

# Performs operations
if operationChoice == 1:
    matrixAdd()
elif operationChoice == 2:
    matrixSub()
elif operationChoice == 3:
    scalarMult()
elif operationChoice == 4:
    matrixMult()
else:
    print("Needs to be developed")

# Prints a 2D array that contains the resultant matrix
print(matrixConversion(resultMatrix))