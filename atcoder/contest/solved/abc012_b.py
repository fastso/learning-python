t = int(input())

a = t % 60
b = t // 60 % 60
c = t // 60 // 60

if a < 10:
    a = '0' + str(a)
else:
    a = str(a)

if b < 10:
    b = '0' + str(b)
else:
    b = str(b)

if c < 10:
    c = '0' + str(c)
else:
    c = str(c)
print(c + ':' + b + ':' + a)
