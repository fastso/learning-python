class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        num_primes = sum(self.isPrime(i) for i in range(1, n + 1))
        return self.factorial(num_primes) * self.factorial(n - num_primes) % (10 ** 9 + 7)

    def isPrime(self, n: int) -> int:
        """
        素数かどうかを判定する
        """
        if n == 1:
            return 0
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return 0
        return 1

    def factorial(self, n: int) -> int:
        """
        階乗を求める
        """
        res = 1
        for i in range(1, n + 1):
            res *= i
            res %= (10 ** 9 + 7)
        return res
