# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode(-1)
        head2 = ListNode(-1)
        temp = head
        temp1 = head1
        temp2 = head2

        while (temp != None):
            if (temp.val < x):
                temp1.next = temp
                temp1 = temp1.next
            else:
                temp2.next = temp
                temp2 = temp2.next
            
            temp = temp.next
        
        temp2.next = None
        temp1.next = head2.next
        head1 = head1.next

        return head1