# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum1(self, root, ls):
        if (root == None):
            return 0
        
        left = max(0, self.maxPathSum1(root.left, ls))
        right = max(0, self.maxPathSum1(root.right, ls))

        ls[0] = max(ls[0], root.val + left + right)

        return (root.val + max(left, right))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ls = [float("-inf")]

        self.maxPathSum1(root, ls)

        return ls[0]