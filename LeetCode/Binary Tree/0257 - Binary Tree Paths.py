# https://leetcode.com/problems/binary-tree-paths/description/
from idlelib.tree import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(root: Optional[TreeNode]) -> list[str]:

        paths = []

        def helper(node, temp):
            if temp != "":
                temp += "->"
            temp += str(node.val)

            if node and not node.left and not node.right: # if we reach the leaf node
                paths.append(temp)
                temp = ""
                return

            if node.left:
                return helper(node.left, temp)
            if node.right:
                return helper(node.right, temp)

        helper(root, "")
        return paths
