# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        prev = ListNode(0)
        prev.next = head

        slow = prev
        fast = head

        while fast != None and fast.next != None:
            # print(f"slow:{slow.val}, fast:{fast.val}")
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next

        return prev.next