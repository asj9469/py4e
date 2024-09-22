# https://leetcode.com/problems/maximum-subarray/
# greedy algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # runtime complexity: O(n)
        # space complexity: O(1)

        maxSum, currSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)

        return maxSum