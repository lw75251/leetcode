class Solution:
    """
    My Solution: Brute Force Solution

    IDEA: Binary Search

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        while s <= e:
            m = (s+e)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1

    """
    Non-Bug Solution:

    # Time Complexity: O(logn)
    # Space Complexity: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums)-1
        while s <= e:
            # This will prevent the possibility of overflow
            m = (s + (e - s)) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1
