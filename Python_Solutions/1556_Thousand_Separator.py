class Solution:
    def thousandSeparator(self, n: int) -> str:
        """
        My Solution: O(n) Time

        IDEA: Format string, then replace commas with dots.

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        """
        return "{:,}".format(n).replace(",", ".")
