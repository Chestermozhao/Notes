"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) > 200 or len(num2) > 200:
            return 0
        return str(int(num1) * int(num2))
