class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        #dp[i][j] represents the lowest ASCII sum of deleted characters to make word1[:i] and word2[:j] identical
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0: #for two empty string, keep dp[0][0] = 0
                    continue
                elif i == 0: #if one of the string is zero, the lowest ASCII sum of deleted characters will be the sum of the other string
                    dp[i][j] = sum([ord(x) for x in s2[:j]])
                elif j == 0:
                    dp[i][j] = sum([ord(x) for x in s1[:i]])
                elif s1[i-1] == s2[j-1]: #if the current character is same, set dp[i][j] as dp[i-1][j-1]
                    dp[i][j] = dp[i-1][j-1]
                else: # if not the same, find the minimum between dp[i-1][j] + ord(s1[i-1]) and dp[i][j-1] + ord(s2[j-1])
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]
