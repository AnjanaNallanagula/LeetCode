class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = float('-infinity')
        max2 = float('-infinity')
        max3 = float('-infinity')

        for i in nums:
            if (i > max1):
                max3 = max2
                max2 = max1
                max1 = i
            elif (i < max1 and i > max2):
                max3 = max2
                max2 = i
            elif (i < max2 and i > max3):
                max3 = i
        
        if (max3 == float('-infinity')):
            return max1
        
        return max3