import re

class Solution:
    def myAtoi(self, s: str) -> int:
        result = re.search("^[+|-]{0,1}\d+", s.strip())
        if result:
            res = result.group()
            if int(res) >= 2147483648:
                return "2147483647"
            elif int(res) < -2147483648:
                return "-2147483648"
            return str(int(res.strip("+")))
        else:
            return 0
