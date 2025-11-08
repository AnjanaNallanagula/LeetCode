class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max1 = -1
        max2 = -1
        count1 = 0
        count2 = 0

        for i in nums:
            if (i == max1):
                count1 += 1
            elif (i == max2):
                count2 += 1
            elif (count1 == 0):
                max1 = i
                count1 = 1
            elif (count2 == 0):
                max2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for i in nums:
            if (i == max1):
                count1 += 1
            elif (i == max2):
                count2 += 1
        
        ls = []

        if (count1 > len(nums) // 3):
            ls.append(max1)
        if (count2 > len(nums) // 3):
            ls.append(max2)

        return ls