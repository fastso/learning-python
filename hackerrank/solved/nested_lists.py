if __name__ == '__main__':
    ans = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = [name, score]
        ans.append(temp)
    s_t = set([i[1] for i in ans])
    s_t_l = list(s_t)
    s_t_l.sort()
    names = list()
    for i in ans:
        if i[1] == s_t_l[1]:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
