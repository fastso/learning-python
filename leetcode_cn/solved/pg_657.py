class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = moves.count('U')
        d = moves.count('D')
        r = moves.count('R')
        l = moves.count('L')

        if u == d and r == l:
            return True
        else:
            return False
