# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructBinaryTree(self, low, high, nums, d):
        if (low > high):
            return None
        
        max1 = max(nums[low: high + 1])
        index = d[max1]

        root = TreeNode(max1)
        root.left = self.constructBinaryTree(low, index - 1, nums, d)
        root.right = self.constructBinaryTree(index + 1, high, nums, d)

        return root
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        d = {nums[i]: i for i in range(n)}
        max1 = -1
        index = -1

        for i in d:
            if (i > max1):
                max1 = i
                index = d[i]
        
        return self.constructBinaryTree(0, n - 1, nums, d)