from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ans = [[0] * m for _ in range(n)]
        r = dict()
        c = dict()

        for i in indices:
            if i[0] in r:
                r[i[0]] += 1
            else:
                r[i[0]] = 1
            if i[1] in c:
                c[i[1]] += 1
            else:
                c[i[1]] = 1

        for k, v in r.items():
            for i in range(m):
                ans[k][i] += v
        for k, v in c.items():
            for i in range(n):
                ans[i][k] += v

        count = 0
        for i in range(n):
            for j in range(m):
                if ans[i][j] % 2:
                    count += 1
        return count
