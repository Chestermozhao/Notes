"""Leetcode 27 Easy Remove the Element
- Given array and num, you need remove the Num in array
- Call by reference
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        while count < length:
            if nums[count] != val:
                count += 1
                continue
            else:
                nums.pop(count)
                length = len(nums)
