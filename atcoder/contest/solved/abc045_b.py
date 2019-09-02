a = list(input())
b = list(input())
c = list(input())

next = 'a'
while True:
    if next == 'a':
        if a == []:
            print('A')
            break
        else:
            next = a.pop(0)
    elif next == 'b':
        if b == []:
            print('B')
            break
        else:
            next = b.pop(0)
    if next == 'c':
        if c == []:
            print('C')
            break
        else:
            next = c.pop(0)
