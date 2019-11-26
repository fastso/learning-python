from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        temp = sum(calories[0:k])
        if temp < lower:
            ans -= 1
        elif temp > upper:
            ans += 1

        n = len(calories)
        for i in range(1, n - k + 1):
            temp -= calories[i - 1]
            temp += calories[i + k - 1]
            if temp < lower:
                ans -= 1
            elif temp > upper:
                ans += 1
        return ans
