class Solution:
    def findSubstringOccurrences(self, s, t, ls1):
        n = len(s)
        m = len(t)

        for i in range(n - m + 1):
            j = 0

            while (j < m and t[j] == s[i + j]):
                j += 1
            
            if (j == m):
                ls1.append([i, i + j - 1])
    
    def addBoldTag(self, s: str, words: List[str]) -> str:
        ls = []

        for t in words:
            ls1 = []

            self.findSubstringOccurrences(s, t, ls1)
            ls.extend(ls1)
        
        if (len(ls) == 0):
            return s
        
        ls.sort()
        prev = 0

        for i in range(1, len(ls)):
            if (ls[i][0] <= ls[prev][1] + 1):
                ls[prev][1] = max(ls[prev][1], ls[i][1])
            else:
                prev += 1
                ls[prev] = ls[i]
        
        ls = ls[:prev + 1]

        prev = 0
        ls2 = []

        for i, j in ls:
            ls2.append(s[prev:i])
            ls2.append("<b>")
            ls2.append(s[i: j+1])
            ls2.append("</b>")
            prev = j + 1
        
        ls2.append(s[prev:])
        s1 = "".join(ls2)
        
        return s1