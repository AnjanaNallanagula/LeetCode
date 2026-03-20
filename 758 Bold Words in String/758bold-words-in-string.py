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
        
    def boldWords(self, words: List[str], s: str) -> str:
        ls = []

        for t in words:
            ls1 = []
            
            self.findSubstringOccurrences(s, t, ls1)

            if (ls1 != []):
                ls.extend(ls1)
            
        ls.sort()
        prev = 0

        for i in range(1, len(ls)):
            if (ls[i][0] <= ls[prev][1] + 1):
                ls[prev][1] = max(ls[prev][1], ls[i][1])
            else:
                prev += 1
                ls[prev] = ls[i]
        
        ls = ls[:prev + 1]

        s1 = ""
        prev = 0

        for i, j in ls:
            s1 += s[prev:i]
            s1 += "<b>"
            s1 += s[i: j+1]
            s1 += "</b>"
            prev = j + 1
        
        s1 += s[prev:]

        return s1