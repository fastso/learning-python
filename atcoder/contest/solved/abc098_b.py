n = int(input())
s = input()

# a-z
az = [chr(i) for i in range(97, 97 + 26)]

ans = 0
for i in range(1, n):
    count = 0
    for j in az:
        if s[i:n].count(j) != 0 and s[:i].count(j) != 0:
            count += 1
    ans = max(ans, count)
print(ans)
