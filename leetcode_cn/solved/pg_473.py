from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        # マッチ棒が4本以下　または　合計長さが4の倍数でない場合はFalse
        if len(matchsticks) < 4 or total_len % 4:
            return False
        # マッチ棒の長さの逆順でソート
        matchsticks.sort(reverse=True)

        edges = [0] * 4

        # マッチ棒を候補とする
        def dfs(idx: int) -> bool:
            if idx == len(matchsticks):
                # 全てのマッチ棒を使った = 解が見つかった Trueを返す
                return True
            for i in range(4):
                # 候補のマッチを仮の解として、4つの辺にそれぞれ入れてみる
                edges[i] += matchsticks[idx]
                if edges[i] <= total_len // 4 and dfs(idx + 1):
                    # 入れてみた解が正しい場合は、次のマッチ棒を候補とし再帰的に解を探す
                    return True
                # 入れてみた解が正しくない場合は、辺を戻して次のマッチ棒を候補とする
                edges[i] -= matchsticks[idx]
            # 全てのマッチ棒を使ったが、正しい解が見つからなかった場合、 Falseを返す
            return False

        return dfs(0)
