# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

####################################################
# My Initial Approach
# Runtime 47ms beats 76.97% of users with Python3
# Memory 16.93mb beats 65.23% of users with Python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first check if the length is equal
        if len(s) != len(t):
            return False

        # count each letters for both strings in dictionary
        # and then compare the numbers for each entry
        # since the length are equal at this point, just do it in one loop

        ogCount = {}
        newCount = {}
        for i in range(len(s)):
            ogCount[s[i]] = ogCount.get(s[i], 0) + 1
            newCount[t[i]] = newCount.get(t[i], 0) + 1

        # go through ogCount and compare key, value with newCount
        ## Neetcode: this part is unnecessary because in Python3, you can just compare if the dictionary is equal
        for key in ogCount.keys():
            if ogCount.get(key) != newCount.get(key):
                return False

        return True

####################################################
# Neetcode Approach
# difference: returns the boolean value if the dictionary is equal
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #you can just compare this without another for loop
