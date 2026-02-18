class Solution:
    def removeStars(self, s: str) -> str:
        s1 = ""
        i = len(s) - 1
        count = 0

        while (i >= 0):
            if (s[i] == "*"):
                count += 1
            elif (count > 0):
                count -= 1
            else:
                s1 = s[i] + s1
            
            i -= 1
        
        return s1