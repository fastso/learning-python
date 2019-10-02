n = int(input())
s = [input() for i in range(n)]

s_s = set(s)

ans = ''
ans_c = 0
for i in s_s:
    if s.count(i) > ans_c:
        ans_c = s.count(i)
        ans = i
print(ans)
