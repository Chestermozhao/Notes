"""Next Greater Element I
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_next_great_num(src_num):
            start = nums2.index(src_num)
            for i in range(start, len(nums2)):
                if nums2[i] > src_num:
                    return nums2[i]
            return -1
        res = []
        for num in nums1:
            next_great_num = get_next_great_num(num)
            if not next_great_num:
                res.append(-1)
            else:
                res.append(next_great_num)
        return res
