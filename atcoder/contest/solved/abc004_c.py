n = int(input())
a = [1, 2, 3, 4, 5, 6]

n %= 30

for i in range(n):
    temp_i = i % 5
    temp = a[temp_i]
    a[temp_i] = a[temp_i + 1]
    a[temp_i + 1] = temp
print(''.join(map(str, a)))
