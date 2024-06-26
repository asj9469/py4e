# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # multiple pass method (get length)
        # time complexity: O(n)
        # space complexity: O(1)

        temp = head
        length = 0

        while temp:
            temp = temp.next
            length += 1

        pos = length - n
        count = 0
        new = newHead = ListNode()
        new.next = head

        while new:
            if count == pos:
                new.next = new.next.next if new.next else None
            new = new.next
            count += 1

        return newHead.next