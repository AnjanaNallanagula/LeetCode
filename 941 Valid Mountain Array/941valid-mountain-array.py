class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if (n < 3):
            return False
        
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        
        for i in range(1, n):
            if (arr[i] > arr[i - 1]):
                left[i] += left[i - 1]
        
        for j in range(n - 2, -1, -1):
            if (arr[j] > arr[j + 1]):
                right[j] += right[j + 1]
        
        for i in range(1, n - 1):
            if (left[i] + right[i] - 1 == n):
                return True
        
        return False