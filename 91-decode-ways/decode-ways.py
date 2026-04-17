class Solution:
    def numDecodings(self, s: str) -> int:
        if (s[0] == "0"):
            return 0
        
        ls = [0 for i in range(len(s) + 1)]
        ls[0] = 1
        ls[1] = 1

        def isValid(s1):
            if (s1[0] == "0"):
                return 0
            
            if (1 <= int(s1) <= 26):
                return True
            return False
        
        for i in range(2, len(s) + 1):
            if (1 <= int(s[i-1]) <= 9):
                ls[i] += ls[i - 1]
            if (isValid(s[i-2: i]) == True):
                ls[i] += ls[i - 2]
        
        return ls[-1]