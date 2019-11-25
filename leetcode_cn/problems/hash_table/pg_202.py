class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        visited = set()
        while True:
            s = str(sum(int(i) ** 2 for i in s))
            if s == '1':
                return True
            if s in visited:
                return False
            visited.add(s)
