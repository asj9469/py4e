# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
############################################
# time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r = 0, 0

        used = set()
        count = 0
        maxCount = 0

        while r <= len(s) - 1:
            if s[r] in used:
                used = set()                        # empty the set
                maxCount = max(maxCount, count)     # update max
                count = 0                           # reset count to 0
                l += 1                              # set both pointers to l+1
                r = l
            else:
                used.add(s[r])                      # add the char at index r into set
                count += 1                          # increase count
                r += 1                              # move right pointer

        return max(maxCount, count)
