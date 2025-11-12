# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView1(self, root, level, ls):
        if (root == None):
            return
        
        if (len(ls) == level):
            ls.append(root.val)
        
        self.rightSideView1(root.right, level + 1, ls)
        self.rightSideView1(root.left, level + 1, ls)
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls = []

        self.rightSideView1(root, 0, ls)

        return ls