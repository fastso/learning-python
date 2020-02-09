s1, s2 = map(str, input().split())
n1, n2 = map(int, input().split())
u = input()

if u == s1:
    print(n1 - 1, n2)
else:
    print(n1, n2 - 1)
