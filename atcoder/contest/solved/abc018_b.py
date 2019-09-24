s = list(input())
n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    temp = s[l:r+1]
    for j in range(len(temp)):
        s[l + j] = temp[-(j + 1)]
print(''.join(s))
