"""Leetcode 172 Easy
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
"""

class Solution:
    def get_five_count(self, num):
        c = 0
        five_flag = True
        while five_flag:
            num = num / 5
            if num % 5 != 0:
                five_flag = False
            c += 1
        return c
    def trailingZeroes(self, n: int) -> int:
        five_count = 0
        for i in range(1, n+1):
            if i % 5 == 0:
                _five_count = self.get_five_count(i)
                five_count += _five_count
        return five_count
