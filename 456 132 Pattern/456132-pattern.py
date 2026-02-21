class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ls = [float("inf") for i in range(len(nums))]

        for i in range(1, len(nums)):
            ls[i] = min(nums[i - 1], ls[i - 1])
        
        s = []

        for i in range(len(nums) - 1, -1, -1):
            if (nums[i] > ls[i]):
                while (len(s) != 0 and s[-1] <= ls[i]):
                    s.pop()
                
                if (len(s) != 0 and s[-1] < nums[i]):
                    return True
            
                s.append(nums[i])
        
        return False