n, p = map(int, input().split())
s = input()

max_len = 2 * 100000

d = dict()

for i in range(1, max_len):
    temp = p * i
    if temp > int(s):
        break
    d[str(temp)] = 1

ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        temp = str(int(s[i:j]))
        if temp in d:
            ans += 1
print(ans)
