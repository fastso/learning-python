import math
from typing import List
from lib.math import sieve_of_eratosthenes

'''
素因数分解

整数Nの素因数の最大値は√N以下
'''


def prime_factorization(n: int) -> List[int]:
    prime_max = math.floor(math.sqrt(n))
    prime_list = sieve_of_eratosthenes.seive_of_eratosthenes(prime_max)

    ans = list()
    for prime in prime_list:
        while n % prime == 0:
            ans.append(prime)
            n //= prime
    if n != 1:
        ans.append(n)
    return ans
