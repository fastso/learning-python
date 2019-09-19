n = int(input())
s = list(input())

ans = ['b']
if ans == s:
    print(0)
    exit()
for i in range(1, n):
    if i % 3 == 0:
        ans.append('b')
        ans.insert(0, 'b')
    elif i % 3 == 1:
        ans.append('c')
        ans.insert(0, 'a')
    else:
        ans.append('a')
        ans.insert(0, 'c')
    if ans == s:
        print(i)
        exit()
print(-1)
