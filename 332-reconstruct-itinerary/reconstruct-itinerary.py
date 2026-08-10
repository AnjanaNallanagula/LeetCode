from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)
        
        for i in adj:
            adj[i].sort(reverse = True)
       
        ls = []

        def dfs(city):
            while adj[city]:
                new_city = adj[city].pop()
                dfs(new_city)
            
            ls.append(city)

        dfs("JFK")

        ls = ls[::-1]

        return ls