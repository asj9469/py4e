# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # brute force method (time limit exceeded)
        # time complexity: O(n^2)
        # space complexity: O(n)

        output = [0 for i in temperatures]

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]: # found warmer temp
                    output[i] = j-i
                    break

        return output

###################################
        # stack method
        # time complexity: O(n)
        #    -> at most it iterates the stack once despite the while loop (while loop goes backwards)
        # space complexity: O(n)

        stack = []
        output = [0 for i in temperatures]

        for i in range(len(temperatures)):
            if stack:
                while stack and stack[-1][0] < temperatures[i]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append((temperatures[i], i))

        return output

