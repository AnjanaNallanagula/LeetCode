class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s = []
        ls = [0 for i in range(len(heights))]

        for i in range(len(heights) - 1, -1, -1):
            while (len(s) != 0 and s[-1] < heights[i]):
                s.pop()
                ls[i] += 1
            
            if (len(s) != 0):
                ls[i] += 1
            
            s.append(heights[i])
        
        return ls