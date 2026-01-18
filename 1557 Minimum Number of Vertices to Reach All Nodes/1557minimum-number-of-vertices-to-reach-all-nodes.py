class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]

        for i in edges:
            adj[i[0]].append(i[1])
            in_degree[i[1]] += 1
        
        ls = []

        for i in range(len(in_degree)):
            if (in_degree[i] == 0):
                ls.append(i)
        
        return ls