n, m = map(int, input().split())

cost = []
key = []
for i in range(m):
    a, b = map(int, input().split())
    cost.append(a)
    key.append(list(map(int, input().split())))

ans = float('inf')

def subset(cost, key, keyset, ans_temp):
    keyset2 = keyset.copy()
    keyset2 |= set(key[0])
    if len(keyset2) > len(keyset):
        ans_temp += cost[0]
        keyset = keyset2

    global ans
    if len(cost) == 1 and ans_temp != -1 and len(keyset) == n:
        ans = min(ans, ans_temp)
        return
    elif len(keyset) == n:
        ans = min(ans, ans_temp)
        return
    else:
        for i in range(1, len(cost)):
            subset(cost[i:], key[i:], keyset, ans_temp)


for i in range(m):
    ans_temp = -1
    key_temp = set()
    # for j in range(i, m):
    #     key_temp2 = key_temp.copy()
    #     key_temp2 |= set(key[j])
    #     if len(key_temp2) > len(key_temp):
    #         ans_temp += cost[j]
    #         key_temp = key_temp2
    #     if len(key_temp) == n:
    #         break
    subset(cost, key, key_temp, 0)

    if ans_temp != -1 and len(key_temp) == n:
        ans = min(ans, ans_temp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
