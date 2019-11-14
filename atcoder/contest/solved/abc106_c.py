a = list(input())
k = int(input())

for i in a:
    if i != '1':
        print(i)
        break
    k -= 1
    if k == 0:
        print('1')
        break
