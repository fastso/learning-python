class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums) + 1) // 2
        nums[::2], nums[1::2] = reversed(nums[:mid]), reversed(nums[mid:])
        return nums