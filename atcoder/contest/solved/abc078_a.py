a, b = map(str, input().split())

if int(a, 16) > int(b, 16):
    print('>')
elif int(a, 16) < int(b, 16):
    print('<')
else:
    print('=')
