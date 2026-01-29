# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1, head)
        prev = temp
        curr = head
        
        while (curr != None):
            while ((curr != None) and (curr.next != None) and (prev.next.val == curr.next.val)):
                curr = curr.next
            
            if (prev.next != curr):
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        temp = temp.next

        return temp