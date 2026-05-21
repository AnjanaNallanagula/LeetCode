class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        ls = [0 for i in range(n + 1)]

        for p, d in lights:
            l = max(0, p - d)
            h = min(n - 1, p + d)
            ls[l] += 1
            ls[h + 1] -= 1 
        
        b = 0
        count = 0

        for i in range(n):
            b += ls[i]

            if (b >= requirement[i]):
                count += 1

        return count