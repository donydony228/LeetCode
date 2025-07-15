# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd_one = head
        even_one = head.next
        ehead = even_one

        while even_one != None and even_one.next != None:
            odd_one.next = odd_one.next.next
            even_one.next = even_one.next.next
            odd_one = odd_one.next
            even_one = even_one.next
        odd_one.next = ehead
        
        return head