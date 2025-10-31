class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ls1 = []
        ls2 = []
        s1 = set()
        s2 = set()

        for i in nums1:
            s1.add(i)
        
        for i in nums2:
            s2.add(i)
        
        for i in s1:
            if (i not in s2):
                ls1.append(i)
        
        for i in s2:
            if (i not in s1):
                ls2.append(i)

        ls = [ls1, ls2]

        return ls