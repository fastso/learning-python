n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

ball = [0] * (n + 1)
for i in reversed(range(1, n + 1)):
    if a[i] == 1:
        if sum(ball[i * 2::i]) % 2 == 0:
            ball[i] = 1
        else:
            ball[i] = 0
    else:
        if sum(ball[i * 2::i]) % 2 == 0:
            ball[i] = 0
        else:
            ball[i] = 1

ans = []
for i in range(1, n + 1):
    if ball[i] == 1:
        ans.append(i)

print(len(ans))
print(*ans)
