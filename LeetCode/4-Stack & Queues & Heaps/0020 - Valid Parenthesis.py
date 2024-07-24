# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#       Open brackets must be closed by the same type of brackets.
#       Open brackets must be closed in the correct order.
#       Every close bracket has a corresponding open bracket of the same type.
# Example 1:
#   Input: s = "()"
#   Output: true
#
# Example 2:
#   Input: s = "()[]{}"
#   Output: true
#
# Example 3:
#   Input: s = "(]"
#   Output: false

####################################################
# My New Approach
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {")" : "(", "]" : "[", "}" : "{" }

        if s[0] in pairs:
            return False

        for i in s:
            if i in pairs:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[i]:
                    stack.pop()
                    continue
            stack.append(i)

        return len(stack) == 0


# My Initial Approach
# Runtime 34ms Beats 81.81% of users with Python3
# Memory 17.46 MB Beats 9.75% of users with Python3
#
#     dict = {
#         "]": "[",
#         "}": "{",
#         ")": "("
#     }
#
#     par = []
#     for i in s:
#         if len(par) == 0 and i in dict.keys():
#             return False
#
#         if i in dict.values():
#             par.append(i)
#         else:
#             if par[-1] == dict.get(i):
#                 par.pop()
#             else:
#                 return False
#
#     return True if len(par) == 0 else False