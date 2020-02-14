class Solution:
    def isArmstrong(self, N: int) -> bool:
        N = str(N)
        N_len = len(N)
        ans = 0
        for n in N:
            ans += int(n) ** N_len
        if ans == int(N):
            return True
        else:
            return False
