"""137 Single number II Medium
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        res = [k for k, v in count_dict.items() if v == 1]
        return res[0]
