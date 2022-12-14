class UnionFind:
    """
    Quick Find
    root[]: Index 節点の番号　Value 根の番号
    計算量: find O(N) union O(N) connected O(1)
    """

    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.root[y_root] = x_root

    def connected(self, x, y):
        return self.find(x) == self.find(y)
