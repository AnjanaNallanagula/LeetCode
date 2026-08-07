# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        
        temp = head

        while (temp != None):
            prev = temp

            while (temp != None and temp.val == prev.val):
                temp = temp.next
            
            prev.next = temp
        
        return head