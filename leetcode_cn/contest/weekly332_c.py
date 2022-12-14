from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key=lambda x: min(x[0], x[1]))
        citys = set()
        citys.add(1)
        ans = float("inf")
        for road in roads:
            if road[0] not in citys and road[1] not in citys:
                continue
            else:
                citys.add(road[0])
                citys.add(road[1])
                ans = min(ans, road[2])
        return ans
