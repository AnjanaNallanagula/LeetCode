# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal1(self, root, ls):
        if (root == None):
            return
        
        ls.append(root.val)
        self.preorderTraversal1(root.left, ls)
        self.preorderTraversal1(root.right, ls)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        
        self.preorderTraversal1(root, ls)
        
        return ls