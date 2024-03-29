from sortedcontainers import SortedDict


class MyCalendarThree:
    """
在无限长的水平空间上，每多一个不重叠的点，都会将水平空间多分割为一个片段
每个start都会往水平空间的左边放向射出一条射线，每个end都会拦截住这个射线阻止其继续传播，射线在其未被拦截之前会一直存在，因此在某段区间上的射线的数目与start的数目有关，也与end的数目有关，计算方式为有N个start则+N有M个end则-M

每个start表示当前空间在此点多了一条线
每个end表示当前空间在此点少了一条线
因此可以记录所有的存在的点的增加和减少的线的数目，例如
[[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
[10,20]=>{10:1,20:-1}
从左到右以此扫描对应的点的重复线段数目为：
[10:1,20:0]
因此K为1
[50,60]=>{10:1,20:-1,50:1,60:-1}
从左到右依次扫码对应的点的重复线段的数目为：
[10:1,20:0,50:1,60:0]
因此K为1
[10,40]=>{10:2,20:-1,40:-1,50:1,60:-1}
从左到右依次扫码对应的点的重复线段的数目为：
[10:2,20:1,40:0,50:1,60:0]
因此K为2
[5,15]=>{5:1,10:2,15:-1,20:-1,40:-1,50:1,60:-1}
从左到右依次扫码对应的点的重复线段的数目为：
[5:1,10:3,15:2,20:1,40:0,50:1,60:0]
因此K为3
[5,10]=>{5:2,10:1,15:-1,20:-1,40:-1,50:1,60:-1}
从左到右依次扫码对应的点的重复线段的数目为：
[5:2,10:3,15:2,20:1,40:0,50:1,60:0]
因此K为3
[25,55]=>{5:2,10:1,15:-1,20:-1,25:1,40:-1,50:1,55:-1,60:-1}
从左到右依次扫码对应的点的重复线段的数目为：
[5:2,10:3,15:2,20:1,25:2,40:1,50:2,55:1,60:0]
因此K为3
    """

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        return ans
