from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if (len(s) < 10):
            return []
        
        d = defaultdict(lambda: 0)

        for i in range(len(s) - 9):
            d[s[i: i+10]] += 1
        
        ls = [i for i in d if d[i] > 1]

        return ls