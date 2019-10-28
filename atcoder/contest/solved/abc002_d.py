n, m = map(int, input().split())
ls = [list(map(int, input().split())) for i in range(m)]

ans = 1
# なり得る全組合せに対し
for bit in range(2 ** n):
    flag = True
    group = list()
    for i in range(n):
        # 組合せの対象 & groupの既存メンバーと関係あり であればgroupに追加
        if (1 << i) & bit:
            for member in group:
                if not [member, i + 1] in ls:
                    flag = False
            group.append(i + 1)

    if flag:
        ans = max(len(group), ans)

print(ans)
