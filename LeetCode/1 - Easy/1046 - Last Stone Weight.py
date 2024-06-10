# https://leetcode.com/problems/last-stone-weight/description/

# My initial approach
# time complexity: O(n log n)
# space complexity: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # time complexity: O(n log n)
        # space complexity: O(n)

        if len(stones) == 1:
            return stones[0]

        stonesClone = [-1 * x for x in stones]
        heapq.heapify(stonesClone)

        while len(stonesClone) > 1:
            stone1 = -1 * heapq.heappop(stonesClone)
            stone2 = -1 * heapq.heappop(stonesClone)

            diff = stone1 - stone2
            if diff > 0:
                heapq.heappush(stonesClone, -1 * diff)

        return -1 * stonesClone[0] if stonesClone else 0

