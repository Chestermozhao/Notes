"""Leetcode 14 Easy Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
class Solution:
    def refresh_prefix(self, item, _prefix):
        _p = ""
        for p in item:
            if _prefix.startswith(p):
                _p += p
                _prefix = _prefix[1:]
            else:
                break
        return _p
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        prefix = ""
        for i, item in enumerate(strs):
            if i == 0:
                prefix = item
            else:
                prefix = self.refresh_prefix(item, prefix)
        return prefix
