class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s1 = ""
        open1 = 0
        close = 0

        for i in s:
            if (i == "("):
                s1 += i
                open1 += 1
            elif (i == ")" and open1 > 0):
                open1 -= 1
                s1 += i
            elif (i.isalpha() == True):
                s1 += i
        
        s2 = ""
        open1 = 0
        close = 0

        for i in s1[::-1]:
            if (i == ")"):
                s2 = i + s2
                close += 1
            elif (i == "(" and close > 0):
                close -= 1
                s2 = i + s2
            elif (i.isalpha() == True):
                s2 = i + s2
        
        return s2