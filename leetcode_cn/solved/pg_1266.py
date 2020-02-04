from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(1, len(points)):
            pre_x = points[i - 1][0]
            pre_y = points[i - 1][1]
            x = points[i][0]
            y = points[i][1]

            diff_x = abs(x - pre_x)
            diff_y = abs(y - pre_y)

            ans += diff_y if diff_y > diff_x else diff_x
        return ans
