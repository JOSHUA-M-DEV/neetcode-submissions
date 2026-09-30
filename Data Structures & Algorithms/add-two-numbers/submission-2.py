# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        d=ListNode(-1)
        s=d
        while l1 and l2:
            s.next=ListNode((l1.val+l2.val+c)%10)
            s=s.next
            c=(l1.val+l2.val+c)//10
            l1=l1.next
            l2=l2.next
        while l1:
            s.next=ListNode((l1.val+c)%10)
            s=s.next
            c=(l1.val+c)//10
            l1=l1.next
        while l2:
            s.next=ListNode((l2.val+c)%10)
            s=s.next
            c=(l2.val+c)//10
            l2=l2.next
        if c>0:
            s.next=ListNode(c)
        

        return d.next


            
        