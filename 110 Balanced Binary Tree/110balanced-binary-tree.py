# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced1(self, root, ls):
        if (root == None):
            return 0
        
        left = self.isBalanced1(root.left, ls)
        right = self.isBalanced1(root.right, ls)
        h = max(left, right) + 1

        if (abs(left - right) > 1):
            ls[0] = False
        
        return h
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ls = [True]

        self.isBalanced1(root, ls)

        return ls[0]