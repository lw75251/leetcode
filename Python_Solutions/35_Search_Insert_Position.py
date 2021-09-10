class Solution:
    """
    My Solution: O(log(n)) Solution

    IDEA: Binary Search, and we return the left index since
    this is where the target element should be if it existed.

    # Time Complexity: O(log(n))
    # Space Complexity: O(1)
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
