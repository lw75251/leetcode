class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        My Solution: Brute Force Solution

        IDEA: We explore all possibilities. Given the rules,
        integerReplacement(n) will converge to 1 for all integers.
        Thus, we can use recursion to see how many steps it will take.
        When odd, we explore BOTH possibilities of adding or subtracting,
        and take the route with the minimal steps.

        # Time Complexity: O(n) by Master's Theorem.
        # Recurrence Relation = 2T(n/2) + O(1)
        # Space Complexity: O(n)
        """
        # Base Case: n == 1
        if n == 1:
            return 0

        # Even
        if n % 2 == 0:
            return self.integerReplacement(n/2) + 1

        # Odd
        else:
            add = self.integerReplacement(n+1) + 1
            subtract = self.integerReplacement(n-1) + 1
            return min(add, subtract)

    def integerReplacement(self, n: int) -> int:
        """
        My Solution: Dynamic Programming

        IDEA: We explore all possibilities, but we can see that we may
        be doing repeated work. Thus, we want to store previous calculations
        to be more efficient.

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        """
        def min_operations(n: int):
            # Previously Calculated Result
            if n in dp:
                return dp[n]

            # Even
            if n % 2 == 0:
                dp[n] = min_operations(n/2) + 1

            # Odd
            else:
                dp[n] = min(min_operations(n+1), min_operations(n-1)) + 1

            return dp[n]

        dp = {}
        dp[1] = 0
        return min_operations(n)
