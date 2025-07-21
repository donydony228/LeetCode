# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lists = []
        while head:
            lists.append(head.val)
            head = head.next
        # print(lists)
        # print(lists[::-1])
        return lists == lists[::-1]