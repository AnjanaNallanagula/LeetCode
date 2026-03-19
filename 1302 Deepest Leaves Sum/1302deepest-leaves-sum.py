from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        sum1 = 0
        
        while (len(q) != 0):
            d = len(q)
            sum1 = 0
            
            for i in range(d):
                node = q.popleft()
                sum1 += node.val
                
                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)
        
        return sum1