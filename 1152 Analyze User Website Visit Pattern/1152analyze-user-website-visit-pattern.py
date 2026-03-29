from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        d = defaultdict(list)

        for i in range(len(username)):
            d[username[i]].append((website[i], timestamp[i]))
        
        d1 = defaultdict(lambda: 0)

        for user in d:
            ls = [i[0] for i in sorted(d[user], key = lambda i: i[1])]
            s1 = set()

            for i in range(len(ls) - 2):
                for j in range(i + 1, len(ls) - 1):
                    for k in range(j + 1, len(ls)):
                        s = ls[i] + " " + ls[j] + " " + ls[k]
                        if (s not in s1):
                            d1[s] += 1
                            s1.add(s)

        max1 = 0
        s2 = ""

        for i in d1:
            if (d1[i] > max1):
                max1 = d1[i]
                s2 = i
            elif (d1[i] == max1 and i < s2):
                s2 = i
        
        ls1 = s2.split(" ")

        return ls1