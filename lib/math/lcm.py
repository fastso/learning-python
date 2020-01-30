import math
from typing import List
from lib.math import sieve_of_eratosthenes
from lib.math import prime_factorization


def lcm_list(l: List[int]) -> int:
    """
    最小公倍数（リスト）
    速度改善の余地あり
    :param l:
    :return:
    """
    l_max = math.floor(max(l))
    prime_list = sieve_of_eratosthenes.seive_of_eratosthenes(l_max)
    exponent_list = [0] * len(prime_list)
    prime_dict = dict(zip(prime_list, exponent_list))

    for i in l:
        prime_dict_temp = dict(zip(prime_list, exponent_list))
        prime_list_temp = prime_factorization.prime_factorization(i)
        for j in prime_list_temp:
            prime_dict_temp[j] += 1
        for j in prime_dict_temp:
            prime_dict[j] = max(prime_dict[j], prime_dict_temp[j])

    ans = 1
    for k, v in prime_dict.items():
        if v != 0:
            ans *= math.pow(k, v)
    return int(ans)
