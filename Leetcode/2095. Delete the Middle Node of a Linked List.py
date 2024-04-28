"""
2095. Delete the Middle Node of a Linked List
"""
# Struggled a bit at the initial case when we have [1, 2] kinda cases, need to move the fast pointer first and then check for fast is None or fast.next is None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        if head.next is None:
            return None
        
        while True:
            fast = fast.next.next
            if fast is None or fast.next is None:
                break
            slow = slow.next

        slow.next = slow.next.next

        return head
