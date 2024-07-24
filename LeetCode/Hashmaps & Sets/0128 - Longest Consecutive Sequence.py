# Longest Consecutive Sequence
# Medium
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        curr, count, maxCount = 0, 1, 0

        for i in numSet:
            curr = i
        while curr - 1 in numSet:
            count += 1
            curr -= 1

            maxCount = max(count, maxCount)
            count = 1

        return maxCount