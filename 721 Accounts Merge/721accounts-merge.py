from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)

        for i in accounts:
            d = i[1]

            for j in i[2:]:
                adj[d].append(j)
                adj[j].append(d)
        
        ls = []
        s = set()

        def dfs(u, ls1, s):
            ls1.append(u)
            s.add(u)

            for v in adj[u]:
                if (v not in s):
                    dfs(v, ls1, s)

        for i in accounts:
            if (i[1] not in s):
                ls1 = []
                ls1.append(i[0])

                dfs(i[1], ls1, s)

                ls1 = [ls1[0]] + sorted(ls1[1:])
                ls.append(ls1[:])
        
        return ls