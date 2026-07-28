class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ls = [0 for i in range(26)]
        n = len(s)

        for i in s:
            ls[ord(i) - 97] += 1
        
        s1 = ["" for i in range(n)]
        i = 0
        j = n - 1
        extra_char = ""

        for k in range(26):
            char = chr(97 + k)
            count = ls[k]

            if (count > 0):
                if (count % 2 == 1):
                    extra_char = char
                    count -= 1
                
                if (count > 0):
                    s1[i: i + count // 2] = [char] * (count // 2)
                    s1[j - count // 2 + 1: j + 1] = [char] * (count // 2)
                    i += count // 2
                    j -= count // 2

        if (extra_char != ""):
            s1[i] = extra_char
        
        s2 = "".join(s1)

        return s2