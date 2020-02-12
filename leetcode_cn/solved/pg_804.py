from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ms = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ans = set()
        for i in range(len(words)):
            temp = list()
            for j in range(len(words[i])):
                temp.append(ms[ord(words[i][j]) - 97])
            ans.add(''.join(temp))

        return len(ans)
