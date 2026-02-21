# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        d = 0
        temp = head

        while (temp != None):
            d += 1
            temp = temp.next
        
        return d
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1 = self.count(l1)
        count2 = self.count(l2)

        if (count1 >= count2):
            d = count1 - count2

            for i in range(d):
                new_node = ListNode(0, l2)
                l2 = new_node
        else:
            d = count2 - count1

            for i in range(d):
                new_node = ListNode(0, l1)
                l1 = new_node
        
        stack1 = []
        temp1 = l1
        temp2 = l2

        while (temp1 != None and temp2 != None):
            stack1.append((temp1.val, temp2.val))
            temp1 = temp1.next
            temp2 = temp2.next
        
        sum1 = 0
        carry = 0
        stack2 = []

        while (len(stack1) != 0):
            d1, d2 = stack1.pop()
            sum1 = d1 + d2 + carry
            stack2.append(sum1 % 10)
            carry = sum1 // 10
        
        if (carry > 0):
            stack2.append(carry)
        
        l3 = ListNode(-1)
        temp3 = l3

        while (len(stack2) != 0):
            d = stack2.pop()
            new_node = ListNode(d)
            temp3.next = new_node
            temp3 = temp3.next
        
        l3 = l3.next

        return l3