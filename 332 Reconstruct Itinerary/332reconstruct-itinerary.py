from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets, reverse = True)

        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        path = []

        def dfs(city):
            while (graph[city]):
                dfs(graph[city].pop())

            path.append(city)
        
        dfs("JFK")

        return path[::-1]