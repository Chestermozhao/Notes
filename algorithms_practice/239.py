"""Sliding Window Maximum Hard
"""
class MonotonicQueue:
    def __init__(self):
        self.q = []
        
    def push(self, num):
        if not self.q:
            self.q.append(num)
        else:
            while self.q and num > self.q[-1]:
                self.q.pop()
            self.q.append(num)
        return self.q
    
    def get_max(self):
        return self.q[0]

    def pop(self, num):
        if num == self.q[0]:
            self.q.pop(0)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_queue = MonotonicQueue()
        res = []
        for i, num in enumerate(nums):
            if i < k -1:
                pushed = monotonic_queue.push(num)
            else:
                pushed = monotonic_queue.push(num)
                res.append(monotonic_queue.get_max())
                monotonic_queue.pop(nums[i - k + 1])
        return res
