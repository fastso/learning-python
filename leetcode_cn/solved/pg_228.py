class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans_list = []
        low = -1
        high = -1
        for i in range(len(nums)):
            if low == -1:
                low = high = nums[i]
            if nums[i] == high + 1:
                high = nums[i]
            elif nums[i] == high:
                continue
            else:
                if low == high:
                    ans_list.append(str(low))
                else:
                    ans_list.append(str(low) + "->" + str(high))
                low = high = nums[i]

        if low == high:
            ans_list.append(str(low))
        else:
            ans_list.append(str(low) + "->" + str(high))

        return ans_list
