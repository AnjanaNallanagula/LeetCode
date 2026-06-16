class Solution:
    def processStr(self, s: str) -> str:
        s1 = ""
        
        for i in s:
            if (i == "*" and len(s1) >= 1):
                s1 = s1[:-1]
            elif (i == "#"):
                s1 = s1 + s1
            elif (i == "%"):
                s1 = s1[::-1]
            elif (i.isalpha()):
                s1 += i
        
        return s1