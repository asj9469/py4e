# https://leetcode.com/problems/symmetric-tree/description/

# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSym(node1, node2):

            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val == node2.val:
                return checkSym(node1.left, node2.right) and checkSym(node1.right, node2.left)
            else:
                return False

        return checkSym(root.left, root.right)