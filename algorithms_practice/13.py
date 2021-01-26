"""Leetcode 13 Easy Roman to Integer
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1,
                      'IV': 4,
                      'IX': 9,
                      'V': 5,
                      'X': 10,
                      'XL': 40,
                      'XC':90,
                      'L': 50,
                      'C': 100,
                      'CD': 400,
                      'CM': 900,
                      'D': 500, 
                      'M': 1000
                     }
        
        res = 0
        
        i = 0
        while (i < len(s)):
            num = roman_dict[s[i]]
            if (i + 1 < len(s) and roman_dict.get(s[i:i+2])):
                num = roman_dict[s[i:i+2]]
                i += 1
            i += 1
            res += num
            
        return res
