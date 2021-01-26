"""Leetcode 35 Easy search insert position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, item in enumerate(nums):
            if item >= target:
                return i
            elif i == len(nums)-1:
                return i + 1
