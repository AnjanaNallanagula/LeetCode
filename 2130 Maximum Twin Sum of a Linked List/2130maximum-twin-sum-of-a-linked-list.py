# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr = head
        prev = None

        while (curr != None):
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
        
        return prev
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = head

        while (fast != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        head1 = self.reverse(slow)
        temp = head
        temp1 = head1
        max1 = -1

        while (temp != None and temp1 != None):
            sum1 = temp.val + temp1.val
            max1 = max(max1, sum1)
            temp = temp.next
            temp1 = temp1.next
        
        return max1