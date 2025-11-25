# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree1(self, preorder, ls, d, low, high):
        if (low > high):
            return None
        
        data = preorder[ls[0]]
        node = TreeNode(data)
        ls[0] += 1
        index = d[data]

        node.left = self.buildTree1(preorder, ls, d, low, index - 1)
        node.right = self.buildTree1(preorder, ls, d, index + 1, high)

        return node
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}

        for i in range(len(inorder)):
            d[inorder[i]] = i
        
        ls = [0]

        return self.buildTree1(preorder, ls, d, 0, len(inorder) - 1)