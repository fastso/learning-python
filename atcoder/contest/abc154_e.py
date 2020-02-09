import itertools

n = int(input())
k = int(input())

l = list(str(n))
for i in range(len(l)):
    l[i] = int(l[i])

comb_list = list(itertools.combinations(range(len(l)), k))

ans = 0
for comb in comb_list:
    # 最大桁を含む場合
    if comb[0] != 0:
        temp = 9 ** len(comb)
        ans += temp
    else:
        renzoku_flag = 0
        for i in range(len(comb) - 1):
            if comb[i+1] - comb[i] != 1:
                renzoku_flag = i
        for i in range(len(comb)):
            temp = 9 ** (len(comb) - 1)
            # 最大桁を含む
            if i > renzoku_flag:
                ans += temp
                temp //= 9
                continue
            if i == len(comb) - 1:
                ans += l[comb[i]]
            else:
                ans += (l[comb[i]]-1) * temp
            temp //= 9
    print(comb)
    print(ans)

print(ans)
