class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {i: -1 for i in nums1}
        s = []

        for i in range(len(nums2)):
            while (len(s) != 0 and nums2[i] > nums2[s[-1]]):
                d[nums2[s[-1]]] = nums2[i]
                s.pop()
            
            s.append(i)
        
        ls = [d[i] for i in nums1]

        return ls