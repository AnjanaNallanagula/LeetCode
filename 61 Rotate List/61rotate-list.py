# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        count = 0
        temp = head

        while (temp != None):
            count += 1
            temp = temp.next
        
        k = k % count

        if (k == 0):
            return head

        temp = head
        prev = head

        for i in range(k + 1):
            prev = temp
            temp = temp.next
        
        prev.next = None
        head1 = temp

        while (temp.next != None):
            temp = temp.next
        
        temp.next = head

        return head1