class Solution:
    def __init__(self):
        self.memo = {}
        
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        c_len = self.longestCommonSubsequence(word1, word2)
        return m - c_len + n - c_len

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp(text1, 0, text2, 0)

    def dp(self, s1, i, s2, j):
        if len(s1) == i or len(s2) == j:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        # 如果相等，相同長度+1
        if s1[i] == s2[j]:
            self.memo[(i, j)] = 1 + self.dp(s1, i+1, s2, j+1)
        # 如果不相等，會出現三種情況，
        # 第一個字串的i不在共同名單內 -> i+1
        # 第二個字串的j不在共同名單內 -> j+1
        # 兩個都不在共同名單內 -> i+1, j+1(但這個因為絕對最短，我們要取max，所以可以忽略)
        else:
            self.memo[(i, j)] = max(
                self.dp(s1, i+1, s2, j),
                self.dp(s1, i, s2, j+1)
          )
        return self.memo[(i, j)]
