# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if (head == None or head.next == None):
            return head
        
        next1 = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return next1

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        prev = head

        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if (fast != None):
            prev = slow
            slow = slow.next
        
        prev.next = None

        head1 = self.reverse(slow)

        temp1 = head
        temp2 = head1

        while (temp1 != None and temp2 != None):
            next1 = temp1.next
            next2 = temp2.next
            temp1.next = temp2
            temp2.next = next1
            
            temp1 = next1
            temp2 = next2