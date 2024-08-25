# https://leetcode.com/problems/pacific-atlantic-water-flow/

# CodePath Approach:
# Iterate through the edges of the matrix and traverse IN to the matrix until we hit lower height

# My Approach:
# Go through each element in the matrix and traverse OUTwardly towards the oceans
# Use 2 functions to track both pacific and atlantic touches -> if both are true, we add to set

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        touchOceans = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                pacificVisited, atlanticVisited = set(), set()

                if reachPacific(heights, i, j, heights[i][j], pacificVisited) and reachAtlantic(heights, i, j,heights[i][j], atlanticVisited):
                    touchOceans.add((i, j))

        return touchOceans


def reachPacific(heights, i, j, prevHeight, visited) -> bool:
    if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i, j) in visited or heights[i][j] > prevHeight:
        return

    visited.add((i, j))

    if i == 0 or j == 0:
        return True

    if (reachPacific(heights, i + 1, j, heights[i][j], visited) or
            reachPacific(heights, i - 1, j, heights[i][j], visited) or
            reachPacific(heights, i, j + 1, heights[i][j], visited) or
            reachPacific(heights, i, j - 1, heights[i][j], visited)):
        return True

    return False


def reachAtlantic(heights, i, j, prevHeight, visited) -> bool:
    if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or (i, j) in visited or heights[i][j] > prevHeight:
        return

    visited.add((i, j))

    if i == len(heights) - 1 or j == len(heights[0]) - 1:
        return True

    if (reachAtlantic(heights, i + 1, j, heights[i][j], visited) or
            reachAtlantic(heights, i - 1, j, heights[i][j], visited) or
            reachAtlantic(heights, i, j + 1, heights[i][j], visited) or
            reachAtlantic(heights, i, j - 1, heights[i][j], visited)):
        return True

    return False