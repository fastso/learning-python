n = int(input())

for i in range(2 ** n):
    temp = list()
    for j in range(n):
        if (i >> j) & 1:
            temp.append(j)
    print(temp)
