from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = [-1 for i in range(len(nums1))]
        s = set()
        index = defaultdict(list)
        
        for i in range(len(nums2)):
            index[nums2[i]].append(i)
        
        for i in range(len(nums1)):
            j = index[nums1[i]][0]
            index[nums1[i]].pop(0)
            ls[i] = j
        
        return ls