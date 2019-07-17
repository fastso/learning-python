import sys

l, r = map(int, input().split())

ans = 2019
for i in range(l, r):
    for j in range(i+1, r + 1):
        temp = i * j % 2019
        if temp < ans:
            ans = temp
        if ans == 0:
            print(0)
            sys.exit()
print(ans)
