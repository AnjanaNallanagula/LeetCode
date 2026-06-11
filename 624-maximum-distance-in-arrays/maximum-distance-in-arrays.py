class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1 = arrays[0][0]
        max1 = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            d1 = max1 - arrays[i][0]
            d2 = arrays[i][-1] - min1
            max_distance = max(max_distance, d1, d2)
            min1 = min(min1, arrays[i][0])
            max1 = max(max1, arrays[i][-1])
        
        return max_distance