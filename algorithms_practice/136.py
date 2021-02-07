"""136 Single Number Easy
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            num = nums.pop()
            try:
                nums.remove(num)
            except ValueError:
                return num
