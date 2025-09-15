class Solution:
    def letterCasePermutation1(self, s, i, ls):
        if (i == len(s)):
            s1 = "".join(s)
            ls.append(s1)
            return
        
        if (s[i].isdigit() == True):
            self.letterCasePermutation1(s, i + 1, ls)
        else:
            j = i + 1

            while (j < len(s) and s[j].isdigit() == True):
                j += 1
            
            self.letterCasePermutation1(s, j, ls)
            
            s[i] = s[i].lower() if (s[i].isupper() == True) else s[i].upper()
            self.letterCasePermutation1(s, j, ls)
            s[i] = s[i].lower() if (s[i].isupper() == True) else s[i].upper()

    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s)
        ls = []

        self.letterCasePermutation1(s, 0, ls)

        return ls