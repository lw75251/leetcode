class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        My Solution: O(n) Solution

        Idea: Check to see if the current number is the double
        or half of another integer. If it is not, then add both
        the double and half of the current integer to the to seek
        set.

        # Time Complexity: O(n), where n = len(s)
        # Space Complexity: O(n)
        """
        pair = set()
        for n in arr:
            if n in pair:
                return True
            pair.add(n*2)
            pair.add(n/2)
        return False
