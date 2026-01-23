class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ls = [0, 0]

        for i in range(len(nums)):
            if (nums[abs(nums[i]) - 1] > 0):
                nums[abs(nums[i]) - 1] *= -1
            else:
                ls[0] = abs(nums[i])
        
        for i in range(len(nums)):
            if (nums[i] > 0):
                ls[1] = i + 1
                break
        
        return ls