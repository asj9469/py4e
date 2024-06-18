# https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # naive / brute force approach
        # time complexity: O(n)
        # space complexity: O(n)

        temp = new = ListNode()
        newList = []

        while head:
            if head.val != val:
                newList.append(head.val)
            head = head.next

        for i in newList:
            temp.next = ListNode(i)
            temp = temp.next

        return new.next

##############################################

        # two pointer method
        # time complexity: O(n)
        # space complexity: O(1)

        temp = prev = ListNode()
        prev.next = head

        while head:
            if head.val == val:
                while head and head.val == val:
                    head = head.next
                prev.next = head

            prev = prev.next
            head = head.next if head else None

        return temp.next