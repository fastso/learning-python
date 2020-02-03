class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = [int(_) for _ in list(str(n))]
        multi = l[0]
        add = l[0]

        for i in range(1, len(l)):
            multi *= l[i]
            add += l[i]
        return multi - add
