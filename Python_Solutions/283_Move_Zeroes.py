class Solution:
    """
    My Solution: One Pass O(n) Solution

    IDEA: Let | be a divider such that everything to the left are non-zero
    elements. As we iterate through the array, when we reach an element
    that is nonzero we swap then increment the divider. 

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[d], nums[i] = nums[i], nums[d]
                d += 1
            i += 1
