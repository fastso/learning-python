s = input()

alpha = ['A', 'B', 'C', 'D', 'E', 'F']
ans = []
for i in alpha:
    ans.append(s.count(i))

print(*ans)
