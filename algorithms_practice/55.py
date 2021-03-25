class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 跳跳題，可不可以跳過邊界，可以就是true, 不可以就false
        boundary = len(nums)
        max_idx = 0
        # 去比較先前最大值跟當前最大值，判斷是否會止步於此
        for i in range(len(nums)-1):
            max_idx = max(max_idx, i+nums[i])
            if max_idx <= i:
                return False
        return True
