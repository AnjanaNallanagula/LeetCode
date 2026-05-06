class Solution:
    def permute1(self, low, high, nums, s):
        if (low == high):
            s.add(tuple(nums[:]))
            return
        
        for i in range(low, high + 1, 2):
            nums[low], nums[i] = nums[i], nums[low]
            self.permute1(low + 1, high, nums, s)
            nums[low], nums[i] = nums[i], nums[low]
    
    def permute(self, n: int) -> List[List[int]]:
        s = set()
        nums = [i for i in range(1, n + 1)]

        self.permute1(0, n - 1, nums, s)

        nums = [i for i in range(n, 0, -1)]
        
        self.permute1(0, n - 1, nums, s)

        ls = [list(i) for i in s]
        ls.sort()

        return ls