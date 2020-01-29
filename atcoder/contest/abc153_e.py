h, n = map(int, input().split())
ab = list()
for i in range(n):
    a, b = map(int, input().split())
    l_temp = list()
    l_temp.append(a)
    l_temp.append(b)
    l_temp.append(a / b)
    ab.append(l_temp)
ab.sort(key=lambda x: (x[2], x[1]), reverse=True)

magic = 0
for i in range(n):
    if h > ab[i][0]:
        attack = h // ab[i][0]
        magic += attack * ab[i][1]
        h -= attack * ab[i][0]
    elif h == ab[i][0]:
        magic += ab[i][1]
        break
    else:
        continue

if h == 0:
    print(magic)
    exit()

m_min = float('inf')
for i in range(n):
    if h < ab[i][0]:
        m_min = min(m_min, ab[i][1])

print(magic + m_min)
