from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = n
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
