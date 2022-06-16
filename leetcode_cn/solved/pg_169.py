class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        for key in hash:
            if hash[key] > len(nums) / 2:
                return key
