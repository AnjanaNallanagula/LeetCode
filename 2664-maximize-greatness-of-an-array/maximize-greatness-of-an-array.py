class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        nums.sort()
        n = len(nums)

        while (i < n):
            if (nums[i] > nums[j]):
                count += 1
                j += 1
            
            i += 1
        
        return count