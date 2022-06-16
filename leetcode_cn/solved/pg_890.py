from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            dic = {}
            for x, y in zip(word, pattern):
                if x not in dic:
                    dic[x] = y
                elif dic[x] != y:
                    return False
            return True

        return [word for word in words if match(word, pattern) and match(pattern, word)]
