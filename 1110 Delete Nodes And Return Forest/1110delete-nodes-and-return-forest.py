# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes1(self, node, target, ls):
        if (node == None):
            return
        
        if (node.val == target):
            ls.append(node.left)
            ls.append(node.right)
            
            return None
        
        node.left = self.delNodes1(node.left, target, ls)
        node.right = self.delNodes1(node.right, target, ls)
        
        return node
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ls = []
        
        if (root == None or len(to_delete) == 0):
            return ls
        
        ls.append(root)
        
        for target in to_delete:
            for i in range(len(ls)):
                ls[i] = self.delNodes1(ls[i], target, ls)
        
        ls = [i for i in ls if (i != None)]
        
        return ls