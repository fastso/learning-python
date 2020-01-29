n = int(input())

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        c_ij = 0
        c_ji = 0
        for k in range(1, n + 1):
            temp = str(k)
            if temp[0] == str(i) and temp[-1] == str(j):
                c_ij += 1
            if temp[0] == str(j) and temp[-1] == str(i):
                c_ji += 1
        ans += c_ij * c_ji
print(ans)
