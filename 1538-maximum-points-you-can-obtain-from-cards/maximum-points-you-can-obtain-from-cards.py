class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        j = 0
        max1 = -1

        for i in range(n):
            total -= cardPoints[i]

            while (j <= i and (i - j + 1) > (n - k)):
                total += cardPoints[j]
                j += 1
            
            if ((i - j + 1) == (n - k)):
                max1 = max(max1, total)
        
        return max1