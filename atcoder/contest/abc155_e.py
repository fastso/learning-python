a = list(input())

pay = list()
add = 0
for i in reversed(range(len(a))):
    temp = int(a[i]) + add
    if temp < 6:
        pay.append(temp)
        add = 0
    else:
        pay.append(0)
        add = 1
if add:
    pay.append(add)

ans = 0
bigger = True
if len(pay) != len(a):
    ans += 1
    for i in range(len(a)):
        if pay[-i - 2] != 0 and pay[-i - 1] == 0:
            ans += 1
            ans += pay[-i - 2]
        elif pay[-i - 2] != 0:
            ans += pay[-i - 2]
        else:
            if int(a[i]):
                ans += 9 - int(a[i])
else:
    for i in range(len(a)):
        if pay[-i - 1] != 0 and pay[-i] == 0:
            ans += 1
            ans += pay[-i - 1]
        elif pay[-i - 1] != 0:
            ans += pay[-i - 1]
        else:
            if int(a[i]):
                ans += 9 - int(a[i])
        if

print(ans)
