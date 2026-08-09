import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n + 1)]

        for u, v, w in times:
            adj[u].append((v, w))

        q = []
        heapq.heapify(q)
        ls = [float("inf") for i in range(n + 1)]
        ls[k] = 0
        heapq.heappush(q, (0, k))

        while q:
            d, u = heapq.heappop(q)

            for v, w in adj[u]:
                if (ls[v] > ls[u] + w):
                    ls[v] = ls[u] + w
                    heapq.heappush(q, (ls[v], v))

        if (float("inf") in ls[1:]):
            return -1
        return max(ls[1:])