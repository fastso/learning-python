from bisect import bisect
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                # 如果i的值与i-1的值相等，已计算过无需再计算
                continue

            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    # 如果j的值与j-1的值相等，已计算过无需再计算
                    continue
                if nums[j] - nums[i] == k:
                    count += 1
                elif nums[j] - nums[i] < k:
                    continue
                else:
                    break
        return count
