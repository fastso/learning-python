n = int(input())
a = list(map(int, input().split()))

ans = 0
while True:
    for i in range(len(a)):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            print(ans)
            exit()
    ans += 1
