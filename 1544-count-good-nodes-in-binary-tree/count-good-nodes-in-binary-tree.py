# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGoodNodes(self, root, ls, path, max1):
        if (root == None):
            return
        
        if ((len(path) == 0) or (len(path) and root.val >= max1[0])):
            ls[0] += 1
            path.append(root.val)
            max1[0] = root.val
        
        self.countGoodNodes(root.left, ls, path, max1)
        self.countGoodNodes(root.right, ls, path, max1)

        if (max1[0] == root.val):
            path.pop()
            max1[0] = path[-1] if (path) else -1
    
    def goodNodes(self, root: TreeNode) -> int:
        ls = [0]
        path = []
        max1 = [-1]

        self.countGoodNodes(root, ls, path, max1)

        return ls[0]