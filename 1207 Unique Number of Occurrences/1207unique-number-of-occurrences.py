from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        ls = [d[i] for i in d]
        s = set(ls)
        
        if (len(s) == len(d)):
            return True
        return False