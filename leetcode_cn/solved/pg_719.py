from bisect import bisect_left
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        # numsがソートされているため、k番目小さい距離はnums[-1] - nums[0]の区間内にある
        return bisect_left([range(nums[-1] - nums[0])], k, key=count)
