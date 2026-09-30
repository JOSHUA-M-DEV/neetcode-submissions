# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        p=None
        while h:
            c=h.next
            h.next=p
            p=h
            h=c
        return p
        
        