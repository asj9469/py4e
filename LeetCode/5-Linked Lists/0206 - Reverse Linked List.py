# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#############################################
# Neetcode approach
# refer to notes
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # reverse the order of the pointer
            temp = curr.next
            curr.next = prev
            # shift prev and curr to right side
            prev = curr
            curr = temp

        # have to return prev because the last iternation of the while loop sets curr to None
        return prev