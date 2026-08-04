# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildSet(self, root, s):
        if (root == None):
            return
        
        s.add(root.val)
        self.buildSet(root.left, s)
        self.buildSet(root.right, s)
    
    def findTarget1(self, root, k, s):
        if (root == None):
            return False
        
        if ((k - root.val) in s and root.val != (k - root.val)):
            return True
        if (self.findTarget1(root.left, k, s)):
            return True
        return self.findTarget1(root.right, k, s)
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        self.buildSet(root, s)

        return self.findTarget1(root, k, s)