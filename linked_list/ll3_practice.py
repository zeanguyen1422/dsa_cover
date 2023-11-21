# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        curnode_pointer = head 

        carry = 0 

        while l1 or l2 is not None:

            sum = 0 + carry 
            
            if l1 is not None:
                sum += l1.val
                l1 = l1.next

            if l2 is not None:
                sum += l2.val 
                l2 = l2.next

            carry = sum // 10
            sum = sum % 10 
            curnode_pointer.next = ListNode(sum)
            curnode_pointer = curnode_pointer.next

            
            if carry:
                curnode_pointer.next = ListNode(carry)
        return head.next 



            
        
        