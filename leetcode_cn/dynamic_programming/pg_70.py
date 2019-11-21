class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            p1 = 1
            p2 = 2
            for i in range(2, n):
                ans = p1 + p2
                p1 = p2
                p2 = ans
            return ans
