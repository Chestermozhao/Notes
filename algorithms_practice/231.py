"""Leetcode 231 Easy
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""
class Solution:
    expected_nums = set([2**i for i in range(31)])
    def isPowerOfTwo(self, n: int) -> bool:
        if n in self.expected_nums:
            return True
        return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return math.log2(n) % 1 == 0 if n > 0 else False
