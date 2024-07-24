# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.
#
# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
####################################################
# initial approach
# time complexity: O(1) each
# space complexity: O(n)
class MinStack:

    def __init__(self):
        self.stack = list()
        self.map = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.map[val] = self.map.get(val, 0) + 1

    def pop(self) -> None:
        self.map[self.stack[-1]] -= 1
        if self.map.get(self.stack[-1]) == 0:
            self.map.pop(self.stack[-1])
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.map)

# new approach (neetcode)
    def __init__(self):
        self.stack = list()
        self.minStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        currMin = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]