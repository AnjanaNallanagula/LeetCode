class Solution:
    def reverseWords(self, s: List[str]) -> None:
        n = len(s)

        def reverse(l, r):
            while (l < r):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        reverse(0, n - 1)
        
        j = 0

        for i in range(n):
            if (s[i] == " "):
                reverse(j, i - 1)
                j = i + 1
            elif (i == n - 1):
                reverse(j, i)