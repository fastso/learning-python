s = input()

ans = ""
for i in s:
    if int(i)==1 or int(i)==9:
        ans = ans + str(10-int(i))
    else:
        ans = ans + i

print(ans)
