n, a, b = map(int, input().split())

ans = 0
for i in range(n):
    s, d = map(str, input().split())
    if s == 'East':
        if a <= int(d) <= b:
            ans += int(d)
        elif int(d) < a:
            ans += a
        else:
            ans += b
    else:
        if a <= int(d) <= b:
            ans -= int(d)
        elif int(d) < a:
            ans -= a
        else:
            ans -= b

if ans > 0:
    print('East ' + str(ans))
elif ans < 0:
    print('West ' + str(ans * -1))
else:
    print(0)
