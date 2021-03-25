"""Next Greater Element II
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        _nums = nums*2
        stack = []
        res = [-1]*n*2
        
        for i in range(n*2):
            while stack and _nums[stack[-1]] < _nums[i]:
                tmp = stack.pop()
                res[tmp] = _nums[i]
            
            stack.append(i)
        return res[:n]

"""
這個更高效，是我看網上學的，可以不要直接對兩倍數組做，可以直接同個數組做兩次
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
        return res
"""
