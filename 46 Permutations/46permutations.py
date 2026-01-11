class Solution:
    def permute1(self, nums, low, high, ls):
        if (low == high):
            ls.append(nums[:])
            return
        
        for i in range(low, high + 1):
            nums[low], nums[i] = nums[i], nums[low]
            self.permute1(nums, low + 1, high, ls)
            nums[low], nums[i] = nums[i], nums[low]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = []

        self.permute1(nums, 0, len(nums) - 1, ls)

        return ls