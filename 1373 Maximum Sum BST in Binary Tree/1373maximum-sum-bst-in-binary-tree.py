# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST1(self, root, ls, min1, max1):
        if (root == None):
            return (True, 0, float("inf"), float("-inf"))
        
        left = self.maxSumBST1(root.left, ls, min1, root.val)
        right = self.maxSumBST1(root.right, ls, root.val, max1)

        if ((left[0] == True) and (right[0] == True) and (left[3] < root.val < right[2])):
            sum1 = root.val + left[1] + right[1]
            ls[0] = max(ls[0], sum1)

            return (True, sum1, min(left[2], root.val), max(right[3], root.val))
        
        return (False, 0, min1, max1)
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ls = [0]

        self.maxSumBST1(root, ls, float("-inf"), float("inf"))

        return ls[0]