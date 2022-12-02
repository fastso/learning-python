from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        cap_a, cap_b = capacityA, capacityB
        left, right = 0, len(plants) - 1
        count = 0
        while left < right:
            if cap_a >= plants[left]:
                cap_a -= plants[left]
            else:
                cap_a = capacityA - plants[left]
                count += 1
            left += 1

            if cap_b >= plants[right]:
                cap_b -= plants[right]
            else:
                cap_b = capacityB - plants[right]
                count += 1
            right -= 1

        if left == right:
            if cap_b <= cap_a < plants[left]:
                count += 1
            elif cap_a < cap_b < plants[right]:
                count += 1
        return count
