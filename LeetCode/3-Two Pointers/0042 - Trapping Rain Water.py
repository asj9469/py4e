# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

####################################################
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def trap(height) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        count = 0

        while l < r:
            if height[l] <= height[r]:          # go through each of them
                count += maxL - height[l]       # calculate the current one
                l += 1                          # increment the pointer
                maxL = max(maxL, height[l])     # update maxL for the next while iteration
            else:
                count += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])

        return count
