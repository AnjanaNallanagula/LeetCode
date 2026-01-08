class Solution:
    def canPartition1(self, n, sum1, mat, nums):
        if (sum1 == 0):
            return True
        if (n == 0):
            return False
        
        if (mat[n][sum1] != -1):
            return mat[n][sum1]
        
        if (nums[n-1] <= sum1):
            mat[n][sum1] = (self.canPartition1(n - 1, sum1 - nums[n-1], mat, nums) or self.canPartition1(n - 1, sum1, mat, nums))
        else:
            mat[n][sum1] = self.canPartition1(n - 1, sum1, mat, nums)
        
        return mat[n][sum1]
    
    def canPartition(self, nums: List[int]) -> bool:
        sum1 = sum(nums)

        if (sum1 % 2 == 1):
            return False
        
        sum1 = sum1 // 2
        n = len(nums)
        mat = [[-1 for j in range(sum1 + 1)] for i in range(n + 1)]

        return self.canPartition1(n, sum1, mat, nums)