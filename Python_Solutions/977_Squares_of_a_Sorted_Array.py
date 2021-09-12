class Solution:
    """
    My Solution: Brute Force

    IDEA: Square each number, then sort the list

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [n**2 for n in nums]
        return sorted(squares)

    """
    My Solution: O(n)

    IDEA: Have Two Pointers, one coming from the left and one
    coming from the right. We append the larger of the two,
    and increment or decrement the left or right respectively.

    # Time Complexity: O(n)
    """
    import collections

    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                ans.appendleft(nums[r])
                r -= 1
            else:
                ans.appendleft(numrs[l])
                l += 1
        return ans
