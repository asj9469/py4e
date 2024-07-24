# https://leetcode.com/problems/last-stone-weight/description/



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # max() method
        # time complexity: O(n^2) -> max function is O(n)
        # space complexity: O(1)

        while len(stones) > 1:
            big1 = max(stones)
            stones.pop(stones.index(big1))

            big2 = max(stones)
            stones.pop(stones.index(big2))

            print(stones)
            if big1 != big2:
                stones.append(big1 - big2)

        return stones[0] if stones else 0

        # [review] heap method - 6/25/24
        # time complexity: O(n log n)
        # space complexity: O(n)

        newStones = [-i for i in stones]
        heapq.heapify(newStones)

        while len(newStones) > 1:
            big1 = -heapq.heappop(newStones)
            big2 = -heapq.heappop(newStones)

            if big1 != big2:
                heapq.heappush(newStones, -(big1-big2))

        return -newStones[0] if newStones else 0

###############################################################
        # first attempt with heap - 6/9/24
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

