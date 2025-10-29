class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        ls = [False for i in candies]

        for i in range(len(candies)):
            if (candies[i] + extraCandies >= max1):
                ls[i] = True
        
        return ls