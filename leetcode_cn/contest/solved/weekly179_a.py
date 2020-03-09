class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ['a']*n
        if n%2:
            return ''.join(ans)
        else:
            ans[-1] = 'b'
            return ''.join(ans)