# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].

# It is guaranteed that the answer is unique.
####################################################
# My approach
# Runtime Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        output = []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        topCount = list(reversed(sorted(count.values())))[:k]

        for key in count.keys():
            if count.get(key) in topCount:
                output.append(key)

        return output