matrix1 = []
matrix2 = []
resultMatrix = []

def matrixAdd():
    for x in range(0 , len(matrix1)):
        print(x)
        result = matrix1[x] + matrix2[x]
        resultMatrix.append(result)

def matrixSub():
    for x in range(0 , len(matrix1)):
        print(x)
        result = matrix1[x] - matrix2[x]
        resultMatrix.append(result)

operationChoice = int(input("Choose the operation to be performed \n 1.Addition \n 2. Substraction \n 3. Constant Multiplication \n 4.Matrix Multiplication"))

print("Input the values as they appear in rows, starting with a1")
x = 0
while x < 9:    
    number = int(input("Input number: "))
    matrix1.append(number)    
    x = x + 1
print(matrix1)
print("Input the values as they appear in rows, starting with a1")
x = 0
while x < 9:    
    number = int(input("Input number: "))
    matrix2.append(number)    
    x = x + 1
print(matrix2)

if operationChoice == 1:
    matrixAdd()
elif operationChoice == 2:
    matrixSub()
else:
    print("Needs to be developed")
print(resultMatrix)