class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ls = [str(i) for i in range(1, n + 2)]
        i = 0

        while (i < n):
            if (pattern[i] == "D"):
                j = i

                while (j < n and pattern[j] == "D"):
                    j += 1
                
                ls[i:j+1] = ls[i:j+1][::-1]
                i = j
            else:
                i += 1
        
        s = "".join(ls)

        return s