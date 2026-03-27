"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (head == None):
            return head
        
        temp = head
        
        while (temp != None):
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next.next
        
        temp1 = head
        
        while (temp1 != None):
            if (temp1.random != None):
                temp1.next.random = temp1.random.next
            
            temp1 = temp1.next.next
        
        temp1 = head
        head1 = head.next
        temp2 = head1
        
        while (temp2.next != None):
            temp1.next = temp2.next
            temp2.next = temp1.next.next
            temp1 = temp1.next
            temp2 = temp2.next
        
        return head1