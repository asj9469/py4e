# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#       Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
#       The remaining elements of nums are not important as well as the size of nums.
#       Return k.
#
# Example:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

####################################################
# My Initial Approach

def removeDuplicates(self, nums: List[int]) -> int:
    unique = dict()
    ptr = 1

    for i in range(len(nums)):
        curr = nums[i]
        if i == 0:
            unique[curr] = 1
            continue
        elif unique.get(curr, 0) != 0:
            continue
        else:  # if it is a new unique number
            unique[curr] = 1
            temp = curr
            nums[i] = nums[ptr]
            nums[ptr] = temp
            ptr += 1

    return len(unique)

####################################################
# NeetCode Optimized Approach
# super simple - using two pointers to go through the array once each, left pointer only gets updated when unique value is copied over

def removeDuplicates(self, nums: List[int]) -> int:
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l