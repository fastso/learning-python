s = input()
k = int(input())

ans = set()
if len(s) < k:
    print(0)
else:
    for i in range(len(s) - k + 1):
        ans.add(s[i:i + k])
    print(len(ans))
