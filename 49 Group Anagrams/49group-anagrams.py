from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            d[key].append(i)
        
        ls = []

        for i in d:
            ls.append(d[i])
        
        return ls