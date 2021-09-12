class Solution:
    def countSegments(self, s: str) -> int:
        """
        IDEA: Split the string and count the length

        # Time Complexity: O(n)
        # Space Complexity: 1
        """
        return len(s.split())
