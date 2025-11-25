# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum1(self, root, sum1, targetSum, ls):
        if (root == None):
            return
        
        sum1 += root.val
        
        if ((root.left == None) and (root.right == None) and (sum1 == targetSum)):
            ls[0] = True
        
        self.hasPathSum1(root.left, sum1, targetSum, ls)
        self.hasPathSum1(root.right, sum1, targetSum, ls)
        
        sum1 -= root.val
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ls = [False]
        
        self.hasPathSum1(root, 0, targetSum, ls)
        
        return ls[0]