"""
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        My Solution: O(n) Time

        IDEA: Create a set of seen numbers. Then, 
        iterate 0...n to see which number is missing.

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        """
        n = len(nums)
        seen = set()

        for i in nums:
            seen.add(i)

        for i in range(n+1):
            if i not in seen:
                return i

        return -1

    def missingNumber(self, nums: List[int]) -> int:
        """
        My Solution: O(n) Time AND O(1) Space

        IDEA: Iterate through the array, swapping the numbers and place them 
        in their "correct" index. We resolve collisons by placing in left most
        empty spot.

        Case 1: Last number missing => All numbers in correct spots
        Case 2: First number missing => All numbers in index + 1
        Case 3: Middle number missing => Some number will be in the wrong spot

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        """

        # See which number is out of index
        for i, n in enumerate(nums):
            if i != n:
                return i + 1

        return len(nums) + 1
