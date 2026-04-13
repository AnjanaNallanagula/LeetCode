import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeNode(Node):
    def __init__(self, val = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def evaluate(self):
        if (self.val.isdigit() == True):
            return int(self.val)
        
        left = self.left.evaluate()
        right = self.right.evaluate()

        if (self.val == "+"):
            return (left + right)
        elif (self.val == "-"):
            return (left - right)
        elif (self.val == "*"):
            return (left * right)
        else:
            return (left // right)
        

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []

        for i in range(len(postfix)):
            node = TreeNode(postfix[i])

            if (postfix[i] in "+-*/"):
                right = stack.pop()
                left = stack.pop()
                node.left = left
                node.right = right
            
            stack.append(node)
        
        return stack[-1]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        