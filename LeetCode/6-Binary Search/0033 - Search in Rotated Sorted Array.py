# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search method
        # time complexity: O(log n)
        # space complexity: O(1)

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if target < nums[m]:
                if nums[m] > nums[r] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < nums[r] and target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return l if nums[l] == target else -1