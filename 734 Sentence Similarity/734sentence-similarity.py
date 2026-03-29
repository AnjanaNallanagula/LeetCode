from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if (len(sentence1) != len(sentence2)):
            return False
        
        d = defaultdict(list)
        
        for i, j in similarPairs:
            d[i].append(j)
            d[j].append(i)
        
        for i in range(len(sentence1)):
            if (sentence1[i] == sentence2[i]):
                continue
            if ((sentence1[i] not in d) or (sentence2[i] not in d[sentence1[i]])):
                return False
        
        return True