# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return None
        
        slow = head
        fast = head
        prev = head

        while (fast and fast.next):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        slow.next = None

        return head