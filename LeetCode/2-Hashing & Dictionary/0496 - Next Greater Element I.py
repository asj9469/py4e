# https://leetcode.com/problems/next-greater-element-i/description/

# my initial solution
# time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        output = []
        numPos = {}

        for i in range(len(nums2)):
            numPos[nums2[i]] = i

        for i in nums1:
            temp = -1
            for j in range(numPos[i], len(nums2)):
                if nums2[j] > i:
                    temp = nums2[j]
                    break
            output.append(temp)

        return output
