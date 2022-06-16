from bisect import bisect_right
from random import randrange
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # sum为矩形面积的前缀和（Prefix Sum）
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        # 总面积中随机取一点k
        k = randrange(self.sum[-1])
        # 二分查找确定k在哪一个矩形中
        rect_index = bisect_right(self.sum, k) - 1
        a, b, x, y = self.rects[rect_index]
        # 确定k在矩形内的点的坐标
        da, db = divmod(k - self.sum[rect_index], y - b + 1)
        return [a + da, b + db]