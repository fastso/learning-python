h, w, a, b = map(int, input().split())

ans = [[0] * w for i in range(h)]


def count_min(l):
    count0 = l.count(0)
    count1 = l.count(1)
    return min(count0, count1)


if a * 2 > w or b * 2 > h:
    print('No')

for i in range(h):
    for j in range(w):
        if count_min(ans[i]) == a:
            break
        else:
            col = [x[j] for x in ans]
            if count_min(col) == b and len(col) != 1:
                continue
            else:
                ans[i][j] = 1

for i in range(h):
    for j in range(w):
        print(ans[i][j], end='')
    print()
