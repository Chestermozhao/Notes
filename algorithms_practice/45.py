class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        farest = 0
        current_idx = 0
        for i in range(len(nums)-1):
            farest = max(farest, i+nums[i])
            if i == current_idx:
                jump_count += 1
                current_idx = farest
        return jump_count


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")]*n
        dp[0] = 0
        for i in range(n):
            print("-----", dp, i)
            for k in range(i+1, nums[i]+i+1):
                if k >= n:
                    break
                dp[k] = min(dp[k], dp[i]+1)
                print("=====", dp, k)
        return dp[n-1]
