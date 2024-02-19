# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#
# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
####################################################
# Runtime 39 ms Beats 55.73% of users with Python3
# Memory 16.68 MB Beats 51.43% of users with Python3

## Dynamic Programming Approach (Bottom Up) learned by https://www.youtube.com/watch?v=Hdr64lKQ3e4

class Solution:
    def fib(self, n: int) -> int:

        # edge case handling
        if n == 0: return 0

        # creating a dictionary to store what we already computed
        mem = {}

        for i in range(1, n + 1):
            if i <= 2:
                output = 1
            else:
                output = mem[i - 1] + mem[i - 2]

            # storing the computed value
            mem[i] = output

        return mem[n]