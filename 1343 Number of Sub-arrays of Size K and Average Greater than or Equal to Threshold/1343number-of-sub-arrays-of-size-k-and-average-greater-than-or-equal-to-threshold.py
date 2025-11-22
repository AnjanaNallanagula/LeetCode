class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        j = 0
        sum1 = 0

        for i in range(len(arr)):
            sum1 += arr[i]

            if (i >= k):
                sum1 -= arr[j]
                j += 1
            
            if ((i - j + 1) == k):
                avg = sum1 / k

                if (avg >= threshold):
                    count += 1
        
        return count