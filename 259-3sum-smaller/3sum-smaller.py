class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                sum1 = nums[i] + nums[j] + nums[k]

                if (sum1 < target):
                    count += (k - j)
                    j += 1
                else:
                    k -= 1
        
        return count