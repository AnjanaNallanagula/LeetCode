class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}

        for i in words:
            if (i in d):
                d[i] += 1
            else:
                d[i] = 1
        
        k = len(words) * len(words[0])
        ls = []
        n = len(words[0])

        if (k > len(s)):
            return ls
        
        for i in range(len(s) - k + 1):
            d1 = d.copy()
            need = len(words)
            j = i

            while (j < i + k):
                s1 = s[j: j + n]

                if ((s1 not in d1) or (d1[s1] == 0)):
                    break
                
                d1[s1] -= 1
                need -= 1
                j += n
            
            if (need == 0):
                ls.append(i)
        
        return ls