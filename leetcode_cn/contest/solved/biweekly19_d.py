from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        arr_len = len(arr)

        if arr_len == 1:
            return 0
        if arr_len == 2:
            return 1

        for i in reversed(range(1, arr_len - 1)):
            if arr[i - 1] == arr[i] == arr[i + 1]:
                arr.pop(i)
        arr_len = len(arr)

        que = list()
        visited = [0] * arr_len

        d = dict()
        for i in range(len(arr)):
            if not arr[i] in d:
                d[arr[i]] = []
            d[arr[i]].append(i)

        # 先頭は訪問済
        visited[0] = 1
        que.append(1)
        visited[1] = 1
        for i in range(2, arr_len):
            if arr[i] == arr[0]:
                que.append(i)
                visited[i] = 1
        level = 1
        if visited[-1]:
            return level

        while que:
            que_size = len(que)
            level += 1
            for i in range(que_size):
                node = que.pop(0)
                if not visited[node - 1]:
                    que.append(node - 1)
                    visited[node - 1] = 1
                if not visited[node + 1]:
                    que.append(node + 1)
                    visited[node + 1] = 1
                for j in d[arr[node]]:
                    if not visited[j]:
                        que.append(j)
                        visited[j] = 1

            if visited[-1]:
                return level
