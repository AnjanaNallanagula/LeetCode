# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countSubtrees(self, root, ls):
        if (root == None):
            return True
        
        left = self.countSubtrees(root.left, ls)
        right = self.countSubtrees(root.right, ls)

        if (not left or not right):
            return False
        
        if (root.left and root.val != root.left.val):
            return False
        if (root.right and root.val != root.right.val):
            return False
        
        ls[0] += 1

        return True
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ls = [0]

        self.countSubtrees(root, ls)

        return ls[0]