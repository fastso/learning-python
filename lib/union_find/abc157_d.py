class UnionFind:
    """
    素集合データ構造: 要素を素集合（互いに重ならない集合）に分割して管理するデータ構造
        Union: 2つの集合を1つに併合する
        Find: ある要素がどの集合に属しているかを判定する
    """

    def __init__(self, n):
        self.n = n
        # 各要素の親要素の番号を格納するリスト
        # 要素が根（ルート）の場合は[-そのグループの要素数]を格納する
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根を返す
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループとを併合する
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズ（要素数）を返す
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        要素x, yが同じグループに属するかどうかを返す
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
        """
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        """
        print()での表示用
        """
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m, k = map(int, input().split())

uf = UnionFind(n)
friend = [set() for _ in range(n)]
block = [set() for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friend[a].add(b)
    friend[b].add(a)
    uf.union(a, b)

for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c,d):
        block[c].add(d)
        block[d].add(c)

for i in range(n):
    print(uf.size(i) - len(friend[i]) - len(block[i]) - 1, end=' ')
