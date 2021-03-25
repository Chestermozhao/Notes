import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _nums = nums[:k]
        res = heapq.heapify(_nums)
        for i in range(k, len(nums)):
            heapq.heappush(_nums, nums[i])
            heapq.heappop(_nums)
        return heapq.heappop(_nums)
