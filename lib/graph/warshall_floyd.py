"""
reference:
https://qiita.com/okaryo/items/8e6cd73f8a676b7a5d75
"""
from typing import List


def warshall_floyd(n: int, d: List[int][int]):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
