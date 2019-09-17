n = int(input())
s = input()

ans = 0
for i in range(n):
    if i + ans*2 > n:
        break
    for j in range(ans, n - i // 2):
        print(s[i:j+1], end='=')
        print(s[i + j+1:i + j + j])
        if s[i:j+1] == s[i + j+1:i + j + j]:
            ans = max(ans, j-i+1)
            print(ans)
            if i + ans*2 > n:
                break
print(ans)
