def tree_add(tree, p, ans, num):
    ans[p] += num
    if tree[p]:
        for i in tree[p]:
            tree_add(tree, i, ans, num)

n, q = map(int, input().split())
tree = [[] for i in range(n)]
ans = [0] * n

for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)

for i in range(q):
    p, x = map(int, input().split())
    p -= 1
    tree_add(tree, p, ans, x)

print(*ans)
