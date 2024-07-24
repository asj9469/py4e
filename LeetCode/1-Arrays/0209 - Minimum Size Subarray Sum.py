# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
######################################################
# Runtime Complexity = O(n) -> because inner loop isn't executing every time the for loop iterates
# Space Complexity = O(1) -> using no extra storage

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, currSum = 0, 0
        length = float("inf")

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                length = min(length, r-l+1)
                currSum -= nums[l]
                l+=1

        return length if length != float("inf") else 0