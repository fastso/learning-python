s = list(input())
n = int(input())

reverse_flag = False
s_head = list()

for i in range(n):
    line = list(map(str, input().split()))
    if line[0] == '1':
        if reverse_flag:
            reverse_flag = False
        else:
            reverse_flag = True
    elif line[0] == '2':
        if line[1] == '1':
            if reverse_flag:
                s.append(line[2])
            else:
                s_head.append(line[2])
        elif line[1] == '2':
            if reverse_flag:
                s_head.append(line[2])
            else:
                s.append(line[2])

if reverse_flag:
    ans = s[::-1]
    ans.extend(s_head)
    print(''.join(ans))
else:
    ans = s_head[::-1]
    ans.extend(s)
    print(''.join(ans))
