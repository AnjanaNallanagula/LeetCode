class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0 for i in range(n)]
        ls = []
        p = 0

        for i, c in queries:
            if ((i - 1) >= 0 and colors[i - 1] != 0 and colors[i] == colors[i - 1]):
                p -= 1
            if ((i + 1) < n and colors[i + 1] != 0 and colors[i] == colors[i + 1]):
                p -= 1

            colors[i] = c

            if ((i - 1) >= 0 and colors[i - 1] != 0 and colors[i] == colors[i - 1]):
                p += 1
            if ((i + 1) < n and colors[i + 1] != 0 and colors[i] == colors[i + 1]):
                p += 1
            
            ls.append(p)

        return ls