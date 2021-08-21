class Solution:
    def maximum69Number(self, num: int) -> int:
        """
        My Solution: O(d) Solution

        IDEA: We take a greedy approach and change look at the digits from
        left to right. If there is a 6 before a 9, then we know if we change
        it to a 9 the number will always be greater than before. Otherwise,
        we do not make any changes.

        IMPLEMENTATION IDEAS:
        - Can Convert to a string first, then look for first 6
        - Use math to iteratively look through the digits to find the first 6

        # Time Complexity: O(d), where d = number of digits in num
        # Space Complexity: O(1)
        """
        n = str(num)
        return n.replace("6", "9", 1)
