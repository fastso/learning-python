from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill) // 2
        half = sum(skill) // n
        skill.sort()
        ans = 0
        for i in range(n):
            if skill[i] + skill[-(i+1)] != half:
                return -1
            ans += skill[-(i+1)] * skill[i]
        return ans
