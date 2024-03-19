# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution:
    def fourSum(self, nums: list[int], target) -> list[list[int]]:
        # time complexity: O(n^3)
        # space complexity: O(n)

        lmap = {}  # {num, index}
        outputSet = set()

        for l in range(len(nums)):
            lmap[nums[l]] = l

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = j + 1
                while k < len(nums):
                    numNeeded = target - (nums[i] + nums[j] + nums[k])
                    if numNeeded in lmap:
                        if lmap[numNeeded] != i and lmap[numNeeded] != j and lmap[numNeeded] != k:
                            outputSet.add(tuple(sorted((nums[i], nums[j], nums[k], numNeeded))))
                    k += 1

        return outputSet