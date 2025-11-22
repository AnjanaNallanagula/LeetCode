class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ls = [-1 for i in range(len(nums))]
        j = 0
        sum1 = 0

        for i in range(len(nums)):
            sum1 += nums[i]

            if (i >= (2 * k + 1)):
                sum1 -= nums[j]
                j += 1
            
            if ((i - j + 1) == (2 * k + 1)):
                mid = (i + j) // 2 
                ls[mid] = (sum1 // (2 * k + 1))

        return ls