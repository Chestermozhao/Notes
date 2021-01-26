"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    limitation = 2147483648
    def reverse(self, x: int) -> int:
        reversed_x = int(str(abs(x))[::-1])
        if x > self.limitation or reversed_x > self.limitation:
            return 0
        if x < 0:
            reversed_x = f"-{reversed_x}"
        return int(reversed_x)
