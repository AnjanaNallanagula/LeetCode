class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        
        if (len(b) < len(a)):
            return self.findMedianSortedArrays(b, a)
        
        total = len(a) + len(b)
        half = total // 2
        low = 0
        high = len(a) - 1

        while (True):
            mid1 = low + (high - low) // 2
            mid2 = half - mid1 - 2

            a_left = a[mid1] if (mid1 >= 0) else float("-inf")
            a_right = a[mid1 + 1] if (mid1 + 1 < len(a)) else float("inf")
            b_left = b[mid2] if (mid2 >= 0) else float("-inf")
            b_right = b[mid2 + 1] if (mid2 + 1 < len(b)) else float("inf")

            if (a_left <= b_right and b_left <= a_right):
                if (total % 2 == 0):
                    return ((max(a_left, b_left) + min(a_right, b_right)) / 2)
                else:
                    return (min(a_right, b_right))
            elif (a_left > b_right):
                high = mid1 - 1
            else:
                low = mid1 + 1