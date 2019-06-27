N = format(int(input()), "04b")
print(N)
print(N.count("1"))
for n, b in zip((8, 4, 2, 1), N):
    if b == "1":
        print(n)
