from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)

        # 単語を分割する
        words = sentence.split(' ')
        # 単語を置換する
        for i, word in enumerate(words):
            for d in dictionary:
                if word.startswith(d):
                    words[i] = d
                    break
        # 単語を結合する
        return ' '.join(words)