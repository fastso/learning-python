n, k = map(int, input().split())
a = list(map(int, input().split()))


def kitai(i: int) -> int:
    if i % 2:
        return ((1 + i) * (i // 2) + (i // 2) + 1) / i
    else:
        return ((1 + i) * (i // 2)) / i


kitai_dict = dict()
kitai_list = list()

for i in range(n):
    if a[i] in kitai_dict:
        kitai_list.append(kitai_dict[a[i]])
    else:
        kitai_dict[a[i]] = kitai(a[i])
        kitai_list.append(kitai_dict[a[i]])

current_sum = sum(kitai_list[:k])
ans = current_sum
for i in range(k, n):
    current_sum += kitai_list[i]
    current_sum -= kitai_list[i - k]
    ans = max(ans, current_sum)

print(ans)
