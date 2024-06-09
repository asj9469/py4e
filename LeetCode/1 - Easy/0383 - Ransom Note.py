# https://leetcode.com/problems/ransom-note/

from collections import Counter

# My initial approach
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        numOccur = {}

        for i in magazine:
            numOccur[i] = numOccur.get(i, 0) + 1

        for i in ransomNote:
            if i in numOccur.keys():
                numOccur[i] = numOccur.get(i, 0) - 1
                if numOccur.get(i, 0) == -1:
                    return False
            else:
                return False

        return True

# neetcode approach
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)

        for i in ransomNote:
            if mCounter[i] < rCounter[i]:
                return False

        return True