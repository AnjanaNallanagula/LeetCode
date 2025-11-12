# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest1(self, root, k, ls):
        if (root == None):
            return -1
        
        left = self.kthSmallest1(root.left, k, ls)

        if (left != -1):
            return left
        
        ls[0] += 1

        if (ls[0] == k):
            return (root.val)
        
        return self.kthSmallest1(root.right, k, ls)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = [0]

        return self.kthSmallest1(root, k, ls)