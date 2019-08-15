s = input()

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
for c in ascii_lowercase:
    if s.count(c) == 0:
        print(c)
        exit()
print('None')
