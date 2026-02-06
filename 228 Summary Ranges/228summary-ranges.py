class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (nums == []):
            return nums
        
        start = nums[0]
        end = nums[0]
        ls = []

        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1] + 1):
                end = nums[i]
            else:
                s = str(start)

                if (start != end):
                    s += "->" + str(end)
                
                ls.append(s)

                start = nums[i]
                end = nums[i]
        
        s = str(start)

        if (start != end):
            s += "->" + str(end)
                
        ls.append(s)

        return ls