from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1

        while i > 0:
            i -= 1
            if nums[i]:
                continue

            # 遇到0时，检查0的前方是否有可以跳过0的值
            j = i
            can_flag = False
            while j > 0:
                j -= 1
                if nums[j] + j > i:
                    i = j
                    can_flag = True
                    break
                else:
                    continue
            if not can_flag:
                return False
        return True
