# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftBoundaryTraversal(self, root, ls):
        if ((root == None) or (root.left == None and root.right == None)):
            return
        
        ls.append(root.val)

        if (root.left != None):
            return self.leftBoundaryTraversal(root.left, ls)
        elif (root.right != None):
            return self.leftBoundaryTraversal(root.right, ls)
    
    def leafNodesTraversal(self, root, ls):
        if (root == None):
            return
        
        self.leafNodesTraversal(root.left, ls)
        self.leafNodesTraversal(root.right, ls)

        if (root.left == None and root.right == None):
            ls.append(root.val)
    
    def rightBoundaryTraversal(self, root, ls):
        if ((root == None) or (root.left == None and root.right == None)):
            return
        
        if (root.right != None):
            self.rightBoundaryTraversal(root.right, ls)
        elif (root.left != None):
            self.rightBoundaryTraversal(root.left, ls)
        
        ls.append(root.val)
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ls = [root.val]

        if (root.left == None and root.right == None):
            return ls

        self.leftBoundaryTraversal(root.left, ls)
        self.leafNodesTraversal(root, ls)
        self.rightBoundaryTraversal(root.right, ls)

        return ls