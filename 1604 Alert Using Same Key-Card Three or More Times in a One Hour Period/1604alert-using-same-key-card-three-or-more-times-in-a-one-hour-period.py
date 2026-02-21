from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)

        for i in range(len(keyName)):
            d[keyName[i]].append(keyTime[i])

        ls = []

        for i in d:
            ls1 = sorted(d[i])
            j = 0

            while (j < len(ls1) - 2):
                h1, m1 = ls1[j].split(":")
                h2, m2 = ls1[j + 2].split(":")
                d1 = ((int(h2) - int(h1)) * 60) + (int(m2) - int(m1))

                if (d1 <= 60):
                    ls.append(i)
                    break
                
                j += 1
        
        ls.sort()

        return ls