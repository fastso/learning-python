from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], x[1]))

        ans = list()
        for i in range(len(items)):
            if i == len(items) - 1 or items[i][0] != items[i + 1][0]:
                temp = list()
                temp.append(items[i][0])
                sum = 0
                for j in range(5):
                    sum += items[i - j][1]
                sum //= 5
                temp.append(sum)
                ans.append(temp)

        return ans
