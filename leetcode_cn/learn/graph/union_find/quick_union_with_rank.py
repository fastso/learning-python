class UnionFind:
    """
    Quick Union with Rank
    union関数の改良：偏りが発生しないように、木の高さが低い方を高い方につなげる。
    root[]: Index 節点の番号　Value 親節点の番号
    計算量: find O(logN) union O(logN) connected O(logN)
    https://leetcode.cn/leetbook/read/graph/r3b9ts/
    """

    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.root[y_root] = x_root
            elif self.rank[x_root] < self.rank[y_root]:
                self.root[x_root] = y_root
            else:
                self.root[y_root] = x_root
                self.rank[x_root] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
