from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if i > min_price:
                max_profit = max(max_profit, i - min_price)
            else:
                min_price = i
        return max_profit
