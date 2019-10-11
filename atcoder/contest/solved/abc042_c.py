n, k = map(int, input().split())
d = list(map(str, input().split()))

ans = n
flag = True
while flag:
    flag = False
    for i in d:
        if str(ans).count(i) != 0:
            flag = True
            ans += 1
            break
print(ans)
