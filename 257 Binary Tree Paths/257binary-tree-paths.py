# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths1(self, root, ls1, ls):
        if (root == None):
            return
        
        ls1.append(str(root.val))

        if ((root.left == None) and (root.right == None)):
            s = "->".join(ls1)
            ls.append(s)
            
        self.binaryTreePaths1(root.left, ls1, ls)
        self.binaryTreePaths1(root.right, ls1, ls)
        ls1.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ls = []
        ls1 = []

        self.binaryTreePaths1(root, ls1, ls)
        
        return ls