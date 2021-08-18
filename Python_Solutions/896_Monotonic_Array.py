class Solution:
    """
    My Solution: Two Pass O(N) Solution 1

    IDEA: Take one pass to check if it is monotonically increasing, and then
    another pass to check if it is monotonically decreasing.

    # Time Complexity: O(N), where n = len(nums)
    # Space Complexity: 1
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)-1

        # Check for Monotonically Increasing
        # O(N)
        increasing = True
        for i in range(n):
            if nums[i] > nums[i+1]:
                increasing = False

        # Check for Monotonically Decreasing
        # O(N)
        decreasing = True
        for i in range(n):
            if nums[i] < nums[i+1]:
                decreasing = False

        return increasing or decreasing

    """
    One Pass Solution 2
    
    IDEA: Check for monotonically increasing and monotonically decreasing at
    the same time.
    
    # Time Complexity: O(N), where n = len(nums)
    # Space Complexity: 1
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        # Check for Monotonically Increasing and Decreasing
        # O(N)
        increasing = True
        decreasing = True
        n = len(nums)-1
        for i in range(n):
            if nums[i] > nums[i+1]:
                increasing = False
            if nums[i] < nums[i+1]:
                decreasing = False
        return increasing or decreasing
