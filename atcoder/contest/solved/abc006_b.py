n = int(input())
mod = 10007
a1 = 0
a2 = 0
a3 = 1

if n == 1 or n == 2:
    print(0)
elif n == 3:
    print(1)
else:
    for i in range(n - 3):
        a4 = a1 + a2 + a3
        if a4 > mod:
            a4 %= mod
        a1 = a2
        a2 = a3
        a3 = a4
    print(a3)
