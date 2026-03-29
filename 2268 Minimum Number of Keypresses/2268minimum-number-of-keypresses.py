class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = 0
        d = {}
        presses = 1

        for i in s:
            if (i not in d):
                d[i] = 0
            d[i] += 1
        
        d = sorted(d.items(), key = lambda i: -1 * i[1])

        for i in range(len(d)):
            if (i == 9 * presses):
                presses += 1
            
            count += d[i][1] * presses

        return count