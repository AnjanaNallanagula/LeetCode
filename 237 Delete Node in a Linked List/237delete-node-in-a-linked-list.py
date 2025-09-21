# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        next1 = node.next
        node.val = next1.val        
        node.next = next1.next
        next1.next = None