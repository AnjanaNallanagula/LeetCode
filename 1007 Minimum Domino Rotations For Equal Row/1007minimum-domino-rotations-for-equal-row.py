class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ls = [tops[0], bottoms[0]]
        
        for t in ls:
            count1 = 0
            count2 = 0
            
            for i in range(len(tops)):
                if (tops[i] != t and bottoms[i] != t):
                    break
                
                if (tops[i] != t):
                    count1 += 1
                if (bottoms[i] != t):
                    count2 += 1
                
                if (i == len(tops) - 1):
                    min1 = min(count1, count2)
                    return min1
        
        return -1