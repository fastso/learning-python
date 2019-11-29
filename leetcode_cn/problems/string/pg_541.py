class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        l = list(s)
        n = len(l)
        while True:
            if i >= n - 1:
                break
            if i + 2 * k - 1 < n:
                left = i
                right = i + k - 1
                i += 2 * k
            elif i + k - 1 < n:
                left = i
                right = i + k - 1
                i += 2 * k
            else:
                left = i
                right = n - 1
                i = n - 1

            mid = left + (right - left + 1) // 2
            while left != mid:
                temp = l[left]
                l[left] = l[right]
                l[right] = temp
                left += 1
                right -= 1
        return ''.join(l)
