# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes1(self, root, ls, ls1, max1):
        if (root == None):
            return
        
        ls1.append(root.val)

        if (root.val >= max1[0]):
            max1[0] = root.val
            ls[0] += 1
        
        self.goodNodes1(root.left, ls, ls1, max1)
        self.goodNodes1(root.right, ls, ls1, max1)

        d = ls1.pop()

        if (d == max1[0]):
            if (ls1 != []):
                max1[0] = max(ls1)
            else:
                max1[0] = 0
                
    def goodNodes(self, root: TreeNode) -> int:
        ls = [0]
        ls1 = []
        max1 = [float("-inf")]

        self.goodNodes1(root, ls, ls1, max1)

        return ls[0]