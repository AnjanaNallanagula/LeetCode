class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(" ")
        ls = [i for i in ls if (i != '')]

        print(ls)

        i = 0
        j = len(ls) - 1

        while (i < j):            
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1
        
        s1 = " ".join(ls)

        return s1