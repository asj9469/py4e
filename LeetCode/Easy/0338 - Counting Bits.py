# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
####################################################
# My initial approach
# Runtime 109 ms Beats 23.38% of users with Python3
# Memory 23.17 MB Beats 92.36% of users with Python3

class Solution:
    def countBits(self, n: int) -> List[int]:

        numsOf1 = []
        for i in range(n + 1):
            count = 0
            # iterating through the bits to count the number of ones
            while i:
                if (i & 0x1) == 1:
                    count += 1
                i >>= 1
            numsOf1.append(count)

        return numsOf1