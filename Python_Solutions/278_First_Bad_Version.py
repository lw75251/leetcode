# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        My Solution: O(log(n)) Solution

        IDEA: Binary Search

        # Time Complexity: O(log(n))
        # Space Complexity: O(1)
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
