class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ls = []
        
        if (len(nums) == 0):
            ls.append([lower, upper])
            return ls
        if (nums[0] > lower):
            ls.append([lower, nums[0] - 1])
        
        i = 1
        
        while (i < len(nums)):
            d = nums[i] - nums[i - 1]
            
            if (d > 1):
                ls1 = [nums[i - 1] + 1, nums[i] - 1]
                
                ls.append(ls1)
            
            i += 1
        
        if (nums[-1] < upper):
            ls.append([nums[-1] + 1, upper])
        
        return ls