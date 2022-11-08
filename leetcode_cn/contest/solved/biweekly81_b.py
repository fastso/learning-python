import collections
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = total = size = 0
        vis = [False] * n

        def dfs(x: int):
            vis[x] = True
            nonlocal size
            size += 1
            for y in graph[x]:
                if not vis[y]:
                    dfs(y)

        for i in range(n):
            if not vis[i]:
                size = 0
                dfs(i)
                ans += size * total
                total += size

        return ans
