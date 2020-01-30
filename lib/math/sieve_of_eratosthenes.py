from typing import List

'''
エラトステネスの篩

https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
計算量：O(nloglogn)
'''


def seive_of_eratosthenes(n: int) -> List[int]:
    if n < 2:
        return None

    ans = [i for i in range(2, n + 1)]
    for i in ans:
        ans = [x for x in ans if (x == i or x % i != 0)]
    return ans
