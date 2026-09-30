# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f=head
        s=head

        for i in range(n):
            f=f.next
        
        if f==None:
            return s.next
        while f and f.next:
            s=s.next
            f=f.next
        if s.next and s.next.next:
            s.next=s.next.next
        elif s.next:
            s.next=None
        
        return head
        

        