from itertools import groupby

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10 ** 9 + 7
        ls1 = [1, 1, 2, 4]
        ls2 = [1, 1, 2, 4]

        for i in range(100000):
            ls1.append((ls1[-1] + ls1[-2] + ls1[-3]) % MOD)
            ls2.append((ls2[-1] + ls2[-2] + ls2[-3] + ls2[-4]) % MOD)
        
        p = 1

        for d, g in groupby(pressedKeys):
            count = len(list(g))

            if (d in "79"):
                p = (p * ls2[count]) % MOD
            else:
                p = (p * ls1[count]) % MOD
        
        return p