import math

n = int(input())
a = list(map(int, input().split()))

ans_sum = 0
ans_num = 0
for i in range(n):
    if a[i] == 0:
        continue
    else:
        ans_sum += a[i]
        ans_num += 1
print(math.ceil(ans_sum / ans_num))
