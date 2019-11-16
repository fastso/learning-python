import itertools
import math

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

seq = list()
for i in range(n):
    seq.append(i)

seq_all = list(itertools.permutations(seq))

ans = 0
for i in seq_all:
    for j in range(n - 1):
        end = i[j + 1]
        start = i[j]
        ans += math.sqrt((a[end][0] - a[start][0]) ** 2 + (a[end][1] - a[start][1]) ** 2)

print(ans / len(seq_all))
