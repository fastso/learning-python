class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            current = n & 1
            ans += (current << (31 - i))
            n = n >> 1
        return ans
