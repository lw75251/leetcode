class Solution:
    """
    My Solution: O(n) Solution

    Idea: Go through each element and check to see if we have
    seen the element before. Regardless, add to a set (sets cannot
    contain dups).

    # Time Complexity: O(n), where n = len(nums)
    # Space Complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    """
    My Solution 2: O(n) Solution

    IDEA: Sort the elements, then go through to see if
    any dups.

    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)-1):
            if nums[i-1] == nums[i]:
                return True
        return False

    """
    One-Liner Solution: O(n) Solution

    IDEA: Compare the lengths of nums and the set of nums. If they're equal,
    then we know all elements are unique. Otherwise, there were duplicates.

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums) == len(set(nums)) else True
