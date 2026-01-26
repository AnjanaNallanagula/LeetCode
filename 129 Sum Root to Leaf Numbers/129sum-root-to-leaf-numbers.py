# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers1(self, root, ls, ls1):
        if (root == None):
            return
        
        ls1[0] = ls1[0] * 10 + (root.val)

        if (root.left == None and root.right == None):
            ls[0] += ls1[0]
        
        self.sumNumbers1(root.left, ls, ls1)
        self.sumNumbers1(root.right, ls, ls1)

        ls1[0] //= 10
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ls = [0]
        ls1 = [0]

        self.sumNumbers1(root, ls, ls1)

        return ls[0]