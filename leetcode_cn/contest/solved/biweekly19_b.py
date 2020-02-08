from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        current_sum = sum(arr[:k])
        if current_sum / k >= threshold:
            ans += 1

        for i in range(k, len(arr)):
            current_sum = current_sum + arr[i] - arr[i - k]
            if current_sum / k >= threshold:
                ans += 1
        return ans
