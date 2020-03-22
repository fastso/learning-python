n = int(input())
a = list(map(int, input().split()))

a_dict = dict()
for i in a:
    if i not in a_dict:
        a_dict[i] = 1
    else:
        a_dict[i] += 1

total = 0
for k, v in a_dict.items():
    if v > 1:
        total += int(v * (v - 1) / 2)

for i in a:
    print(total - a_dict[i] + 1)
