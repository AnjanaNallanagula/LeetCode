class Solution:
    def subsetXORSum1(self, i, nums, ls, ls1):
        if (i == len(nums)):
            ls[0] += ls1[0]
            return
        
        ls1[0] ^= nums[i]
        self.subsetXORSum1(i + 1, nums, ls, ls1)

        ls1[0] ^= nums[i]
        self.subsetXORSum1(i + 1, nums, ls, ls1)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        ls = [0]
        ls1 = [0]

        self.subsetXORSum1(0, nums, ls, ls1)

        return ls[0]