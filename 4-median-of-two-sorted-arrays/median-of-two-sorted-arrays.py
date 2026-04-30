class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums2) < len(nums1)):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        half = (n1 + n2) // 2
        low = 0
        high = n1 - 1

        while (True):
            mid1 = low + (high - low) // 2
            mid2 = half - mid1 - 2

            a_left = nums1[mid1] if (mid1 >= 0) else float("-inf")
            b_left = nums2[mid2] if (mid2 >= 0) else float("-inf")
            a_right = nums1[mid1 + 1] if (mid1 + 1 < n1) else float("inf")
            b_right = nums2[mid2 + 1] if (mid2 + 1< n2) else float("inf")

            if (a_left <= b_right and b_left <= a_right):
                if (total % 2 == 0):
                    return ((max(a_left, b_left) + min(a_right, b_right))) / 2
                else:
                    return min(a_right, b_right)
            elif (a_left > b_right):
                high = mid1 - 1
            else:
                low = mid1 + 1