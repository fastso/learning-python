s = input()
ans = len(s)

if ans % 2 == 1:
    ans -= 1
else:
    ans -= 2

while ans > 0:
    if s[0:(ans//2)] == s[(ans//2):ans]:
        print(ans)
        exit()
    ans -= 2
