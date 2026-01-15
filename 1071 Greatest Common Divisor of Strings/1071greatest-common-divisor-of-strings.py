class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (len(str2) > len(str1)):
            return self.gcdOfStrings(str2, str1)
        
        if (str1.startswith(str2) == False):
            return ""
        if (len(str2) == 0):
            return str1
        
        return self.gcdOfStrings(str1[len(str2):], str2)