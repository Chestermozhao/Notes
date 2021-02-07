"""Plus one Easy
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(f) for f in digits]
        digit = "".join(digits)
        res = int(digit) + 1
        
        result = [int(r) for r in str(res)]
        if len(result) != len(digits):
            result = [0]*(len(digits)-len(result)) + result
        return result
