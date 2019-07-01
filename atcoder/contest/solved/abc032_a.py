import fractions

a = int(input())
b = int(input())
n = int(input())

c = a * b // fractions.gcd(a, b)

i = 1
while c * i < n:
    i += 1

print(c*i)
