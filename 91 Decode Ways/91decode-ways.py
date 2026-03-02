class Solution:
    def isValid(self, s1):
        if (s1[0] == "0"):
            return False
        if (int(s1) < 1 or int(s1) > 26):
            return False
        return True
        
    def numDecodings(self, s: str) -> int:
        if (s[0] == "0"):
            return 0
        
        ls = [0 for i in range(len(s) + 1)]
        ls[0] = 1
        ls[1] = 1

        for i in range(2, len(s) + 1):
            if (self.isValid(s[i - 1: i]) == True):
                ls[i] += ls[i - 1]
            if (self.isValid(s[i - 2: i]) == True):
                ls[i] += ls[i - 2]
        
        return ls[len(s)]