from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)

        for i, score in items:
            d[i].append(score)
        
        ls = []

        for i in d:
            ls1 = sorted(d[i], reverse = True)
            avg = sum(ls1[:5]) // 5
            ls.append([i, avg])
        
        ls.sort()

        return ls