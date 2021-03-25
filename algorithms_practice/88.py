"""88 Merge Sorted Array Easy
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        while (p1 != m + n and p2 != n):
            # if p2 item < p1 item insert it to bf idx
            if nums1[p1] > nums2[p2] or p1 >= m + p2:
                nums1.insert(p1, nums2[p2])
                nums1.pop()
                p2 += 1
            p1 += 1
        
