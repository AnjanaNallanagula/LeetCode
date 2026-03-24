class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [float("inf") for i in range(n)]
        right = [float("inf") for j in range(n)]
        index = -1
        
        for i in range(n):
            if (seats[i] == 1):
                index = i
            if (index != -1):
                left[i] = index
        
        index = -1
        
        for i in range(n - 1, -1, -1):
            if (seats[i] == 1):
                index = i
            if (index != -1):
                right[i] = index

        
        ls = [-1 for i in range(n)]
        
        for i in range(n):
            d1 = abs(i - left[i])
            d2 = abs(right[i] - i)
            
            if (d1 <= d2):
                ls[i] = left[i]
            else:
                ls[i] = right[i]

        
        max1 = -1
        
        for i in range(n):
            d = abs(i - ls[i])
            max1 = max(max1, d)
        
        return max1
