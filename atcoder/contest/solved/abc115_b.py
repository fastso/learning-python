n = int(input())
a = [int(input()) for i in range(n)]

a.sort()
print(sum(a)-int(a[-1]/2))
