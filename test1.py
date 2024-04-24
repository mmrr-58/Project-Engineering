listOne = [[1,2,3],[5,5,6],[7,8,9]]
listTwo = [[1,2,3],[4,5,6],[7,8,9]]
result = []
x = 0
for rowOne in listOne:
    listOneRowIndex = listOne.index(rowOne)
    for rowTwo in listTwo:
        listTwoRowIndex = listTwo.index(rowTwo)
        for columnOne in listOne[listOneRowIndex]:
            result = listOne[listOneRowIndex][x] * listTwo[x][listTwoRowIndex]
            print(result)
            x = x + 1
        break
    break
        
        