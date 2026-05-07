from math import ceil
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if (n == 1):
            return 0
        
        prev = self.kthGrammar(n - 1, ceil(k / 2))

        if (prev == 0):
            curr = 0 if (k % 2 == 1) else 1
        else:
            curr = 1 if (k % 2 == 1) else 0
        
        return curr