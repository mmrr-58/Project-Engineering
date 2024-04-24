listOne = [[1,2,4],[-2,1,5],[1,1,1]]
listTwo = [[4,0,3],[0,1,2],[1,2,2]]
result = []
intermediate = []
for rowOne in listOne:
    listOneRowIndex = listOne.index(rowOne)
    for rowTwo in listTwo:
        listTwoRowIndex = listTwo.index(rowTwo)
        x = 0
        for columnOne in listOne[listOneRowIndex]:
            res = listOne[listOneRowIndex][x] * listTwo[x][listTwoRowIndex]
            intermediate.append(res)
            x = x + 1
        result.append(sum(intermediate))
        intermediate = []
print(result)
        
        