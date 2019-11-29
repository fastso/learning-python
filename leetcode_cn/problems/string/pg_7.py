class Solution:
    def reverse(self, x: int) -> int:
        flag = (x < 0)
        if flag:
            l = list(str(x)[1:])
        else:
            l = list(str(x))
        n = len(l)
        left = 0
        right = n - 1
        mid = n // 2

        while left != mid:
            temp = l[left]
            l[left] = l[right]
            l[right] = temp
            left += 1
            right -= 1

        ans = int(''.join(l))
        if flag:
            ans = -ans
        if -(2 ** 31) <= ans <= 2 ** 31 - 1:
            return ans
        else:
            return 0
