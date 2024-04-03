# Given an array of strings strs, group the anagrams together. You can ####################################################return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

####################################################
# My Solution
# My solution is more simple than neetcode
# time complexity = O(n)
# space complexity = O(n)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # { anagram : [list of words] }
        anagrams = {}

        for word in strs:
            tempKey = "".join(sorted(word))
            anagrams[tempKey] = anagrams.get(tempKey, []) + [word]

        return anagrams.values()