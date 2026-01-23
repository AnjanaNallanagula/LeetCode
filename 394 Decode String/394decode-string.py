class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = 0
        s1 = ""

        for i in s:
            if (i == "["):
                stack.append((s1, n))
                s1 = ""
                n = 0
            elif (i == "]"):
                prev, count = stack.pop()
                s1 = prev + count * s1
            elif (i.isalpha() == True):
                s1 += i
            else:
                n = n * 10 + int(i)
        
        return s1