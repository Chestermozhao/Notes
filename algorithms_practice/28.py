"""Implement strStr()
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # string lengths
        h, n = len(haystack), len(needle)
        
        # if needle size is 0 => needle found by default
        if n == 0:
            return 0  
        
        # needle size > haystack => needle doesnt exist in haystack
        elif n > h:
            return -1
        
        # check for all possible size of n in h (when haystack[i] matchs needle[0])
        else:
            i, flag = 0, False
            while(i <= h - n):
                if needle[0] == haystack[i]:
                    flag = self.match(i, haystack, needle)
                
                if flag:
                    return i
                i += 1
             
            # if string not found
            return -1
    
    # checks if string "needle", exists from ith index -> returns True
    # else False
    def match(self, i, haystack, needle):
        # needle length
        n = len(needle)
        
        j, found = 0, False
        while(j < n):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                break
        
        if j == n:
            return True
        return False
"""
