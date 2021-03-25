class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        # 創建二維數組
        dp = [[0] * n for _ in range(n)]
        # 倒序，從右下角開始iter
        for i in range(n - 1, -1, -1):
            # 對角線就是自己等於自己，所以都1
            dp[i][i] = 1
            # 只做右上角，從下面往上做
            for j in range(i + 1, n):
                # 如果s.i == s.j, 縮小範圍+2
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # 如果不相等，那就看左邊往前或右邊往後誰比較大
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1] 
