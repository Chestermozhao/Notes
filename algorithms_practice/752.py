"""Leetcode 752 Medium
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
"""
class Solution:
    def plus(self, num):
        if num == "9":
            return "0"
        return str(int(num) + 1)
    def minus(self, num):
        if num == "0":
            return "9"
        return str(int(num) - 1)
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = []
        q.append("0000")
        times = 0
        while q:
            next_q = []
            for i, item in enumerate(q):
                if item in visited:
                    continue
                visited.add(item)
                if item == target:
                    return times
                for i in range(4):
                    plused = self.plus(item[i])
                    new_pwd = item[:i] + plused + item[i+1:]
                    if new_pwd not in visited:
                        next_q.append(new_pwd)
                    minused = self.minus(item[i])
                    new_pwd = item[:i] + minused + item[i+1:]
                    if new_pwd not in visited:
                        next_q.append(new_pwd)
            q = next_q
            times += 1
        return -1
