currentlist = []
for w in input1:
    currentlist.append(w)
    if len(currentlist) == 3:
        matrix1.append(currentlist)
        currentlist = []
print(matrix1)

 row = []
    for w in interList:
        row.append(w)
        if len(row) == 3:
            matrix1.append(row)
            row = []