class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s1 = set()

        for i in range(len(s) - k + 1):
            s1.add(s[i: i + k])

        if (len(s1) == (2 ** k)):
            return True
        return False