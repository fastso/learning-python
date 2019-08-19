s = input()
t = input()

for i in t:
    if s.count(i) == 0:
        print(-1)
        exit()

ans = 0
index_sum = 0
s_work = s[:]
for i in t:
    index = s_work.find(i)
    if index == -1:
        ans += len(s)
        index_sum = 0
        s_work = s[:]
        index = s_work.find(i)
        index_sum += index + 1
    else:
        index_sum += index + 1
    s_work = s_work[index + 1:]

print(ans + index_sum)
