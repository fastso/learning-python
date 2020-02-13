from lib.math import sieve_of_eratosthenes
from lib.math import prime_factorization
from lib.math import lcm
from lib.tree import binary_search_tree
from lib.dynammic_programming.digit_dp.leetcode1012 import Solution
from lib.dynammic_programming.digit_dp.pg_233 import Solution

# エラトステネスの篩
# print(sieve_of_eratosthenes.seive_of_eratosthenes(10000))

# 素因数分解
# print(prime_factorization.prime_factorization(341324))

# 最小公倍数
# l = [18,24,46,452,542,321,13]
# print(lcm.lcm_list(l))

s = Solution()
print(s.countDigitOne(1))
