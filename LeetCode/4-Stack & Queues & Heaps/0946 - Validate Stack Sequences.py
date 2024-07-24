# https://leetcode.com/problems/validate-stack-sequences/description/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # codepath approach
        # time complexity: O(n)
        # space complexity: O(n)

        j = 0
        stack = []

        for i in pushed:
            stack.append(i)

            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j+=1

        return j == len(popped)

        # my initial approach
        # time complexiy: O(n)
        # space complexity: O(n)

        newPopped = []
        newPushed = []

        ptr = 0
        while popped:

            if newPushed and popped[0] == newPushed[-1]:
                newPopped.append(newPushed.pop())
                popped.pop(0)
            elif ptr < len(pushed) and popped[0] == pushed[ptr]:
                newPopped.append(popped.pop(0))
                ptr += 1
            elif ptr < len(pushed):
                newPushed.append(pushed[ptr])
                ptr += 1
            else:
                return False

        return True

