# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# my approach (sort P & compare with substring sorted)
# time complexity: O(n*m*log(m))
# space complexity: O(n)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        output = []
        sortedP = sorted(p)

        for i in range(len(s)):

            if i + len(p) > len(s):
                return output

            if s[i] not in sortedP:
                continue
            elif sorted(s[i:i + len(p)]) == sortedP:
                output.append(i)

        return output

