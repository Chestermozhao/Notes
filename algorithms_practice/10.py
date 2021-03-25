class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while s and p:
            if p.find("*") == 1:
                if len(p) > 2 and p[0] == p[2]:
                    p = p[0:2] + p[3:]
                if p[0] == ".":
                    # 任意字符
                    if len(p) > 2:
                        if s.find(p[2]) == -1:
                            return False
                        else:
                            s = s[s.find(p[2]):]
                            p = p[2:]
                    else:
                        return True
                else:
                    # 很多重複的n
                    while s.find(p[0]) == 0:
                        s = s[1:]
                    p = p[2:]
            else:
                if p[0] == ".":
                    s = s[1:]
                    p = p[1:]
                else:
                    if s.find(p[0]) == 0:
                        s = s[1:]
                    p = p[1:]
        print(s)
        print(p)
        return not s and not p
            
