# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        if (left == right):
            return head
        
        temp = ListNode(-501)
        temp.next = head
        prev = temp

        for i in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        prev1 = prev
        curr1 = curr
    
        for i in range(right - left + 1):
            next1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = next1
        
        prev.next = prev1
        curr.next = curr1
        temp = temp.next

        return temp