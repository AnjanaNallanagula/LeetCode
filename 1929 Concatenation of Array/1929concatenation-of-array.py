class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ls = [0 for i in range(2 * n)]

        for i in range(len(nums)):
            ls[i] = nums[i]
            ls[i + n] = nums[i]
        
        return ls