# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSequence(self, root, ls):
        if (root == None):
            return
        
        if (root.left == None and root.right == None):
            ls.append(root.val)
        
        self.leafSequence(root.left, ls)
        self.leafSequence(root.right, ls)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ls1 = []
        ls2 = []

        self.leafSequence(root1, ls1)
        self.leafSequence(root2, ls2)

        if (ls1 == ls2):
            return True
        return False