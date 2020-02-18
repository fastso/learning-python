from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = list()
            d[groupSizes[i]].append(i)

        ans = list()
        for k, v in d.items():
            temp = list()
            for i in v:
                if k <= len(temp):
                    ans.append(temp)
                    temp = list()
                    temp.append(i)
                else:
                    temp.append(i)
            ans.append(temp)
        return ans
