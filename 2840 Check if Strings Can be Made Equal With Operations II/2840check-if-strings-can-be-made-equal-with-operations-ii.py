from collections import defaultdict

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        dict_even = defaultdict(lambda: 0)
        dict_odd = defaultdict(lambda: 0)

        for i in range(len(s1)):
            if (i % 2 == 0):
                dict_even[s1[i]] += 1
                dict_even[s2[i]] -= 1
            else:
                dict_odd[s1[i]] += 1
                dict_odd[s2[i]] -= 1
        
        for i in dict_even:
            if (dict_even[i] != 0):
                return False
        
        for j in dict_odd:
            if (dict_odd[j] != 0):
                return False
        
        return True