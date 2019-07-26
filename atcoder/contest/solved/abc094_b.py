n, m, x = map(int, input().split())
a = list(map(int, input().split()))

goal1 = 0
goal2 = 0

for i in range(x + 1, n):
    if i in a:
        goal1 += 1

for i in range(1, x):
    if i in a:
        goal2 += 1

print(min(goal1, goal2))
