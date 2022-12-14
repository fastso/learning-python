class UnionFind:
    """
    Quick Union
    find関数の改良：経路圧縮
    root[]: Index 節点の番号　Value 親節点の番号
    計算量: find O(H) union O(H) connected O(H)　Hは木の高さ
    https://leetcode.cn/leetbook/read/graph/r3yaqt/
    """

    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.root[y_root] = x_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)
