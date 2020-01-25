from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        diff = list()
        for i in range(n - 1):
            diff.append(abs(nums[i] - nums[i + 1]))
        max_num = max(nums)
        max_index = nums.index(max_num)

        max_value = 0
        for i in range(n - 1):
            if i == max_index:
                continue
            j = max_index
            temp_value = 0
            if i > 0:
                temp_value += abs(nums[j] - nums[i - 1]) - diff[i - 1]
            if j < n - 1:
                temp_value += abs(nums[i] - nums[j + 1]) - diff[j]

            if temp_value > max_value:
                max_value = temp_value

        if max_value:
            return sum(diff) + max_value
        else:
            return sum(diff)
