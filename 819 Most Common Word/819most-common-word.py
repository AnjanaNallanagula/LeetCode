class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = ""

        for i in paragraph:
            if (i.isalpha() == True or i == " "):
                s = s + i.lower()
            else:
                s = s + " "

        ls = s.split(" ")

        d = {}

        for i in ls:
            if (i.isalpha() == True):
                if (i in d):
                    d[i] += 1
                else:
                    d[i] = 1
        
        max1 = -1
        s1 = ""

        for i in d:
            if (d[i] > max1 and i not in banned):
                max1 = d[i]
                s1 = i
        
        return s1