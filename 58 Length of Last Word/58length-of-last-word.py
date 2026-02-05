class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split(" ")
        i = len(ls) - 1

        while ((i >= 0) and (ls[i].isalpha() == False)):
            i -= 1
        
        return len(ls[i])