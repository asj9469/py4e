# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # first approach: prev, curr method (intuitive approach)
        # time complexity: O(n)
        # space complexity: O(1)

        if not head:
            return None
        prev = new = head

        while head:
            if prev.val != head.val:
                prev.next = head
                prev = head
            head = head.next

        prev.next = None

        return new

        # second approach: direct two pointer method (codePath approach)
        # time complexity: O(n)
        # space complexity: O(1)

        if not head:
            return None

        temp = l = head
        r = l.next

        while r != None:
            if l.val == r.val:
                l.next = r.next
                r = r.next
            else:
                l = l.next
                r = r.next

        return temp