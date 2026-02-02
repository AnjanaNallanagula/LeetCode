class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ls = []

        for i in range(len(nums)):
            if (nums[abs(nums[i]) - 1] > 0):
                nums[abs(nums[i]) - 1] *= -1
            else:
                ls.append(abs(nums[i]))
        
        return ls