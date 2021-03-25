class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len == 0:
            return 0
        # initialize跟數列一樣長度的list
        dp = [-1]*num_len
        for i in range(num_len):
            # 如果第0個就是直接assign value
            if i == 0:
                dp[i] = nums[i]
            # 後續就是去比較自己更大還是累加更大，一旦自己更大家保留自己
            # 下一步就會只從你這個開始加
            else:
                dp[i] = max(nums[i], dp[i-1]+nums[i])

        # 初始化極小值
        res = -100000
        # 去比較哪個是最大值 他就是總合最大
        for i in range(num_len):
            res = max(res, dp[i])
        return res
