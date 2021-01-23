"""Leetcode 241 Easy
- Refer from https://blog.csdn.net/github_39261590/article/details/73864039
- 厄拉多塞筛法
  - 走訪的時候把倍數全部過濾，因為質數的倍數不會是質數
"""


class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        # initialize with True list
        primes = [True] * n
        primes[0] = primes[1] = False
        # Just traverse n ** 0.5
        # Re-assugn value to False since the num is one of multiple prime
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)


