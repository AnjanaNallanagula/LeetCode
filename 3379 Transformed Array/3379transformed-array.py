class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)

        for i in range(n):
            if (nums[i] > 0):
                index = (i + nums[i]) % n
            elif (nums[i] < 0):
                index = (n + i + nums[i]) % n
            else:
                index = i
            
            result.append(nums[index])
        
        return result