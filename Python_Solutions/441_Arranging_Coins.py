class Solution:
    """
    My Solution 1: O(n) Brute Force Solution

    IDEA: Subtract the ith row starting at 1. We keep incrementing i until
    n-i is negative (which means we went over). Thus, we have to return the
    i-1th row.

    # Time Complexity: O(n)
    # Space Complexity: 1
    """

    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n-i >= 0:
            n -= i
            i += 1
        return i-1

    """
    My Solution 2: O(log(n)) Binary Search

    IDEA: 1 + 2 + 3 +... + k = k(k+1)/2.

    So, we need the max value for k, such that k <= n.

    # Time Complexity: O(log(n))
    # Space Complexity: 1
    """

    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = (l+r) // 2
            k = m*(m+1) // 2
            if k == n:
                return m
            elif k < n:
                l = m + 1
            else:
                r = m - 1

        return r

    """
    Solution 3: O(1) Math

    IDEA: Solve for k in the equation k(k+1) <= N

    So, we need the max value for k, such that k <= n.

    # Time Complexity: O(1)
    # Space Complexity: 1
    """

    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
