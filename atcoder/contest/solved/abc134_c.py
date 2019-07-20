n = int(input())
l = [int(input()) for i in range(n)]

ls = l[:]
ls.sort()

for i in l:
    print(ls[-1] if i != ls[-1] else ls[-2])
