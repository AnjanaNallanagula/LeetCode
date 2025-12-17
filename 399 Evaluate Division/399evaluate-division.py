from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)

        for i in range(len(equations)):
            d[equations[i][0]].append((equations[i][1], values[i]))
            d[equations[i][1]].append((equations[i][0], 1 / values[i]))
        
        ls = []

        def dfs(src, dest, ls1, s):
            if (src == dest):
                return True
            
            s.add(src)

            for j, val in d[src]:
                if (j not in s):
                    ls1[0] *= val

                    if (dfs(j, dest, ls1, s) == True):
                        return True
                    
                    ls1[0] /= val
            
            s.remove(src)

        for u, v in queries:
            ls1 = [1.0]

            if ((u not in d) or (v not in d)):
                ls.append(-1 * ls1[0])
            else:
                s = set()
                if (dfs(u, v, ls1, s) == True):
                    ls.append(ls1[0])
                else:
                    ls.append(-1 * ls1[0])
        
        return ls