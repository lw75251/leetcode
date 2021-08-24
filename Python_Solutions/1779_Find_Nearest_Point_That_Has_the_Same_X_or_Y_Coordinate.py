class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        My Solution: O(n) Solution

        Idea: Go through each point, if it is a valid point then calculate a
        Manhattan Distance. If that distance turns out to be the min 
        distance, then we save that index and distance. For tie breakers,
        we keep the earliest occurrence.

        Created helper functions to make code easier to read

        # Time Complexity: O(n), where n = len(s)
        # Space Complexity: 1
        """

        def isValidPoint(point: List[int]):
            return True if x == point[0] or y == point[1] else False

        def calculateDistance(point: List[int]):
            return abs(x - point[0]) + abs(y - point[1])

        valid_point_index = -1
        min_dist = float('inf')
        for i, p in enumerate(points):
            if isValidPoint(p):
                dist = calculateDistance(p)
                if calculateDistance(p) < min_dist:
                    min_dist = dist
                    valid_point_index = i
        return valid_point_index
