class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        
        while (i < n - 1):
            if (arr[i] == 0):
                j = n - 1
                
                while (j > i):
                    arr[j] = arr[j - 1]
                    j -= 1
                
                arr[i + 1] = 0
                i += 2
            else:
                i += 1