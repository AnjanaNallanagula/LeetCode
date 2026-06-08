class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ls = [pivot for i in range(n)]
        j = 0

        for i in range(n):
            if (nums[i] < pivot):
                ls[j] = nums[i]
                j += 1
        
        j = n - 1

        for i in range(n - 1, -1, -1):
            if (nums[i] > pivot):
                ls[j] = nums[i]
                j -= 1
        
        return ls