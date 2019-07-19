s = int(input())

l = [s]
for i in range(1000000):
    if s % 2 == 0:
        s /= 2
    else:
        s = 3 * s + 1
    if s in l:
        print(i + 2)
        break
    else:
        l.append(s)
