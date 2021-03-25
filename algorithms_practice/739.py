"""Daily Temperatures
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                tmp = stack.pop()
                res[tmp] = i - tmp
            stack.append(i)
        return res
