h = int(input())

h_copy = h
count = 0
while h_copy > 1:
    h_copy //= 2
    count += 1

ans = 0
for i in range(count + 1):
    ans += pow(2, i)
print(ans)
