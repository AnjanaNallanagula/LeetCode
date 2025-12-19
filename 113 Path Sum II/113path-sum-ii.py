# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum1(self, root, sum1, targetSum, ls, ls1):
        if (root == None):
            return
        
        sum1 += root.val
        ls1.append(root.val)

        if ((root.left == None) and (root.right == None) and (sum1 == targetSum)):
            ls.append(ls1[:])
        
        self.pathSum1(root.left, sum1, targetSum, ls, ls1)
        self.pathSum1(root.right, sum1, targetSum, ls, ls1)

        sum1 -= root.val
        ls1.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ls = []
        ls1 = []
        sum1 = 0

        self.pathSum1(root, 0, targetSum, ls, ls1)

        return ls