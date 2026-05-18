from collections import defaultdict

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = 0
        j = 1
        n = len(arr)

        if (k > n):
            return max(arr)
        
        d = defaultdict(lambda: 0)

        while (i < n and j < n):
            if (d[arr[i]] == k):
                return arr[i]
            if (d[arr[j]] == k):
                return arr[j]
            
            if (arr[i] > arr[j]):
                d[arr[i]] += 1
                j += 1
            else:
                d[arr[j]] += 1
                i = j
                j = i + 1
        
        return max(arr)