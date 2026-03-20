# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST1(self, root, low, high, sum1):
        if (root == None):
            return
        
        self.rangeSumBST1(root.left, low, high, sum1)
        self.rangeSumBST1(root.right, low, high, sum1)
        
        if (root.val < low or root.val > high):
            return
        
        sum1[0] += root.val
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum1 = [0]
        
        self.rangeSumBST1(root, low, high, sum1)
        
        return sum1[0]