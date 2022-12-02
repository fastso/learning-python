from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            else:
                if plus:
                    digits[i] += 1
                break
        return digits
