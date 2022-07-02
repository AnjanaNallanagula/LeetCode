class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        d = [[-1 for j in range(m + 1)] for i in range(n + 1)]
        max1 = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if (i == 0 or j == 0):
                    d[i][j] = 0
                else:
                    if (nums1[i - 1] == nums2[j - 1]):
                        d[i][j] = 1 + d[i - 1][j - 1]
                        max1 = max(max1, d[i][j])
                    else:
                        d[i][j] = 0
        return max1
        