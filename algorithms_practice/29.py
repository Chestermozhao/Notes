"""Leetcode 29 Medium Devide two integer

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0
        res = int(dividend / divisor)
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        return res
