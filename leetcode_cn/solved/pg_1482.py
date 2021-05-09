from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.canMake(mid, bloomDay, m, k):
                right = mid
            else:
                left = mid + 1
        return left

    def canMake(self, days: int, bloomDay: List[int], m: int, k: int) -> bool:
        flower = 0
        bouquet = 0
        for day in bloomDay:
            if day <= days:
                flower += 1
                if flower == k:
                    bouquet += 1
                    flower = 0
            else:
                flower = 0
            if bouquet >= m:
                break
        return bouquet >= m
