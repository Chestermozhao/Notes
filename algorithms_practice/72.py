"""Leetcode 72, minDistance from two words
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def dp(i, j):
            # 如果word1 length == 0, 要修改len(word2)次
            if i == -1:
                return j+1
            # 如果word2 length == 0, 要修改len(word1)次
            if j == -1:
                return i+1
            # 如果已經做過，直接取就可以，不再進入遞迴
            if (i, j) in memo:
                return memo[(i, j)]
            # 如果該值相同，那就不用動作，直接往斜上角走
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i-1, j-1)
            # 如果該值不同，那看是插入，修改，或替換那個最小就走哪一條
            else:
                memo[(i, j)] = min(
                    dp(i-1, j) + 1, # 刪除word1, word1引數-1
                    dp(i, j-1) + 1, # 插入word2, word2引數-1
                    dp(i-1, j-1) + 1 # 替換word1 成 word2 兩者往前走
                )
            return memo[(i, j)]
        # 從最右下角開始往上面遞減，看走到左上角最少走幾步
        return dp(len(word1) - 1, len(word2) - 1)
