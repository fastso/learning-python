class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        if n == 1:
            if words[0][-1] == words[0][0]:
                return True
            else:
                return False
        else:
            for i in range(n):
                if words[i][-1] == words[(i + 1) % n][0]:
                    continue
                else:
                    return False
            return True
