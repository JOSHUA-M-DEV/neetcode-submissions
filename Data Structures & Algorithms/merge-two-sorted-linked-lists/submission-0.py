# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode(-1)
        t=l
        while list1 and list2:
            if list1.val>list2.val:
                t.next=ListNode(list2.val)
                t=t.next
                list2=list2.next
            else:
                t.next=ListNode(list1.val)
                t=t.next
                list1=list1.next
        while list1:
            t.next=ListNode(list1.val)
            t=t.next
            list1=list1.next
        while list2:
            t.next=ListNode(list2.val)
            t=t.next
            list2=list2.next
        return l.next


        