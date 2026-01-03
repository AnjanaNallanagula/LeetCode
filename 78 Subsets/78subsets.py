class Solution:
    def subsets1(self, nums, i, ls, ls1):
        if (i == len(nums)):
            ls.append(ls1[:])
            return
        
        ls1.append(nums[i])
        self.subsets1(nums, i + 1, ls, ls1)
        ls1.pop()
        self.subsets1(nums, i + 1, ls, ls1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = []
        ls1 = []

        self.subsets1(nums, 0, ls, ls1)

        return ls