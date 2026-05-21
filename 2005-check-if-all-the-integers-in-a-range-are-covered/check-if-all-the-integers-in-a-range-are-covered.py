class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        min1 = min([i[0] for i in ranges])
        max1 = max([i[1] for i in ranges])

        if (left < min1 or right > max1):
            return False
        
        ls = [0 for i in range(max1 + 2)]

        for s, e in ranges:
            ls[s] += 1
            ls[e + 1] -= 1
        
        count = 0

        for i in range(max1 + 1):
            count += ls[i]

            if (left <= i <= right and count < 1):
                return False
        
        return True