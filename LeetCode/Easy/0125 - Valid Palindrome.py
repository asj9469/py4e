# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

####################################################
# Neetcode approach
# Runtime 40 ms Beats 87.58% of users with Python3
# Memory 16.99 MB Beats 98.27% of users with Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # store only alphanumeric characters & compare it with the reversed version of it
        alphaOrDigit = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                alphaOrDigit += i.lower()

        return alphaOrDigit == alphaOrDigit[::-1]

    # Notes:
    # palindrome is forward = backward
    # focusing on this concept, extract all comparable stuff
    # compare forward with backward