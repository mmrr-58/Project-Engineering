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

matrix = [[1,1,1,100],[1,0,2,125],[0,-1,2,25]]
rowSwap(matrix)
rowSubtracion(matrix)
print(matrix)