class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        My Solution: One Pass O(n) Solution

        Idea: Create an empty array, and loop through string
        and mapping to fill out empty array

        # Time Complexity: O(n), where n = len(s)
        # Space Complexity: 1
        """
        ans = [0]*len(s)
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return "".join(ans)

    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Forum Solution: One Pass O(n) Solution

        Idea: Create an empty array, and utilize enumerate
        for cleaner code.

        # Time Complexity: O(n), where n = len(s)
        # Space Complexity: 1
        """
        ans = [None]*len(s)
        for i, j in enumerate(indices):
            ans[j] = s[i]
        return "".join(ans)
