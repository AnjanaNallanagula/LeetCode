# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST1(self, low, high, nums):
        if (low > high):
            return None
        
        mid = low + (high - low) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST1(low, mid - 1, nums)
        root.right = self.sortedArrayToBST1(mid + 1, high, nums)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortedArrayToBST1(0, len(nums) - 1, nums)