# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

######################################################3
# passed 37/38 test cases
# last one failed bc time limit exceeded
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > 0 :
            last = nums[len(nums)-1]
            temp = nums[len(nums)-1-k] if len(nums)-1-k > 1 else nums[0]
            for i in range(k):
                for i in range(len(nums)-1):
                    temp = nums[i]
                    nums[i] = last
                    last = temp
                    # print(nums)
            nums[len(nums)-1] = temp
