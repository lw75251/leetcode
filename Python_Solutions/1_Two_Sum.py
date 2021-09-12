class Solution:
    """
    My Solution: Brute Force

    IDEA: Try every combination using two for loops

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    """
    My Solution: One-Pass O(n) Solution

    IDEA: By subtracting the target - element, we will know what values we
    still have to try to search for as we continue. If the current element
    isn't found, then we save the difference.

    The key of the dictionary is the difference, the value is the index.

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            if n in diff:
                return [diff[n], i]
            diff[target-n] = i
        return None
