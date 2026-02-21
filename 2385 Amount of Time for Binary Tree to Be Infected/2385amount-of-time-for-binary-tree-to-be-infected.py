from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findParentNodes(self, root, parent, d):
        if (root == None):
            return
        
        d[root.val] = parent

        self.findParentNodes(root.left, root, d)
        self.findParentNodes(root.right, root, d)
    
    def findStartNode(self, root, start):
        if (root == None):
            return root
        
        if (root.val == start):
            return root
        
        left = self.findStartNode(root.left, start)

        if (left != None):
            return left
        
        return self.findStartNode(root.right, start)
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d = {}

        self.findParentNodes(root, None, d)

        start_node = self.findStartNode(root, start)

        time = 0
        q = deque()
        q.append(start_node)
        s = set()
        s.add(start_node)

        while (len(q) != 0):
            d1 = len(q)

            for i in range(d1):
                node = q.popleft()

                if ((node.left != None) and (node.left not in s)):
                    q.append(node.left)
                    s.add(node.left)
                if ((node.right != None) and (node.right not in s)):
                    q.append(node.right)
                    s.add(node.right)
                if ((d[node.val] != None) and (d[node.val] not in s)):
                    q.append(d[node.val])
                    s.add(d[node.val])
            
            time += 1
        
        return (time - 1)