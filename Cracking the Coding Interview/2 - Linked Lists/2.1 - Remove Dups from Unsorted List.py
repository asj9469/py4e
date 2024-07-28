# write code to remove duplicates from an UNSORTED linked list
# FOLLOW UP: how would you solve this problem if a temporary buffer (extra space) is not allowed?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # hashmap method
    # runtime complexity: O(n)
    # space complexity: O(n)
    def deleteNodes(self, head: ListNode):
        hash = set()
        prev = None

        while head:
            if head.val in hash:
                prev.next = head.next
            else:
                hash.add(head.val)
                prev = head
            head = head.next

    # runner method (no extra space)
    # for each element, go through the rest of the linked list to check if there are any duplicates
    # runtime complexity: O(n^2)
    # space complexity: O(1)
    def deleteNodes2(self, head: ListNode):
        curr = head
        while curr:
            runner = curr
            while runner.next:
                if runner.next.val == curr.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
                curr = curr.next