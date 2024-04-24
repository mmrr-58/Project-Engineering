arrayOne = [[1,1,1], [2,2,2], [1,1,1]]
arrayTwo = [[4,5,1], [1,1,1], [1,1,1]]
for row in arrayOne:
    rowIndex = arrayOne.index(row)
    arrayTwoRowIndex = 0
    for element in arrayOne[rowIndex]:
        result = element * arrayTwo[arrayTwoRowIndex][rowIndex]
        print(result)