class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        
        for i in num:
            while (len(s) != 0 and k > 0 and s[-1] > i):
                s.pop()
                k -= 1
            
            s.append(i)
        
        while (len(s) != 0 and k > 0):
            s.pop()
            k -= 1
        
        n = "".join(s)
        i = 0
        
        while (i < len(n) and s[i] == "0"):
            i += 1
        
        if (i == len(n)):
            return "0"
        return n[i:]