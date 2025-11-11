"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph1(self, node, d):
        if (node == None):
            return node
        if (node in d):
            return d[node]
        
        d[node] = Node(node.val, [])

        for j in node.neighbors:
            d[node].neighbors.append(self.cloneGraph1(j, d))
        
        return d[node]
        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}

        return self.cloneGraph1(node, d)