from itertools import pairwise
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        for c in words[0]:
            g[c] = []
        for s1, s2 in pairwise(words):
            for c in s2:
                g.setdefault(c, [])
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    g[c1].append(c2)
                    break
            else:
                if len(s1) > len(s2):
                    # all (c1 == c2) 且 s1 > s2 时，说明 s2 是 s1 的子串
                    # 所以 s2 不能排在 s1 的后面, 不为合法字母顺序，返回空
                    return ""

        VISITING, VISITED = 1, 2
        states = {}
        order = []

        def dfs(u: str) -> bool:
            # 将节点 u 的状态更新为「访问中」
            states[u] = VISITING
            # 对于每个与节点 u 相邻的节点 v，判断节点 v 的状态
            for v in g[u]:
                if v not in states:
                    # 如果节点 v 的状态是「未访问」，则继续搜索节点 v
                    if not dfs(v):
                        return False
                elif states[v] == VISITING:
                    # 如果节点 v 的状态是「访问中」，则找到有向图中的环，因此不存在拓扑排序
                    return False
                else:
                    pass
                    # 如果节点 v 的状态是「已访问」，则节点 v 已经搜索完成并入栈，节点 u 尚未入栈，因此节点 u 的拓扑顺序一定在节点 v 的前面，不需要执行任何操作。

            # 当节点 u 的所有相邻节点的状态都是「已访问」时，将节点 u 的状态更新为「已访问」，并将节点 u 入栈
            order.append(u)
            states[u] = VISITED
            return True

        # 任意选取一个「未访问」的节点 u，从节点 u 开始深度优先搜索
        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ""
