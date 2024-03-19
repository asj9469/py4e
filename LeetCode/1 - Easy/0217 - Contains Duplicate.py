# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#
# # Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

####################################################
# My Initial Approach

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # approach 1: add everything in count and then check if anything is 2
        # Runtime 456ms Beats 51.99% of users with Python3
        # Memory 34.65 MB Beats 14.75% of users with Python3
        count = dict()
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for i in count:
            if count[i] != 1:
                return True

        return False

        # approach 2: check if the value is in dict and return true if it does
        # Runtime 428 ms Beats 70.03% of users with Python3
        # Memory 34.71 MB Beats 14.01% of users with Python3
        count = dict()
        for i in range(len(nums)):
            if count.get(nums[i], 0) == 0:
                count[nums[i]] = count.get(nums[i], 0) + 1
            else:
                return True

        return False