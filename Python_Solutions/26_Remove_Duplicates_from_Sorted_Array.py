class Solution:
    """
    CONSTRAINTS: Do not allocate extra space for another array. 
    You must do this by modifying the input array in-place with O(1) 
    extra memory.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        My Solution: O(n) Solution

        IDEA: Anything to the left of the `unique` index will contain all
        unique numbers in sorted order. As we iterate through the array,
        we do not make a swap if we've already seen that number before.
        If we haven't seen the number (it implies the new number is greater),
        then we make `unique` larger by incrementing and swapping.

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        """
        unique = 0
        i = 0
        while i < len(nums):
            # Swap current element with element to the right of # unique
            if nums[unique] != nums[i]:
                unique += 1
                nums[unique], nums[i] = nums[i], nums[unique]
            i += 1

        # Since index starts at 0
        return unique + 1
