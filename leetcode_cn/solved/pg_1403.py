class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        for i in range(len(nums)):
            if sum(ans) <= sum(nums[i:]):
                ans.append(nums[i])
        return ans