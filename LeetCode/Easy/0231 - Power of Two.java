/*
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
*/

// Runtime 1ms Beats 49.23% of users with Java
// Memory 40.49 MB Beats 91.55% of users with Java

class Solution {
    public boolean isPowerOfTwo(int n) {
        // there has to be only one 1 in bit
        // cannot be negative or 0

        if (n<=0) return false;

        int counter = 0;
        for(int i = n; i > 0; i >>=1){
            if((i & 0x1) == 1) counter++;
        }

        return counter > 1 ? false : true;
    }
}