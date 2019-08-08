s = list(input())
t = list(input())

s.sort()
t.sort()

i = 0
j = len(t) - 1
while True:
    if s[i] < t[j]:
        print('Yes')
        exit()
    elif s[i] > t[j]:
        print('No')
        exit()
    else:
        i += 1
        j -= 1
        if j < 0:
            print('No')
            exit()
        if i >= len(s):
            print('Yes')
            exit()
