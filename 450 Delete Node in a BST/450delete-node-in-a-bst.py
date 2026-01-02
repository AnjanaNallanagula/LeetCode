# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderPredecessor(self, root):
        prev = root.left

        while (prev != None and prev.right != None):
            prev = prev.right
        
        return prev
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (root == None):
            return root
        
        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        else:
            if (root.left == None):
                return root.right
            if (root.right == None):
                return root.left
            
            prev = self.inorderPredecessor(root)
            root.val = prev.val

            root.left = self.deleteNode(root.left, prev.val)
        
        return root