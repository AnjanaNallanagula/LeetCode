class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ls = [0 for i in range(len(nums))]
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1

        while (i <= j):
            d1 = nums[i] ** 2
            d2 = nums[j] ** 2

            if (d1 >= d2):
                ls[k] = d1
                i += 1
            else:
                ls[k] = d2
                j -= 1
            
            k -= 1
        
        return ls