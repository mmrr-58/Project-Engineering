equationList = []
equation = "2x + 3y - 30z = 10"
equationList.append(equation)
equation = equation.split()
row = []
for value in equation:
    if value.isnumeric():
        row.append(int(value))
        continue
    for char in value:
        print(char)
        if char.isdigit():
            row.append(int(char))
print(row)
