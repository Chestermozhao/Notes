"""Leetcode 26 Easy
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while True:
            if i+1 > len(nums)-1:
                break
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:          
                i += 1
        return len(nums)
