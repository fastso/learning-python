a, b = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


i_min = min(a, b)
i_max = max(a, b)

yaku_list = make_divisors(i_min)

kouyaku_list = []
for i in yaku_list:
    if i_max % i == 0:
        kouyaku_list.append(i)

for i in range(len(kouyaku_list) - 1):
    if kouyaku_list[i] == 1:
        continue
    if kouyaku_list[i] != -1:
        for j in range(i + 1, len(kouyaku_list)):
            if kouyaku_list[j] % kouyaku_list[i] == 0:
                kouyaku_list[j] = -1

print(len(kouyaku_list) - kouyaku_list.count(-1))
